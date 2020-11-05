def paramsimg(typeOflens=1, d=0, F=0):
    print("Рассеивающая - 1, собирающая - 0")
    typeOflens = int(input())
    if typeOflens == 1:
        print("Уменьшеное, мнимое, прямое")
    elif typeOflens == 0:
        d = int(input())
        F = int(input())
        if d < F:
            print("Увеличенное, прямое, мнимое")
        elif F < d < 2*F:
            print("Увеличенное, перевернутое, действительное")
        elif d > 2*F:
            print("Уменьшенное, перевернутое, действительное")
paramsimg()