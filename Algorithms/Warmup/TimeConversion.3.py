time = input().strip()
if time[-2:] == "PM":
    h = int(time[:2])
    print(time[:-2] if h == 12 else str((h + 12) % 24) + time[2:-2])
else:
    h = int(time[:2])
    print("00" + time[2:-2] if h == 12 else time[:-2])