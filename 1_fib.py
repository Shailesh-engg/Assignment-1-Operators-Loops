n = int(input("enter a number: "))
first = 0 
second = 1 
for i in range(n):
    print(first)
    res = first 
    first = second
    second = res + second
