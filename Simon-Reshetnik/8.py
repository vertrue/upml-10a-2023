def main():
    # Розмір масиву
    n = int(input("Введіть розмір масиву: "))

    # Створення масиву
    a = [int(input(f"Введіть елемент списку №{i + 1}: ")) for i in range(n)]
    # for i in range(n):
    #     a.append(int(input(f"Введіть елемент списку №{i + 1}: ")))

    # Сума елементів, які менші за 5
    summa = sum([x for x in a if x < 5])
    # summa = int()
    # for x in a:
    #     if x < 5:
    #         summa += x

    # Виведення
    print(summa)

if __name__ == "__main__":
    main()
