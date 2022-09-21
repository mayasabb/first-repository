import ArithmeticProg

beginning_value = int(input("Enter the beginning value of this series: "))
step = int(input("Enter the length of the step: "))
num_of_values = int(input("Enter the number of values in the series: "))

sum_n_values = ArithmeticProg.sum_n_items(beginning_value, step, num_of_values)
print(sum_n_values)

values_in_double_seats = ArithmeticProg.print_n_items((beginning_value + 1), (step*2), (num_of_values/2))
print(values_in_double_seats)