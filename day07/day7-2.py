from statistics import mean
from math import floor

with open("day7.txt", "r") as file:
    numbers = tuple([int(number) for number in file.readline().strip().split(",")])
    mean = floor(mean(numbers))

    total_fuel = sum( sum( i for i in range(1, abs(number - mean) + 1) ) for number in numbers )
    print(total_fuel)
    