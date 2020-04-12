import re

text_to_search = """

abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

coreyMS@gmail.com
dandy_12@msn.edu
likely-9lad2@yahoo.net
getLost-87@putlook.gov

Mr James Bond
Mr. S Smith
Ms Arcadia Davida
Miss Sara Jay
Mrs. Sammie Sparxxx

01737 032 301
01275 667 778
020 3396 8219
07913 556 391
07932273973
0121 378 4244

124 Drury Lane, Covent Garden , London WC1A 4DG

file_1.ico
text_file.txt

"""

# search for salutation and names

# pattern = re.compile(r'M[r|s|iss|rs]+\.?\s[A-Z]\s?\w+\s?\w')

# search for phone numbers

# pattern = re.compile(r'\d{3,5}\s?\d{3,4}\s?\d{3,4}')

# search for email addresses

# pattern = re.compile(r'([a-zA-z0-9-_]+)@([a-zA-Z0-9]+)\.([a-zA-Z]+)')

# file extention

pattern = re.compile(r'([a-zA-Z0-9_-]+?)\.([a-zA-Z0-9]+)')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
