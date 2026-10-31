string = input().lower()
result = ""
final = ""
for x in range(len(string)):
    if string[x] == "a" or string[x] == "e" or string[x] == "i" or string[x] == "o" or string[x] == "u" or string[x] == "y":
        continue
    else:
        result = result + string[x]
 
for x in range(len(result)):
    final = final + "." + result[x]
print(final)