_ = input()
numbers = list(map(int, input().strip().split()))

locations = {}

for i in range(len(numbers)):
    if numbers[i] in locations:
        locations[numbers[i]] += [i]
    else:
        locations[numbers[i]] = [i]

mins = []

for number in locations:
    if len(locations[number]) == 1:
        pass
    else:
        locations[number].sort()
        mins += [min([locations[number][i + 1] - locations[number][i] for i in range(len(locations[number]) - 1)])]

print(min(mins) if len(mins) > 0 else -1)