a, b = map(int, input().split())  # read n and k from one line
count = 0
weight_a = a
weight_b = b
while weight_a<=weight_b:
    weight_a = weight_a * 3
    weight_b = weight_b * 2
    count = count + 1
 
print(count)