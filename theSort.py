my_list = []
counter = 0
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    my_list.append(val)
my_list.sort()
counter += 1
print("\nSorted:")
print(my_list)
print(counter, "comparisons")

