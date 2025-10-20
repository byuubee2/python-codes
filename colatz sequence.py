def collatz(number):
    if number % 2 == 0:
        yourNumber = number // 2
    else:
        yourNumber = 3 * number + 1
    print(yourNumber)
    return yourNumber

print('enter a number:')
number = int(input())
while True:
    number = collatz(number)
    if number == 1:
        break
