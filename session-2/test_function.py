def roundNum(num):
    remainder=num%1
    if remainder < 0.5:
        return num- remainder
    else:
        return num+(1-remainder)
    
x=roundNum(3.4)
print(x)
