# Managing strings for multiple platforms

This repository serves as an example for this blog post: https://medium.com/@janbina/managing-strings-for-multiple-platforms-eea3003d367c.
It shows how we manage strings for multiple platforms.
We are using [twine](https://github.com/scelis/twine) - all our string are in a single twine file 
(`strings/strings.txt` in this repository), and twine generates platform-specific string files from it.

There is a scripts for generating android string files (`generateAndroidStrings.py`). Generated android files
are in `app/src/main/res/values`.

We are using [webtranslateit.com](https://webtranslateit.com) to manage our translations 
and [github.com/AtelierConvivialite/webtranslateit](https://github.com/AtelierConvivialite/webtranslateit)
to sync them with our twine file from command line. There is config file for this library, as well as some helper scripts needed to
upload/download files from webtranslateit, in `strings` directory.

## Workflow

Complete workflow then looks like this:
1. Add new strings to twine file
2. Upload strings to WebTranslateIt (`wti push`).
Generate platform specific string files (`python generateAndroidStrings.py`)
3. Download translated string from WebTranslateIt (`wti pull`)
4. Generate platform specific string files (`python generateAndroidStrings.py`)
