import re


text_to_search = """

ABCDEFGHIJKLMNOPQRSTUJVWXYZabcdefghijklmnopqrstuvwxyz
0123456789

{[]}#~@/?><./\|&$£"!^-_=+*()

01737 032 301
0845 900 9900
0207 331 3456
020 8898 1347
07963117521

daniel_919@gmail.com
bistudio@outlook.com

www.google.com
https://msn.com
http://amazon,co.uk

Mrs. J. Smith
Mr. Bob Balaban
Miss. Ladyedee

My very eyes may just see under nine planets

"""

# to search for phone numbers

#
# pattern = re.compile(r'\d{4,5}\s\d{3,4}\s\d{3,4}')
# matches = pattern.findall(text_to_search)
#
# for match in matches:
#     print(match)