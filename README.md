# AsianLangFileNameTranslator
Translates mp3 file names (within a given directory and it's sub directories) written in Japanese, mandarin, Cantonese, Korean (and a few other languages) text to English. It's pretty cave-man ish - It'll properly organise it later.
I plan to use it to translate the filenames of all the Japanese CD/Radio Drama and music files I have.

Accomplishments:
------
- Script has basic functionality - it: 
  - Translates text to English
    - Does not translate if already english
    - Translates to Japanese (instead of auto dectected language) if hiragana and katakana is found
  - Logs
    - Translations in parent dir (and in target dir when the script successfully finishes)
    - The state of program before ending due to and error
  - Formats translations
    - Removes leading text in lenticular brackets
    - Caps renamed text to 250 characters max to avoid renaming errors
    - Gets ride of specail characters not allowed in windows names
    - Removes newlines
    - Removes text with lenticular brackets and certain contents (like chinese only characters or the word "Drama") if there is a type error on the API side where the translation is too big to send back
    - Makes the translated's words all begin with a capital and proceed with lowercase letters
  - Renames untranslated file names to translated file names
  - Handles Some Errors
    - Handles 429 HTTPs error when too many requests were sent at once by putting the program to sleep for a while and resuming and then logging state of program if that fails after
    - TypeError when the translation is too big to send back from the API, thus causing a type error (handling mentioned above), and logs the state of the program is that fails
- Organised code
  - The Repo was somewhat organised into folders
  - Restructured code into functions and reduced repetition in code
  - Got rid of redundant code

- Fixed errors
  - Errors with code resuming post fail
  - Errors with renaming when translations have specail characters
  - Errors with logging format
  - Errors with anti-duplication functionality
- Tested code in edge cases

- Researched
  - The UTF space of CJK characters
  - Quirks of Asian characters
  - Google Trans API functionality
  - Adding threading to the program
  - Regex library
  - Disabling traceback
  - Advanced exception handling
  - Making dynamic progress bar

Plans:
------
- Clean up code:
  - Make the script a PY file instead of an IPYBN file
  - Make datatype/class that stores chunks items, items index, file directory, filename, trasnlation, source langauge and destination langauge
  - Put part of the code in classes reduce repetitions
  - Organise repo into folders and name appropriately
  
- Add functionality:
  - Make sure the program only handles MP3 files, and determines it's MP3 but looking at meta data and not just the .mp3 portion
    - Maybe make the program handle any file regardless
  - Make it so that chunks only hold a certain number of lines of text to translate (assume each line is at most the windows 10 file naming limit)
    - Make sure that each line in the translated chunk is limited to the number of max chars a windows file name can be
  - Make a function that sees how much of a langauge is in the text to determine the source language - the google lang detect library isn't too good with detection
    - Looks for a better libary instead of making own version
    - If title has multiple langage, break it down and translate it seperately
  - Make program use meta data to translate/select source language more accurate
    - Look at the site it was downloaded from - if it's from bili bili, it's most likely written in chinese
    - Maybe translate meta data too
    - See what useful info is in the meta data
  - Make/Finish a version of the script that
    - Translates in chunks
    - Translates per file name
      - Translate only foreign part of text instead of whole line
    - Translates with chunks with a type of chunk per langauge
      - See if chunks and indexes are being paired and ordered properly once they are rebuilt into a single string/list post translation 
    - Translates chunks into Japanese only - except when it's english
    - Translates chunks in a pipeline of translator function calls (E.g. Translate all the Japanese, all to Chinese, then all too korean)
    - Translates Japanese into Romaji
  - Make the program make copy of files instead of renaming them
    - Put translated file copies in a new directory
    - Put translated file copies in the current directory but with a suffix and prefix to distinquise it
  - Make the program put files from the same track, series or group into their own folder
  - Make program optionally show a breakdown of what langauge files were classified as and how many files were translated and had their name cropped
  - Make program only run in certain directories in a file with a certain name to prevent it running on important files
  - Make program run itself again if 429 error - this has be done, but it doesn't work, figure out how to make it run as if play has been pressed again
  - Make program get rid of all leftover CJK characters post translation
  - Allow Users to add suffixes and prefixes to resulting files
  - Allow Users to remove part of file name that is unwanted (E.G. artist or channel name)
  - Allow user to undo-renaming
  - Create GUI
    - Add progress bar
    - Display file list and metadata
    - Allow users to use the windows file selector to select files, directories and destinations
  - Add multuthreading so trssnalted names can be applied while translation continues
  - Deal with case where file that was going to be renamed no longer exists

- Check/Research
  - Check if translating chunks to Japanese is the same as translating each line to Japanese
  - Find out the Google trans API limit and account for it
  - Look for a way to have the required libraries/APIs installed if they aren't installed on the PC the program runs on
  - Look for OS library functions that does windows file system checks before proceeding
    - See if you can make code get ride of specail chracters from file names
      - Or use asian special characters that are allowed in files names as a substitute
    - See if you can make code check if a directory exists before renaming
  - Look for more accurate langauge detector
  - Look at other translator APIs
