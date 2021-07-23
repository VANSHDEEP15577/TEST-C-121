array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
array1=[]
we=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for j in range(0,we):
    pe=input("ENTER THE ELEMENT:")
    array1.append(pe)
print(array1)
array.extend(array1)
array2=[]
wea=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for k in range(0,wea):
    pea=input("ENTER THE ELEMENT:")
    array2.append(pea)
print(array2)
array.extend(array2)
print(array)