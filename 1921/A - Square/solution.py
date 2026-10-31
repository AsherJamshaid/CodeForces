t = int(input())
 
for x in range(t):
    x_coords = []
    y_coords = []
    for _ in range(4):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
    
    side = max(x_coords) - min(x_coords) 
    area = side * side
    print(area)