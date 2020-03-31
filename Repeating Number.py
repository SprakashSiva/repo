#1.method
l=[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
print('Befor Sorting of list :',l)
m=l.copy()
m.sort()
#removing duplicates
n=set(m)
#convert into list
o=list(n)
#print(o)
l.sort()
#creating new empty list
b=[]
for i in o:
        a=l.count(i)
        b.append(a)

print('After Sorting of list :',l)
print("Repeating of 0 is :",b[0])
print("Repeating of 1 is :",b[1])
print("Repeating of 2 is :",b[2])
print("Repeating of 3 is :",b[3])
print("Repeating of 4 is :",b[4])
print("Repeating of 5 is :",b[5])
print("Repeating of 6 is :",b[6])
print("Repeating of 7 is :",b[7])
print("Repeating of 8 is :",b[8])
print("Repeating of 9 is :",b[9])
print("Repeating of 12 is :",b[10])

#2.method
from collections import Counter
l=[1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
n=str(l)
# m=Counter(l)
print(Counter(l))
