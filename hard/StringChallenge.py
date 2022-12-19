def string_challenge(str_param):
  result = ""
  
  for i in str_param:
    if i.isalpha():
      result += str(ord(i.lower()) - 96)
    else:
      result += i
      

  return result

print(string_challenge(input()))
