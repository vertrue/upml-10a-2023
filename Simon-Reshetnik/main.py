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
    print("v1: {}".format(funcs.v1(n, a)))
    print("v2: {}".format(funcs.v2(n, a)))
    print("v3: {}".format(funcs.v3(n, a)))
    print("v4: {}".format(funcs.v4(n, a)))
    print("v5: {}".format(funcs.v5(n, a)))
    print("v6: {}".format(funcs.v6(n, a)))
    print("v7: {}".format(funcs.v7(n, a)))
    print("v8: {}".format(funcs.v8(n, a)))
    print("v9: {}".format(funcs.v9(n, a)))
    print("v10: {}".format(funcs.v10(n, a)))
    print("v11: {}".format(funcs.v11(n, a)))
    print("v12: {}".format(funcs.v12(n, a)))

if __name__ == "__main__":
    main()
