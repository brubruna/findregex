# findregex.py

The script searches one or more named input files for lines containing a match to a regular expression pattern.
If a line matches, it is print alongside the file name and the line number for every match.

## Getting Started

### Requirements

* python version: 3.6


## Using the script

### Usage:

```
findregex.py [-h] [-u | -c | -m] [infile [infile ...]] regex
```

### Positional arguments:

* ```infile``` - the name of the file(s) to search.
* ```regex``` - the regular expression.

### Optional arguments:
* ```-h, --help ``` -  show help message and exit
* ```-u, --underscore``` - prints "^" under the matching text.
* ```-c, --color``` - highlights matching text.
* ```-m, --machine``` - generates machine readable output. Format: <b>file_name:no_line:start_pos:matched_text</b>


## Example

```first.txt second.txt [a-z][A-Z]{3}[a-z][A-Z]{3}[a-z] -c ``` - Searches for the regular expression in the lines of the <b>first.txt</b> and <b>second.txt</b> files. The output will be the matching text highlighted.

## Author
Bruna Bonguardo

<b>Date:</b>
Jul-08-2018

Built with PyCharm
