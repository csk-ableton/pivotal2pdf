pivotal2pdf
===========

Create a pdf document from an exported csv of Pivotal Tracker

## Requirements

* Python (tested with 2.7)
* pyfpdf (https://code.google.com/p/pyfpdf/)

## How it works

Select your stories from Pivotal Tracker. Export them to a csv file.
Run the Python script to convert them into a pdf. The stories will be split into chunks
of 4 per page.

`python pivotal2pdf.py yourproject_20140820_1036.csv`
