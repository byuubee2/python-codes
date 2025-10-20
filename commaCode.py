spam = ['apples', 'bananas', 'tofu', 'cats']
a = []
b = ['choco']
c = ['choco', 'banana']

def commaCode(list):
    if len(list) == 0:
        print('There are no items in this list')
    if len(list) == 1:
        print(list[0])
    if len(list) == 2:
        print(list[0] + ', and ' + list[1])
    if len(list) > 2:
        for i in range(len(list)-1):
            newList = list[i] + ', '
            print(newList, end='')
        print('and ' + list[-1])



commaCode(spam)
commaCode(a)
commaCode(b)
commaCode(c)
