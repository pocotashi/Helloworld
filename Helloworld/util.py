def find_max(numbers):
    maxi = numbers[0]
    for numbers in numbers:
        if numbers > maxi:
            maxi = numbers
    return maxi
