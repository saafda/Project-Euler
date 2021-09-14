reject = []
num = []
for n in range(200000000, 300000000):
    if n % 20 != 0:
        reject.append(n)
    elif n % 19 != 0:
        reject.append(n)
    elif n % 18 != 0:
        reject.append(n)
    elif n % 17 != 0:
        reject.append(n)
    elif n % 16 != 0:
        reject.append(n)
    elif n % 15 != 0:
        reject.append(n)
    elif n % 14 != 0:
        reject.append(n)
    elif n % 14 != 0:
        reject.append(n)
    elif n % 13 != 0:
        reject.append(n)
    elif n % 12 != 0:
        reject.append(n)
    elif n % 11 != 0:
        reject.append(n)
    else:
        num.append(n)
print(num[0])