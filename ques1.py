'Write a Python program to create an array of 5 integers and display the array items. Access individual'
' element through indexes.Access first three items individually'
array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
print(array[0])
print(array[1])
print(array[2])