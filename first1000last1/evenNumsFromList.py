list1 = [i for i in range (1,11)]

print(list1)

def Delete():
    
    for num in list1:
     if num % 2 == 0:
        print(num, end=" ")
    return
Delete()