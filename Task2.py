nomer = input("Число: ")
summa = 0
i = 1
nomer = int(nomer)
while i <= nomer:
    if i % 2 != 0:
        summa = i + summa
    i += 1
print(summa)