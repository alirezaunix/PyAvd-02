
def f1():
    global x
    x=12
    
def f2():
    global x
    x=x+6

x=0    
f1()
f2()
print(x)