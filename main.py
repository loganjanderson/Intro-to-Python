def fizzbuzz():
    for num in range(1, 101):
        print(num)
        if num % 3 == 0:
            print('fizz')
        if num % 5 ==0:
            print('buzz')
        if num % 3 == 0 and num % 5 == 0:
            print(fizzbuzz)

fizzbuzz()