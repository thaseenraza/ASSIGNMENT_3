# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20
# Explanation:
# Summation should like 8+2+3+0+7 = 20
def add():
    lst =[]
    size = int(input("Enter the size in list :"))
    for i in range(size):
        ele = int(input("Enter the values for summation : "))
        lst.append(ele)
    print("The Entered list is :",lst)
    lst2 = sum(lst)
    print("the addition of the entered list is :",lst2)
add()
