array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
array.extend(array)
print(array)