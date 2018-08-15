Generates 4 output.csv files.  

**Phone numbers in the first two files are formatted as 10 digits with no special characters.  

**Phone numbers in the second two files are formatted randomly such as having dashes, parenthesis around area codes, having extentions added to the end, +{country code} attached to the front, or just remaining basic such as in the first two files.

**The fourth file does not have the 'Company' column.

~10% of records in each file are IAV

~33% of middle names in the 3rd and 4th files are blank

~1% of records in the 4th file are blank


To install required python packages
~~~
pip install -r requirements.txt
~~~

To run script to generate 4 output.csv files
~~~
python generate.py
~~~
