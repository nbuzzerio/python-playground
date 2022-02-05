# if divisible by 3 return Fizz
# if divisible by 5 return Buzz
# if divisible by 3 and 5 return FizzBuzz
# else return the number

def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    else:
        return input

print(fizz_buzz(15))
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(7))