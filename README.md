# asianLangFileNameTranslator
Translates mp3 file names (within a given directory and it's sub directories) written in Japanese, mandarin, Cantonese, Korean (and a few other languages) text to English. It's pretty cave-man ish - It'll properly organise it later.
Accomplishments:
------
- Go it somewhat working

Plans:
------
- Make code a PY file instead of an IPYBN file
- Clean up code
  - Put part of the code in functions and classes reduce repetitions
  - Organise repo int folders and name appropriately
  - Make datatype/class that stores chunks items, items index, file directory, filename, trasnlation, source langauge and destination langauge
- Attempt to use meta data to translate/select source language more accurate
  - Look at the site it was downloaded from - if it's from bili bili, it's most likely written in chinese
  - Maybe translate meta data too
  - See what useful info is in the meta data
- Make a function that sees how much of a langauge is in the text to determine the source language - the google lang detect library isn't too good with detection
  - Looks for a better libary instead of making own version
  - If title has multiple langage, break it down and translate it seperately
- Make sure the program only handles MP3 files, and determines it's MP3 but looking at meta data and not just the .mp3 portion
  - Maybe make the program handle any file regardless
- Allow chunks to only hold a certain number of lines of text to translate (assume each line is at most the windows 10 file naming limit)
  - Make sure that each line in the translated chunk is limited to the number of max chars a windows file name can be
- Have an option to translate Japanese to Romaji
- Make/Finish version of the script that
  - Translates in chunks
  - Translates per file name
  - Translates with chunks with a type of chunk per langauge
    - See if chunks and indexes are being paired and ordered properly once they are rebuilt into a single string/list post translation 
  - Translates chunks into Japanese only - except when it's english
  - Translates chunks in a pipeline of translator function calls (E.g. Translate all the Japanese, all to Chinese, then all too korean)
- Find a way for PIP to install the required libraries/APIs if they aren't installed on the PC the program runs on
- Check if translating chunks to Japanese is the same as translating each line to Japanese
- Find out the Google trans API limit and account for it
- Check is anti-duplication functionality works properly
- Make code check if a directory exists before renaming
- Look for OS library functions that does windows file system checks before proceeding
  - Make code get ride of specail chracters from file names
    - Or use asian special characters that are allowed in files names as a substitute
- Save the old names of files and allow user to undo-renaming (by having a mapping of the new and old names) 
- Show breakdown of what langauge files were classified as
- Add progress bar
- Give GUI
- Translate only foreign part of text instead of whole line
- Look for more accurate langauge detector
- Look at other translator APIs
- Make the program make copy of files instead of renaming them
  - Put in new directory
  - Put in current directory but with a suffix and prefix to distinquise it
- Allow users to add suffixes and prefixes to resulting files
- Make the program put files from the same track, series or group into their own folder
- 
