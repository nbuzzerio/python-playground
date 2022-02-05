var_int = 1000
var_float = 1.999
var_boolean = False
var_multiLine = """
template
literal
"""

first = 'john'
last = 'doe'

var_templateLiteral = f"{first} - {last}"
var_multi, var_variable = 1, 2

# Iteriables
var_string = '1,2,3'
var_list = [1, 2, 3]
var_tuple = (1, 2, 3) # unmutible list

# functions
def doSomething():
    return('some', 'thing')
print(doSomething())

# usign variable arguments
def doSomething2(*tuple):
    total = 0
    for number in tuple:
        total += number
    return total
print(doSomething2(1,2,3,4,5))

# dictionaries
def jsObject(**user):
    print(user)
    print(user['id'], user['name'])
print(jsObject(id=1, name='admin'))
