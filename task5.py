def stul(gruppa_a, gruppa_b, gruppa_c):
    stul_a = gruppa_a / 2
    stul_b = gruppa_b / 2
    stul_c = gruppa_c / 2
    res_a = round(stul_a)
    res_b = round(stul_b)
    res_c = round(stul_c)
    print(f"Для первой группы нужен {res_a} стуля")
    print(f"Для второй группы нужен {res_b} стуля")
    print(f"Для третой группы нужен {res_c} стуля")
    res = res_a + res_b + res_c
    print(f"Вам нужен {res} стуля")

stul(31, 43, 50)