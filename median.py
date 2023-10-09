"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
list = [1,2,12,7,6,3]
list.sort()
if (len(list) % 2 == 1):
    median = list[len(list) // 2]
else:
    middle1 = list[len(list) - 1 // 2]
    middle2 = list[len(list) + 1 //2]
    median = (middle1 + middle2) / 2
print(median)
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
