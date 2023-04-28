# Максимальне число
def v1(n, a):
    return max(a)

# Мінімальне число
def v2(n, a):
    return min(a)

# Кількість нулів
def v3(n, a):
    ansv = 0

    for i in a:
        if i == 0:
            ansv += 1

    return ansv

# Сума непарних
def v4(n, a):
    ansv = 0

    for i in a:
        if i % 2 != 0:
            ansv += i

    return ansv

# Сума парних
def v5(n, a):
    ansv = 0

    for i in a:
        if i % 2 == 0:
            ansv += i

    return ansv

# Сума елементів з непарними індексами
def v6(n, a):
    ansv = 0

    for i in range(len(a)):
        if i % 2 != 0:
            ansv += a[i]

    return ansv

# Сума елементів з парними індексами
def v7(n, a):
    ansv = 0

    for i in range(len(a)):
        if i % 2 == 0:
            ansv += a[i]

    return ansv

# Сума елементів, які менші за 5
def v8(n, a):
    summa = sum([x for x in a if x < 5])
    # summa = int()
    # for x in a:
    #     if x < 5:
    #         summa += x

    return summa

# Сума елементів, які менші за 10
def v9(n, a):
    summa = sum([x for x in a if x < 10])

    return summa

# Чи є нуль
def v10(n, a):
    if 0 in a:
        return True
    else:
        return False

# Чи є хоча б 3 нулі
def v11(n, a):
    zeros = 0

    for i in a:
        if i == 0:
            zeros += 1

    if zeros >= 3:
        return True
    else:
        return False

# Чи нема нулів
def v12(n, a):
    if 0 not in a:
        return True
    else:
        return False
