#!/usr/bin/env python3
"""Nettoie un notebook Colab avant de le versionner.

- supprime toutes les sorties de cellules et les compteurs d'exécution
- supprime les métadonnées propres à Colab (identité de l'utilisateur, horodatages)
- remplace les identifiants écrits en dur par des variables d'environnement
- signale les chaînes qui ressemblent encore à des secrets

Usage :
    python tools/clean_notebook.py entree.ipynb sortie.ipynb
    python tools/clean_notebook.py --from-drive-json export.json sortie.ipynb
"""
import base64
import json
import re
import sys

SENSITIVE = r"(password|passwd|pwd|secret|token|api_?key|client_?id|client_?secret|username|login)"
# nom = "valeur"   ou   "nom": "valeur"
ASSIGN = re.compile(
    rf"^(?P<indent>\s*)(?P<name>\w*{SENSITIVE}\w*)\s*=\s*(?P<q>['\"]).*?(?P=q)\s*(#.*)?$",
    re.IGNORECASE,
)
DICT_ENTRY = re.compile(
    rf"(?P<key>(?P<kq>['\"])\w*{SENSITIVE}\w*(?P=kq))\s*:\s*(?P<q>['\"])[^'\"]+(?P=q)",
    re.IGNORECASE,
)
BEARER = re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}")
SUSPECT = re.compile(r"['\"][A-Za-z0-9+/=_\-]{32,}['\"]")


def env_name(name: str) -> str:
    return re.sub(r"\W+", "_", name).upper()


def clean_source(lines):
    """Retourne (lignes nettoyées, noms de variables d'environnement utilisées)."""
    used, out = set(), []
    for line in lines:
        text = line.rstrip("\n")
        m = ASSIGN.match(text)
        if m:
            var = env_name(m.group("name"))
            used.add(var)
            text = f'{m.group("indent")}{m.group("name")} = os.environ["{var}"]  # défini hors du notebook (.env.example)'
        else:
            def repl(d):
                var = env_name(d.group("key").strip("'\""))
                used.add(var)
                return f'{d.group("key")}: os.environ["{var}"]'
            text = DICT_ENTRY.sub(repl, text)
            text = BEARER.sub("Bearer " + "{TOKEN}", text)
        out.append(text + ("\n" if line.endswith("\n") else ""))
    return out, used


def clean_notebook(nb):
    used_all, warnings = set(), []
    for i, cell in enumerate(nb.get("cells", [])):
        cell.pop("outputs", None)
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        src = cell.get("source", [])
        if isinstance(src, str):
            src = src.splitlines(keepends=True)
        if cell.get("cell_type") == "code":
            src, used = clean_source(src)
            used_all |= used
            for l in src:
                if SUSPECT.search(l):
                    warnings.append(f"cellule {i}: {l.strip()[:30]}…")
        cell["source"] = src
        keep = {k: v for k, v in cell.get("metadata", {}).items() if k in ("id",)}
        cell["metadata"] = keep
    nb["metadata"] = {
        "colab": {"provenance": []},
        "kernelspec": nb.get("metadata", {}).get("kernelspec", {"name": "python3", "display_name": "Python 3"}),
        "language_info": {"name": "python"},
    }
    if used_all:
        header = {
            "cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [],
            "source": ["import os  # les identifiants sont lus dans l'environnement (voir .env.example)\n"],
        }
        nb["cells"].insert(0, header)
    return nb, sorted(used_all), warnings


def main(argv):
    from_drive = "--from-drive-json" in argv
    args = [a for a in argv if not a.startswith("--")]
    src, dst = args[0], args[1]
    raw = json.load(open(src, encoding="utf-8"))
    nb = json.loads(base64.b64decode(raw["content"])) if from_drive else raw
    nb, used, warnings = clean_notebook(nb)
    with open(dst, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print(f"{dst}: variables d'environnement = {used or '-'}")
    for w in warnings:
        print("  ATTENTION chaîne suspecte :", w)


if __name__ == "__main__":
    main(sys.argv[1:])
