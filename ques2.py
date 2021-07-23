'Write a Python program to reverse the order of the items in the array. Sample Output Original array:'
'array([1, 3, 5, 3, 7, 1, 9, 3]) Reverse the order of the items: array(i, [3, 9, 1, 7, 3, 5, 3, 1])'
array=[]
rev=[]
w=int(input("ENTER THE NO. OF ELEMENTS YOU WANT:"))
for i in range(0,w):
    p=input("ENTER THE ELEMENT:")
    array.append(p)
array.reverse()
rev.append(array)
print(rev)