class polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes
    def __add__(self, otro):
        if len(self.coeficientes) > len(otro.coeficientes):
            maximo = len(self.coeficientes)
        else:
            maximo = len(otro.coeficientes)
        resultado = []
        for i in range(maximo):
            if i < len(self.coeficientes):
                if i < len(otro.coeficientes):
                    resultado.append(self.coeficientes[i] + otro.coeficientes[i])
                else:
                    resultado.append(self.coeficientes[i])
            else:
                resultado.append(otro.coeficientes[i])
        return polinomio(resultado)
    def __sub__(self, otro):
        if len(self.coeficientes) > len(otro.coeficientes):
            maximo = len(self.coeficientes)
        else:
            maximo = len(otro.coeficientes)
        resultado = []
        for i in range(maximo):
            if i < len(self.coeficientes):
                if i < len(otro.coeficientes):
                    resultado.append(self.coeficientes[i] - otro.coeficientes[i])
                else:
                    resultado.append(self.coeficientes[i])
            else:
                resultado.append(otro.coeficientes[i])
        return polinomio(resultado)
    def __mul__(self, otro):
        resultado = []
        for i in range(len(self.coeficientes)):
            for j in range(len(otro.coeficientes)):
                if i + j < len(resultado):
                    resultado[i + j] += self.coeficientes[i] * otro.coeficientes[j]
                else:
                    resultado.append(self.coeficientes[i] * otro.coeficientes[j])
        return polinomio(resultado)
    #definir una función que elimine un coeficiente convirtiendolo en 0
    def eliminar(self, coeficiente):
        self.coeficientes[coeficiente] = 0
        
        #definir una función que determina si un coeficiente existe
    def __contains__(self, coeficiente):
        return coeficiente in self.coeficientes
    
    def dividir(self, otro):
        resultado = []
        for i in range(len(self.coeficientes)):
            for j in range(len(otro.coeficientes)):
                if i + j < len(resultado):
                    resultado[i + j] += self.coeficientes[i] / otro.coeficientes[j]
                else:
                    resultado.append(self.coeficientes[i] / otro.coeficientes[j])
        return polinomio(resultado)

    def __str__(self):
        resultado = ""
        for i in range(len(self.coeficientes)):
            if self.coeficientes[i] != 0:
                if self.coeficientes[i] > 0:
                    resultado += " + "
                else:
                    resultado += " - "
                if i == 0:
                    resultado += str(abs(self.coeficientes[i]))
                elif i == 1:
                    resultado += str(abs(self.coeficientes[i])) + "x"
                else:
                    resultado += str(abs(self.coeficientes[i])) + "x^" + str(i)
        return resultado
    # añadir las funcion dividir 
    def dividir(self, otro):
        resultado = []
        for i in range(len(self.coeficientes)):
            for j in range(len(otro.coeficientes)):
                if i + j < len(resultado):
                    resultado[i + j] += self.coeficientes[i] / otro.coeficientes[j]
                else:
                    resultado.append(self.coeficientes[i] / otro.coeficientes[j])
        return polinomio(resultado)
    

def main():
    p1 = polinomio([1, 2, 3])
    p2 = polinomio([2, 3, 4])
    p3 = polinomio([1, 2, 3, 4])
    p4 = polinomio([1, 2, 3, 4, 5])
    #llamar a a la función que elimina un coeficiente
    p1.eliminar(1)
    #llamar a la función que determina si un coeficiente existe
    print(2 in p1)
    print(3 in p1)


    


    print(p1 + p2)
    print(p1 - p2)
    print(p1 * p2)
    print(p3 + p4)
    print(p3 - p4)
    print(p3 * p4)
    print(p1.dividir(p2))
    print(p1.dividir(p3))
    print(p1.dividir(p4))
    

if __name__ == "__main__":
    main()