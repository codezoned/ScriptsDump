
def armstrongnumber(num):
    Sum = 0
    temp = num
    while (temp > 0):
        digit = temp % 10

        Sum += digit ** 3
        temp //= 10

    if (num == Sum):
        return True


    else:
       return False




