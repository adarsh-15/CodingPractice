size = int(input("Enter the length of Pyramid: "))
temp = size
while size > 0:
    num = temp-(size-1)
    while num > 0:
        print("\U0001F600", end=" ")
        num -= 1
    print()
    size -= 1
