limit = 4000000
sum = 0
first_number = 1
second_number = 1
every_third_number_in_sequence = first_number + second_number
while every_third_number_in_sequence <= limit:
    sum += every_third_number_in_sequence
    first_number = second_number + every_third_number_in_sequence
    second_number = every_third_number_in_sequence + first_number
    every_third_number_in_sequence = first_number + second_number

print(sum)