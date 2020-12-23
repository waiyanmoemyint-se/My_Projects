#Write a python program to create an array of 5 intergers and display the arrays items

import array
array_number = array.array("i",[1,2,3,4])
for i in array_number:
    print(i)
    print("Access the first three items individual is")
    print(array_number[0])
    print(array_number[2])
