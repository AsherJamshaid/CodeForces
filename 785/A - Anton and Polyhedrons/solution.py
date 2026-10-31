n = int(input())
shape_one = "tetrahedron"
shape_two = "cube"
shape_thr = "octahedron"
shape_fo = "dodecahedron"
shape_five = "icosahedron"
count = 0
for x in range(n):
    strin = input()
    if strin.lower() == shape_one:
        count+=4
    elif strin.lower() == shape_two:
        count+=6
    elif strin.lower() == shape_thr:
        count+=8
    elif strin.lower() == shape_fo:
        count+=12
    elif strin.lower() == shape_five:
        count+=20
print(count)