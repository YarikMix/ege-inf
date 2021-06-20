def f(a, b, i, name):
    """
    a - количество камней в первой куче
    b - количество камней во второй куче
    i - номер хода
    name - имя ходящего
    """
    # Четвёртый ход нас не интересует
    if i > 2:
        return
    else:
        name = "Ваня" if name == "Петя" else "Петя"
        if a + b >= 77:
            print(f"Выиграл {name} своим {i - 1} ходом, очков {a + b}")
        else:
            return f(a + 1, b, i + 1, name), f(a, b + 1, i + 1, name), f(2 * a, b, i + 1, name), f(a, 2 * b, i + 1, name)

for S in range(1, 70):
    print(S)
    f(7, S, 0, "Петя")


# Ответ: 18