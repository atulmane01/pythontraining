'''
Regular expressions are used to perform search-related tasks in Python. 
To work with regular expressions, we have to import a built-in module in Python called ‘re’.


The module defines several functions and constants to work with RegEx. The “re” module is composed of five functions known as:

findall:    It finds all searches for matches and prints resultant in the form of a list.
search:     It works the same as a findall, but the resultant is a matched object if any is found.
split:  The split function splits the string from every matched into two new strings.
sub:    The sub-function works exactly like a replace function in notepad or MS Word. It replaces the original word with a word of our choice.
finditer: The finditer yields an iterator as a resultant with all the objects that match the one we sent it) finditer supports more attributes than any other function defined above. It also provides more details related to the matched object. So,
 most of the examples we are going to see next will contain a finditer function in them.
'''
import re
mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii'''

# findall, search, finditer
patt = re.compile(r'fass')
patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')


#compile() method is used to compile a regular expression pattern provided as a string into a regex pattern objec

# Special Sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

matches = patt.finditer(mystr)

for match in matches:
    print(match)


#Findall in the above string

# match = re.findall('\d+', mystr)
# print(match)


#search the avove
# regex = r"([a-zA-Z]+) (\d+)"
# asd=re.search(regex,mystr)
# print(asd)









