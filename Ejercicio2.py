def comprobar(lista):
    for i in lista:
        if i < 200 and i%10 == 0:
            print(i)
        if i > 300:
            break
    return lista

def main():
    lista = [18, 50, 210, 80, 145, 333, 70, 30]
    print(comprobar(lista))


if __name__ == "__main__":
    main()