PyDedupFiles
============

Python and bash utility to find duplicate files. It generates a list of duplicated files and shows a UI to select which ones to keep and which ones to delete

Please see the TODO.txt file for a roadmap

======= Features
- Scans all the files under the specified path looking for binary identical jpg images
- Presents the identical files side to side allowing the user to delete one of the duplicates

======= Known limitations
- The scan needs to run before each visual comparison.
  If the visual comparison is restarted it starts from the beginning but will generate an error when it does not find the already deleted files 
- Currently the comparison only works for jpg files and only comparing the MD5SUM of the files.
  This means that identical jpg files with different EXIF information are not binary identical so they will not show in the comparison

====== How to use
This version consists of two manual steps:

1) Execute findDuplicateImages.sh passing as a paremeter the root path to scan for duplicates redirecting the ouput to a file called "duplicates.txt"

sh ./findDuplicateImages.sh <root path> > duplicates.txt

2) Execute pyDedupFiles.py without parametes (it assumes the "duplicates.txt" file as the input file)

python ./pyDedupFiles.py



