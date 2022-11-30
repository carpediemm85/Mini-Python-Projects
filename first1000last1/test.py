a = [i for i in range (1,11)]

print(a)

def Delete():
    x=0
    while True:
        del a[x]
        x += 1
        print(a)
    return

Delete()