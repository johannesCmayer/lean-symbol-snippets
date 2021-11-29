from urllib import request
import json
import os
import glob
import re

def template(key, definition, start, end): 
    key = key.replace("\\", r"\\")
    key = key.replace("\"", r"\"")
    definition = definition.replace("\\", r"\\")
    definition = definition.replace("\"", r"\"")

    s = ""
    s += f'    - trigger: "{start}{key}{end}"\n'
    s += f'      replace: "{definition}"\n'
    return s

def main():
    file_url = "https://raw.githubusercontent.com/leanprover/vscode-lean/master/src/abbreviation/abbreviations.json"
    match_file = os.path.expanduser("~/.config/espanso/match/lean-symbols.yml")
    
    path, _ = request.urlretrieve(file_url)

    with open(path, 'r') as f:
        data = json.load(f)

    os.remove(path)

    with open(match_file, 'w') as f:
        f.write("matches:\n")
        for i,(key, definition) in enumerate(data.items()):
            if i < 30:
                print(key)
            if key == "\\":
                continue
            f.write(template(key, definition, "\\\\", "\\\\"))
            f.write(template(key, definition, "\\\\", " "))
            f.write(template(key, definition, "\\\\", "\t"))

if __name__ == "__main__":
    main()

