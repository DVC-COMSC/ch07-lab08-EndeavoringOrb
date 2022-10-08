values = list(map(int, input().split()))
values.insert(0,int(input()))
for i in range(len(values)-1):
    if values[i] > values[i+1]:
        values[i],values[i+1] = values[i+1],values[i]
print(values)