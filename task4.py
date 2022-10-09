n = int(input("Введите число N: "))
listNums = []

for i in range(1, n + 1):
    if i % 2 == 0:
        listNums.append(i)

print(listNums)        
