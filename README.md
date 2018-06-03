# Managing strings for multiple platforms

This repository shows how we manage strings for multiple platforms.
We are using [twine](https://github.com/scelis/twine) - all our string are in a single twine file 
(`strings/strings.txt` in this repository), and twine generates platform-specific string files from it.

There are scripts for generating android string files and ios string files [TBA]. Generated android files
are in `app/src/main/res/values` folders, ios files are in [TBA].

We are using [webtranslateit.com](https://webtranslateit.com) to manage our translations 
and [github.com/AtelierConvivialite/webtranslateit](https://github.com/AtelierConvivialite/webtranslateit)
to sync them with our twine file from command line. There is config file for this library, as well as some helper scripts needed to
upload/download files from webtranslateit, in `strings` directory.
