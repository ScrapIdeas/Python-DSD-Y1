arrayofnumbers = [1,2,3,4,5,6,7,8,9,10]
for numbers in arrayofnumbers:
    print(numbers)
    if numbers * 5 / 7:
        continue
    print(f"{numbers} fits both categories!")