from urllib import request
import json
import os
import glob

def template(name, key, definition): 
    s = ""
    s += f"# -*- mode: snippet -*-\n"
    s += f"# name: {name}\n"
    s += f"# key: {key}\n"
    s += f"# --\n"
    s += f"{definition}"
    return s

def main():
    file_url = "https://raw.githubusercontent.com/leanprover/vscode-lean/master/src/abbreviation/abbreviations.json"
    snippets_dir = os.path.expanduser("~/.emacs.d/private/snippets/org-mode/")
    file_prefix = "lean_symbols_autogen_393939"
    
    if False:
        snippets_dir = "/tmp/pytest"
        if not os.path.isdir(snippets_dir):
            os.mkdir(snippets_dir)

    path, _ = request.urlretrieve(file_url)

    with open(path, 'r') as f:
        data = json.load(f)

    os.remove(path)

    for i,(key, definition) in enumerate(data.items()):
            contents = []
            contents.append(template(key, f"\{key}", definition))
            contents.append(template(key, f"~\{key}", definition))
            for j,c in enumerate(contents):
                with open(f"{snippets_dir}/{file_prefix}-{i}-{j}-{definition}", "w") as f:
                        f.write(c)


if __name__ == "__main__":
    main()

