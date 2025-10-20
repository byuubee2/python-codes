spam = {'dog': 'choco', 'nickname': 'chocomani','color': 'brown'}
print(spam.keys())
for k in spam.keys():
    print(k)
for i in spam.items():
    print(list(i))
for k, v in spam.items():
    print('key: ' + k + ' value: ' + v)

print('I am bringing ' + str(spam.get('dog', 'milo')) + ' to the park.')
spam.setdefault('color', 'black')
print(spam)
