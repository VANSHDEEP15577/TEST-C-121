' you will ask the user to insert an element at a position given by user'
array=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
print(array)
ins=input("THE YOU WANT TO INSERT:")
pos=int(input("ENTER THE POSITION:"))
array.insert(pos-1,ins)
print(array)
