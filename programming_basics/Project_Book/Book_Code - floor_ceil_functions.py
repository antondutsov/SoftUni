def floor(num):
    if num >= 0:
        return int(num)
    else:
        if int(num) == num:
            return int(num)
        else:
            return int(num) - 1
 
 
def ceil(num):
    if num >= 0:
        if int(num) == num:
            return int(num)
        else:
            return int(num) + 1
    else:
        return int(num)