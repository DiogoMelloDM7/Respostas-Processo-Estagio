def confereFibonnaci(number):
    if number == 0:
        print(f"O número {number} pertence a sequência")
        return
    a = 0
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        if a > number:
            print(f"O número {number} não pertence a sequência")
            break
        elif number == a:
            print(f"O número {number} pertence a sequência")
            break


confereFibonnaci(0)


def inverteString(frase):
    fraseInvertida = ''
    for i in range(len(frase) - 1, -1, -1):
        fraseInvertida += frase[i]
    return fraseInvertida

print(inverteString("Diogo"))



    






