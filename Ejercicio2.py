def comprobar(lista):
    for i in lista:
        if i < 200 and i%10 == 0:
            print(i)
        if i > 300:
            break
    return lista

def merge_sort(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        merge_sort(izquierda)
        merge_sort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
    return lista


def main():
    lista = [18, 50, 210, 80, 145, 333, 70, 30]
    print(comprobar(lista))
    print(merge_sort(lista))
    indice = lista.index(145) if 145 in lista else -1
    print(indice)
    



if __name__ == "__main__":
    main()