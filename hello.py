phrase = "python For everyone"
phrase1 = phrase.split(' ')  
phrase2 = []
phrase2.append((phrase1[0][0]).upper()) 
phrase2.append(phrase1[1][0].upper())
phrase2.append(phrase1[2][0].upper())

phrase3= ''.join(phrase2)

print(phrase3)
'''
radius = 100
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")
#library = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#print('#'.join(library))
print('#'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

phrase = input("Enter 3 words and get acronymn ")
phrase1 = phrase.split(' ')
s1 = phrase1[0]
s2 = phrase1[1]
s3 = phrase1[2]

s4 = s1[0].upper()
s5 = s2[0].upper()
s6 = s3[0].upper()

acronym = s4+s5+s6
print(acronym)
my_list = [5,4,3,2,1]
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sorted(my_list))

a = 4
b = 3
print('{} / {} = {:.4f}'.format(a, b, a / b))
challenge = 'thirty days of python'
print(challenge.upper()) 
print('Coding For All'.replace("Coding","Python"))
print(14 % 4)
print("good MorNing SIR".title())
print("good MorNing SIR".find('M'))
new_str = "The cow jumped over the man."
print(new_str.split(' ',3))
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[:3:2])
age = int(input("How old are you"))
print(age)
if(age == 18):
    print("you can vote")

print("Hello World!!")
y = """
This is a comment
written in
more than just one line

print(y)
print(0b1011)

print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
#Author : Gbenga
a = 4
A = "Sally"

print(A == a)

#x, y, z = "Orange", "Banana", "Cherry"

x = "Orange"
y = "Banana"
z = "Cherry"

print(x, y, z)

x = 2
y = 2
z = 2

x = y= z = 2

print(0b011)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z, sep=('-'))
'''