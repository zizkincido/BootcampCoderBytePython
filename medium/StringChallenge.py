def string_challenge(str):
    result = []
    str = float(str)
    for i in range(5):
        if(str < 0.25):
            result.append("empty")
        elif(str >= 0.25 and str < 1):
            result.append("half")
            str = int(str)
        elif(str >= 1):
            result.append("full")
            str -= 1
    return ", ".join(result)

print(string_challenge(input()))

