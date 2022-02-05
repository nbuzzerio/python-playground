# Must enable mypy linter for intelescence
age: int = 1
# age = 'hello' will trigger linter

# Typing Functions
def square(a: int, b: int = 2) -> int:
    square = a ** b
    return square
print(square(10))