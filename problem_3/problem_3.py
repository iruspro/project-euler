from math import sqrt

factor = 2
last_factor = 1
target = 600851475143

if target % 2 == 0:
    last_factor = 2
    while target % 2 == 0:
        target //= 2

max_factor = sqrt(target)
factor = 3
while target > 1 and factor <= max_factor:
    if target % factor == 0:
        target //= factor
        last_factor = factor
        while target % factor == 0:
            target //= factor
        max_factor = sqrt(target)
    factor += 2

if target == 1:
    print(last_factor)
else:
    print(target)