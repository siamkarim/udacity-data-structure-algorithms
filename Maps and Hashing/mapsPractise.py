"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

locations = {'North America': {'USA': ['Mountain View', 'Atlanta']},
              'Asia': {'India': ['Bangalore'], 'China': ['Shanghai']},
              'Africa': {'Egypt': ['Cairo']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""
print (1)
print (locations['North America']['USA'][1])
print (locations['North America']['USA'][0])

string1 = str(locations['Asia']['India'][0]) + ' - ' + str(list(locations['Asia'].keys())[1])
string2 = str(locations['Asia']['China'][0]) + ' - ' + str(list(locations['Asia'].keys())[0])
print (2)
print (string1)
print (string2)
# print (locations['Asia'].keys())