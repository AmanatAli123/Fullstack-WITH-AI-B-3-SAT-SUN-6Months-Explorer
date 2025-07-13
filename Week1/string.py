my_string1=int(50)
print(type(my_string1))
string="pakistan"
print(string[3:5])
print(string[6:])
print(len(string))
print(string[::-1])
String="WsCube@#123"
cleaned_string=""
for char in String:
    if char.isalnum():
        cleaned_string +=char
        print(cleaned_string)
print(cleaned_string)        
        # if i write the statement inside the for loop then it will print the each character one by one by 
        # seeking if it has the special chracter or not 
        # what if i write the statement outside the for loop then it only check the full string along it checking the special charater within the string and print it only one time
institute = [2003,"shahid anwar",19.3]
print(type(institute))
print(institute)
for i in institute:
    print(i)
print(institute[0])
print(institute[1])
tuple1=(2003,"linux",1.2)
print(type(tuple1))
print(tuple1)
for t in tuple1:
    print(t)       #we can not use the range funciton in the set
set1={2003,"list",2.3}
print(set1)
for i in set1:
    print(i)
dict1={"a":"Amanatali","b":1243}
print(dict1)
for i in dict1:
    print(dict1["a"])
    print(dict1["b"])