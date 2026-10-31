t = int(input())
 
for _ in range(t):
    s = input()
    
    hour = int(s[:2])
    minute = s[3:]
    
    if hour == 0:
        print("12:" + minute + " AM")
    elif 1 <= hour < 12:
        print(s[:2] + ":" + minute + " AM")
    elif hour == 12:
        print("12:" + minute + " PM")
    else:
        new_hour = hour - 12
        print(f"{new_hour:02d}:{minute} PM")