'''
Question 1: Rendering HTML from a List of Data

Suppose you have a list of dictionaries, where each dictionary represents a person's data with keys 'name' and 'age'. Write a Python program that generates an HTML table displaying this data.

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

html = "<table>\n"
html += "<tr><th>Name</th><th>Age</th></tr>\n"
for person in people:
    html += f"<tr><td>{person['name']}</td><td>{person['age']}</td></tr>\n"
html += "</table>"

print(html)

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

html = "<select>\n"
for city in cities:
    html += f"<option value='{city.lower()}'>{city}</option>\n"
html += "</select>"

print(html)

article_titles = ['Introduction to Python', 'Advanced Data Structures', 'Web Development with Flask']

html = "<ul>\n"
for title in article_titles:
    html += f"<li><a href='/articles/{title.replace(' ', '-').lower()}'>{title}</a></li>\n"
html += "</ul>"
print(html)

a = 2
print(f"{a:02d}")


def check_season(month):
    if month == 'september' or month == 'october' or month == 'november' :
        print('The season is Autumn')
    elif month == 'december' or month == 'january' or month == 'february':
        print('The season is winter')
    elif month == 'march' or month == 'april' or month == 'may':
        print('The season is Spring')
    elif month == 'june' or month == 'july' or month == 'august':
        print('Summer')
    else:
        print('unrecognized season')

check_season("may")


def remove_item(lst,item):
    #x = lst.index(item)
    #del lst[x]
    
    lst.remove(item)
    nwlist = lst
    print(nwlist)

numbers = [2, 3, 7, 9];
remove_item(numbers, 3)


dict_items = {"name": "gbenga", "age": 12, "address":"ikota"}
try:
    print(dict_items["phone"])
except:
    print("there is no key like phone in the dictionary")

print("program running continues")


try:
    num = int(input("Enter a number"))
    print(num)
except:
    print("Only number is acceptable")


def readable_timedelta(num_days):
    num_weeks = int(num_days) // 7
    remain_days = int(num_days) % 7
    print(f"{num_weeks} week(s) and {remain_days} day(s)")

readable_timedelta(3.0)

elements={"hydrogen":1, "helium":2, "carbon":6}
list_1 = []

for key, value in elements.items():
    list_1.append((key,value))

print(list_1)
'''
print("{:.5}".format(10./3))