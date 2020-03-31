l=[1,2,0,0,4,1,6,2,1,3]
Total_Score=0
for i in l:
	Total_Score=Total_Score+i
print("Total Score:",Total_Score)

a=l[0]
b=l[-1]
c=a+b
print("Batsman 1 Score:{0} ({1}+{2})".format(c,a,b))
d=l[1:-1]
e=0
for i in d:
	e=e+i
f=l[1]
g=l[4]
h=l[5]
i=l[6]
j=l[7]
k=l[8]
print("Batsman 2 Score:{0} ({1}+{2}+{3}+{4}+{5}+{6})".format(e,f,g,h,i,j,k))