string = input()
 
lower_count = 0
upper_count = 0
 
for x in range(len(string)):
    if string[x].islower():
        lower_count+=1
    elif string[x].isupper():
        upper_count+=1
 
if upper_count > lower_count:
    print(string.upper())
elif upper_count<lower_count:
    print(string.lower())
else:
    print(string.lower())