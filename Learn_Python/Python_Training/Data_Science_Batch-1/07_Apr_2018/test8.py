a = 1
def sum(x,y):
    global z
    z = 2
    print z
    return x+y

print sum(5,6)
print z