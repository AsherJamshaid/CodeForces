n = int(input())
stones = input()
count = 0
for x in range(len(stones)):
    if x == len(stones) - 1:
        break
    elif stones[x] == stones[x+1]:
        count = count + 1
    else:
        continue
print(count)