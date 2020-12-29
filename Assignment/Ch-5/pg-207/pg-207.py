greeting = 'Greetings'
def greet(name, message):
    global greeting
    print(greeting + ' '+ name + '.' + message)

greet('June ', 'See you again my friend!')
print(greeting)
