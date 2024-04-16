person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'Angular','Fortran'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if person.get('skills') is not None:
    list_of_skills = person['skills']
    pos_mid_skill = (len(list_of_skills)//2) 
    mid_skill = list_of_skills[pos_mid_skill]
    print(f"The middle skill is {mid_skill}")
else:
    print("There is no key called skills")

'''
set1 = ['september', 'october', 'november']
set2 = ['december', 'january', 'february']
set3 = ['march', 'april', 'may']
set4 = ['june', 'july', 'august']

month = (input("Enter the name of the month ")).lower()

if month in set1:
    print('The season is Autumn')
elif month in set2:
    print('The season is winter')
elif month in set3:
    print('The season is Spring')
elif month in set4:
    print('Summer')
else:
    print('your season cant be determined')

month = (input("Enter the name of the month ")).lower()
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

elements={"hydrogen":1, "helium":2, "carbon":6}
elements={"hydrogen":1, "helium":2, "carbon":6}
print(elements.keys())
print(elements.values())
'''