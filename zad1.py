def max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

def min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

def avg(numbers):
    return sum(numbers) / len(numbers)

def var(numbers):
    numbersAvg = avg(numbers)
    return sum(map(lambda x: (x - numbersAvg) ** 2, numbers)) / (len(numbers) - 1)

functionsMap = {
    '1': max,
    '2': min,
    '3': avg,
    '4': var
}

data = [int(x) for x in input('Podaj zestaw liczb: ').split()]
index = input('''\
Co chcesz zrobić?
1 - wyświetl maximum
2 - wyświetl minimum
3 - wyświetl średnią
4 - wyświetl wariancję
''')
print(functionsMap[index](data))

#qweqweqwe
