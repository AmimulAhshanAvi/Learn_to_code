def compute(x, y):
    total = x + y
    if (total > 10):
        total = 10
    return total
 
var1 = compute(2, 3)
print(var1)



def compute1(x, y):
    total = x + y
    if (total > 10):
        total = 10
    return total
        
var2 = compute1(11, 3)
print(var2)


def allow_access(person):
    if person == 'Dr Evil':
        answer = True
    else:
        answer = False
    return answer

var3 = allow_access('Codie')
var4 = allow_access('Dr Evil')
print(var3)
print(var4)



