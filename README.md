pivotal2pdf
===========

Create a pdf document from an exported csv of Pivotal Tracker

## Requirements

* Python (tested with 2.7 and 3.4)
* pyfpdf (https://github.com/reingart/pyfpdf)
* Optional: Qt5 and PyQt5

## How it works

Select your stories from Pivotal Tracker. Export them to a csv file.
Run the Python script to convert them into a pdf. The stories will be split into chunks
of 4 per page.

`python pivotal2pdf.py yourproject_20140820_1036.csv`

Or if you like to use a graphical version use

`python pivotal2pdf-gui.py yourproject_20140820_1036.csv`

## Usage

```
pivotal2pdf.py [-h] [-m MARGIN] [-o OUTPUT] [-n] [-t] [-c] csv

positional arguments:
  csv                   the file path to the csv file

optional arguments:
  -h, --help            show this help message and exit
  -m MARGIN, --margin MARGIN
                        margin of the page in mm (default: 5)
  -o OUTPUT, --output OUTPUT
                        file path to the generated pdf (default: None)
  -n, --show-number     shows the story number on the bottom left (default:
                        False)
  -t, --show-tasks      shows the tasks for each story (default: False)
  -c, --collate         collate stories for easier sorting after cutting all
                        pages (default: False)
```
