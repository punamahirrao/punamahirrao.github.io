a=40
b=30
c=50
print(a<b)
if(a>b):
    print("a is smaller than b")
elif(a==b):
    print("a and b are equal")
else:
    print('False')

print('A')if(a>b)else print('B')

if a>b and c>a:
    print('both conditions are true')

print ('')

mylist=['apple','orange','banana','cherry']
print(mylist[1])
mylist.remove('banana')
print(mylist)
mylist.append('pear')
print(mylist)
mylist[1]='straberry'
print(mylist)
for x in mylist:
    print(x)