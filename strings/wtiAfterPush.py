from pathlib import Path

wtiFilePrefix = "strings_" # prefix of files pushed to wti

# delete generated files pushed to wti
for p in Path(".").glob(wtiFilePrefix + "*.xml"):
    p.unlink()
