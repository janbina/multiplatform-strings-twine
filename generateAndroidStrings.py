import subprocess
import shutil
import os

twineFile = "./strings/strings.txt"
resPath = "./app/src/main/res"
resFileName = "strings.xml" # name of the generated file(s)
devLang = "en"
tags = "android"

# make resPath/values directory if it does not exists
if not os.path.exists(resPath + "/values"):
    os.makedirs(resPath + "/values")

# Generate all localization files
subprocess.call([
    "twine", 
    "generate-all-localization-files", 
    twineFile, 
    resPath, 
    "--create-folders", # create "values-xx" folders for all languages
    "--developer-language", devLang,
    "--format", "android",
    "--include", "translated",
    "--tags", tags,
    "--untagged", # include also untagged entries
    "--file-name", resFileName
])

# Move strings file from "values-devLang" to "values" and delete "values-devLang" dir
devLangValues = resPath + "/values-" + devLang
oldFile = devLangValues + "/" + resFileName
newFile = resPath + "/values/" + resFileName

shutil.move(oldFile, newFile)
shutil.rmtree(devLangValues)
