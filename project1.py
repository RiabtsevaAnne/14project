h = lambda a, b: (a**2 + b**2)**0.5

vp = lambda a, b, h: a * b * h

a = float(input("Введіть довжину першої сторони трикутника (a): "))
b = float(input("Введіть довжину другої сторони трикутника (b): "))

c = h(a, b)
print(f"Гіпотенуза трикутника: {c}")

h_prism = float(input("Введіть висоту призми (h): "))

v = vp(a, b, h_prism)
print(f"Об'єм призми на основі трикутника: {v}")
