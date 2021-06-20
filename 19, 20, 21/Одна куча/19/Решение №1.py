def f(a, i, name):
    """
    a - количество камней в куче
    i - номер хода
    name - имя ходящего
    """
    # Четвёртый ход нас не интересует
    if i > 2:
        return
    else:
        name = "Ваня" if name == "Петя" else "Петя"
        if a >= 42:
            print(f"Выиграл {name} своим {i - 1} ходом, очков {a}")
        else:
            return f(a + 1, i + 1, name), f(a, i + 1, name), f(2 * a, i + 1, name), f(a, i + 1, name)

for S in range(1, 42):
    print(S)
    f(S, 0, "Петя")


# Ответ: 11