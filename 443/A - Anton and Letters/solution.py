s = input()
 
content = s.strip("{}").replace(" ", "")
 
if content == "":
    print(0)
else:
    print(len(set(content.split(","))))