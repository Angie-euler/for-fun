import json
import unittest
'''filename='demo_py.txt'
with open(filename,'a') as file_objiect:
    file_objiect.write("I also love finding meaning in lager dataest.\n")
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.strip()
print(pi_string)
print(len(pi_string))'''
#//**********************************************************************
'''print("Give me two number,and I'll divide them.")
print("Enter 'q' quit.")
while True:
    first_number = input("\nFirst number:")
    if first_number=='q':
        break
    second_number=input("\nSecond number:")
    if second_number=='q':
        break
    try:
        print(int(first_number)/int(second_number))
    except ZeroDivisionError:
        print("you can't divide zero!")
    else:
        print(int(first_number)/int(second_number))
'''
"""FileNotFondError"""
"""def count_words(filename):
#filename='alice.txt'
    try:
        with open(filename,'w') as file_object:
            line="Why are you so serious son"
            file_object.write(line)
        with open(filename) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        msg="Sorry,the file "+filename+" does not exist."
        print(msg)
    else:
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")
filenames=['alice.txt','demo_py.txt','little_women.txt','moby_dick.txt']   
for filename in filenames:
     count_words(filename)"""
"""numbers=[2,3,4,5,6,7,8,9]
filename='numbers.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)
with open(filename) as file_object:
    numbers1=json.load(file_object)
print(numbers1)"""
"""filename='username.json'
try:
    with open(filename) as f_ojb:
        username=json.load(f_ojb)
except:
    username=input("What's your name?")
    with open(filename,'w') as f_ojb:
        json.dump(username,f_ojb)
        print("Well come back "+username+"!\n")
else:
    print("Well come back "+username+"!\n")"""
"""******************************************************************"""
"""filename='username.json'
def get_new_username():
    username=input("What's your name?")
    with open(filename,'w') as f_ojb:
        json.dump(username,f_ojb) 
        print("Well come back "+username+"!\n")
    return username
def get_username():
    try:
        with open(filename) as f_ojb:
            username=json.load(f_ojb)
    except FileNotFoundError:
        return None
    else:
        return username
def greet_user():
    username=get_username()
    if username:
        print("Well come back "+username+"!\n")  
    else:
        username=get_new_username()
        print("Well come back "+username+"!\n") 
greet_user()"""
"""def get_formatted_name(first,last):
    full_name=first+' '+last
    return full_name.title()
print("Enter 'q' at any time quite.")
while True:
    first=input("\nPlease give a first name.")
    if first=='q':
        break
    last=input("\nPlease give a last name.")
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print("\nNeatly formatted name:"+formatted_name+".")
"""
"""class AnonymousSurvey():
    def __init__(self,question):
        self.question=question
        self.responses=[]
    def show_question(self):
        print(self.question)
    def store_responses(self,new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('- '+response)
"""









