#1.without using buitins fuunctions
d={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
m=d.values()
j=0
for i in m:
	j=j+i
print(j)


# 2.using buitins function
def sumof(d):
    m=d.values()
    n=sum(m)
    return n
d={"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
print(sumof(d))
