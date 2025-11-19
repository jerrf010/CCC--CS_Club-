employee_record = (6767,"Chad Jefferson", 250000, True)

print(employee_record[1:3])

y = list(employee_record)
y[1] = "kiwi"
employee_record = tuple(y)
print(employee_record[1:3])