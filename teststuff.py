def calc(num):
    if (num % 30) != 0:
        return (num // 30) +1
    else:
        return num // 30
    
print(calc(60))