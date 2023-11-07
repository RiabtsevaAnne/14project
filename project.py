def suma(n):
    if n <= 0:
        return 0
    else:
        return n + suma(n - 1)

N = int(input("Введіть кількість перших натуральних чисел (N): "))

if N < 1:
    print("N має бути більше або дорівнювати 1.")
else:
    result = suma(N)
    print(f"Сума перших {N} натуральних чисел дорівнює {result}.")
