a=500
#print(a)
b=100
#print(b)
#sum=a+b
#print('sum of ' + str(a) + '+' + str(b) + '=' + str(a+b))

d=30
print(d)
def someFunction():
    global d
    print (d)
    d = 'learning python'
someFunction()
print(d)

c=5
print(c)
del c
#print (c)

print('multi of ' + str(a)+'*'+str(b)+'='+str(a*b))
