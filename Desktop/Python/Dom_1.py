list = [2, 3, 5, 9, 3]
summ = 0
for i in range(1, len(list),2):
    if i%2 ==1:
        summ +=list[i]
print(f"{list} Сумма на ненечетных позициях: {summ}")