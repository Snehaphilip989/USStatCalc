def mode(number):
    if number == []:
        return None
    else:
        return max(number, key=number.count) # checks what the maximum number is , count how many times the maximum number occurs