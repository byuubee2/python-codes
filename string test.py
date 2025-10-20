name = 'zombie'
print(list(name))
name = name[0:4] + 'boid' + name[3:6]
print(name)
#reference is being copied
#immutable values = new value created and new reference created
spam = 42
cheese = spam
spam = 100
print(cheese)
print(spam)
#mutable values = same reference but stored in a different variable
spam = [1,2,3]
cheese = spam
cheese[1] = 'strawberry'
print(cheese)
print(spam)

piece = 'wking'
print(piece.startswith('w'))
print(piece.endswith('king'))
