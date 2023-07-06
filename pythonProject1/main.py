print("welcome to the telephone book service\n")
print("To inquire about the owner of a number write number one\n ")
print("To add a new number or modify a previous number write number two\n")
print("To search for a person's number by name write number three\n ")
service = str(input("Enter the number of the service you want"))
name_number = {'1111111111': 'Amal','2222222222':'Mohammed','3333333333':'Khadijah','4444444444':'Abdullah','555555555': 'sara','6666666666':'Faisal','7777777777':'Layla'}
if service == 'one':
    desired_number = input("please write the number in this place")
    for number,name in name_number.items():
        if desired_number == number:
            print("the name of this number " + desired_number + " is " + name_number[desired_number])
            break
        print("Sorry, the number is not found")


elif service == 'two':
    x= input("please write the number in this place")
    y= input("please write the name in this place")
    name_number[x]=y
    print("The number has been added successfully")
elif service == 'three':
    desired_name = input("please write the name in this place")
    for number, name in name_number.items():
        if desired_name == name:
            print("the name of this number " + desired_name + " is " + number)
            break
        print("Sorry, the number is not found")
else:
    print("The entry is incorrect")
