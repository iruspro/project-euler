target = 999


def sum_divisible_by(divisor):
    last_integer = target // divisor
    return divisor * (last_integer * (last_integer + 1)) / 2


sum = sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)
print(int(sum))