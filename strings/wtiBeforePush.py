from pathlib import Path
import subprocess
import zipfile

twineFile = "./strings.txt"
zipFileName = "strings.zip"
wtiFilePrefix = "strings_" # prefix of files pushed to wti

# generate zip file with all localizations from twine
subprocess.call([
    "twine", 
    "generate-localization-archive",
    twineFile,
    zipFileName,
    "--format", "android",
    "--include", "translated"
])

# extract the zip file
with zipfile.ZipFile(zipFileName,"r") as zip_ref:
    zip_ref.extractall(".")

# raneme generated file and move them to parent directory
for p in Path("Locales").iterdir():
    p.rename(wtiFilePrefix + p.name)

# remove created garbage
Path("Locales").rmdir()
Path(zipFileName).unlink()
