import math

demo = '   PythoN Tutorial'
# length
print(len(demo))
# slice
print(demo[2:5])
print(demo[5:]) #returns entire string from start
print(demo[:]) #returns entire string

#Text Transform
print(demo.upper())
print(demo.lower())
print(demo.title())

print(demo.strip()) # trim

print(demo.find('yt'))
print(demo.replace('N', 'n'))

print(demo.startswith('P'))

print('Python' in demo)
print('Python' not in demo)




math.floor(3.14)

# Type Conversion
x = input('x: ')
print(int(x))
print(float(x))
print(bool(x))
print(str(x))