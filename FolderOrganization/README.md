# Folder Information Retriever

A simple Python script that retrieves information about a folder and its contents.

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=Python)

## Getting started

1. Clone the repository to your local machine
2. Install the dependencies: `os`, `datetime`, `csv`, and `win32security` libraries
3. Run the script using the following command:

<pre>python folderInfo.py</pre>


## Usage
The script prompts the user to input the path to a folder, then retrieves the following information:
- File name
- File path
- Last modified date
- Created date
- Last accessed date
- Size of file or folder
- Number of folders contained inside the folder
- Directories contained inside the folder
- Files contained inside the folder
- Creator of the file or folder

The information is then stored in a list and displayed to the user.

## Dependencies
- `os` library
- `datetime` library
- `csv` library
- `win32security` library

## Recommendation
We recommend using the `CSV Edit` extension for Visual Studio Code for viewing the generated CSV file.

## License
This project does not have any license.

![License](https://img.shields.io/badge/license-None-green.svg?style=flat-square)
