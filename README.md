Convert a .csv downloaded from the BlackBoard Grade Center output into a format that can be imported into Osiris

1. Go to Grade Center and click on Work Offline -> Download
2. Choose the 'Selected Column' option and choose which column contains the grades to be imported into Osiris
3. Choose the 'Comma' Delimiter Type
4. Click 'Submit' to download a .csv output of gradecenter
5. Run this script on the .csv file, for example: `./bb2osiris.py bbinput.csv`
6. An Osiris readable file will be printed on standard output

To save the output to a file you can redirect standard output:
`./bb2osiris.py bbinput.csv > osiris.txt`
