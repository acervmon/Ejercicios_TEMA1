num_inputs = int(input("How many numbers do you want to enter? "))

sum_of_numbers = 0

for _ in range(num_inputs):
    number = float(input("Enter a number: "))
    sum_of_numbers += number
