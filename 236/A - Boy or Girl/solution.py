import sys
input = sys.stdin.readline
 
s = input()
new = set(s)
length = len(new)
if length % 2 == 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")