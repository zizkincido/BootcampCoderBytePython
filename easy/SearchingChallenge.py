def searching_challenge(str):
    sum = 0
    i = 0
    while i < len(str):
        if str[i].isdigit():
            num = []
            while i < len(str) and str[i].isdigit():
                num.append(str[i])
                i += 1
            if len(num) > 1:
                temp = int("".join(num))
                sum += temp
        i += 1
    return sum

print(searching_challenge(input()))

