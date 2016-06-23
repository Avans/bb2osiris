#!/usr/bin/env python

from __future__ import print_function
import csv, argparse, os, sys, math

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def error(text):
    print(text, file=sys.stderr)
    quit(-1)

parser = argparse.ArgumentParser(description="Convert a .csv downloaded from the BlackBoard Grade Center output into a format that can be imported into Osiris", usage="""
1. Go to Grade Center and click on Work Offline -> Download
2. Choose the 'Selected Column' option and choose which column contains the grades to be imported into Osiris
3. Choose the 'Comma' Delimiter Type
4. Click 'Submit' to download a .csv output of gradecenter
5. Run this script on the .csv file, for example: `./bb2osiris.py bbinput.csv`
6. An Osiris readable file will be printed on standard output

To save the output to a file you can redirect standard output:
./bb2osiris.py bbinput.csv > osiris.txt
 """)
parser.add_argument('file', help="a .csv input file", type=lambda x: is_valid_file(parser, x))

args = parser.parse_args()

with open(args.file, 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Analyse header
    header = csvreader.next()
    if len(header) <= 5:
        error("Invalid .csv file, not enough columns")

    try:
        studentnumber_column = header.index('Student ID')
    except:
        error("Column 'Student ID' not in header")

    grade_columns = [x for x in header if '|' in x]
    if len(grade_columns) <> 1:
        error(".csv file should contain exactly 1 grade column, please redownload the .csv from BlackBoard with the 'Selected Column' option enabled")

    grade_column = header.index(grade_columns[0])

    # Print all the grades
    for row in csvreader:
        if row[grade_column] == 'Needs Grading' or row[grade_column] == '':
            pass
        else:
            print(row[studentnumber_column] + "\t" + str(math.ceil(float(row[grade_column])*10)/10))


