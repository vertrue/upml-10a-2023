#from funcs import v8
import f as funcs

def main():
    # Розмір масиву
    n = int(input("Введіть розмір масиву: "))

    # Створення масиву
    a = [int(input(f"Введіть елемент списку №{i + 1}: ")) for i in range(n)]
    # for i in range(n):
    #     a.append(int(input(f"Введіть елемент списку №{i + 1}: ")))

    # Виведення
    print("v1: " + funcs.v1(n, a))
    print("v2: " + funcs.v2(n, a))
    print("v3: " + funcs.v3(n, a))
    print("v4: " + funcs.v4(n, a))
    print("v5: " + funcs.v5(n, a))
    print("v6: " + funcs.v6(n, a))
    print("v7: " + funcs.v7(n, a))
    print("v8: " + funcs.v8(n, a))
    print("v9: " + funcs.v9(n, a))
    print("v10: " + funcs.v10(n, a))
    print("v11: " + funcs.v11(n, a))
    print("v12: " + funcs.v12(n, a))

if __name__ == "__main__":
    main()
