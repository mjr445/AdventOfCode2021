from statistics import median
from math import floor

with open("day7.txt", "r") as file:
    numbers = tuple([int(number) for number in file.readline().strip().split(",")])
    median = floor(median(numbers))
    
    total_fuel = sum(abs(number - median) for number in numbers)
    print(total_fuel)
    