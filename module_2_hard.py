import random
def number():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    num = random.choice(numbers)
    return num
num = number()
print(num)

list_1 = list(range(1, num))
list_2 = list(range(1, num))
pairs = []
result = ''

for i in list_1:
    for j in list_2:
        lst_1 = i  
        lst_2 = j  
        if lst_1 >= lst_2:
            continue
        else:
            kratno = num % (lst_1 + lst_2)
            if kratno == 0:
                pairs.append([lst_1, lst_2])
                result = result + str(lst_1) + str(lst_2)
print(result)