def f(a, b, i, name):
    if i > 4:
        pass
    else:
        name = "Ваня" if name == "Петя" else "Петя"
        if 4 * a + b >= 77 and a + 4 * b >= 77:
            return f(a + 1, b, i + 1, name), f(a, b + 1, i + 1, name)
        elif 4 * a + b >= 77:
            return f(a + 1, b, i + 1, name), f(a, b + 1, i + 1, name), f(a, 2 * b, i + 1, name)
        elif a + 4 * b >= 77:
            return f(a + 1, b, i + 1, name), f(a, b + 1, i + 1, name), f(2 * a, b, i + 1, name)
        else:
            return f(a + 1, b, i + 1, name), f(a, b + 1, i + 1, name), f(2 * a, b, i + 1, name), f(a, 2 * b, i + 1, name)

for j in range(1, 69+1):
    print(j)
    f(7, j, 1, "Петя")