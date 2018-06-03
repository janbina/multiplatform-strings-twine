from pathlib import Path
import subprocess
import re

twineFile = "./strings.txt"
wtiFilePrefix = "strings_" # prefix of files pushed to wti
wtiFilePrefixLen = len(wtiFilePrefix)

# consume all downloaded files to our twine file
for p in Path(".").glob(wtiFilePrefix + "*.xml"):
    lang = p.name[wtiFilePrefixLen:wtiFilePrefixLen+2]
    subprocess.call([
        "twine", 
        "consume-localization-file", 
        twineFile, 
        p.name, 
        "--lang", lang,
        "--format", "android"
    ])

# delete downloaded files
for p in Path(".").glob(wtiFilePrefix + "*.xml"):
        p.unlink()
