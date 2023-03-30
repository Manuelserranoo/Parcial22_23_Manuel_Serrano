import random

# Definimos la función que encripta un caracter
def encriptar_caracter(caracter):
    # Convertimos el caracter en un número decimal
    decimal = ord(caracter)
    
    # Generamos 8 números aleatorios entre 32 y 125
    numeros_aleatorios = [random.randint(32, 125) for i in range(8)]
    
    # Sumamos cada número aleatorio al número decimal del caracter
    numeros_encriptados = [decimal + num for num in numeros_aleatorios]
    
    # Convertimos cada número en un caracter y los concatenamos
    caracteres_encriptados = ''.join([chr(num) for num in numeros_encriptados])
    
    return caracteres_encriptados

# Definimos la función que genera las tablas hash
def generar_tablas():
    tabla_encriptar = {}
    tabla_desencriptar = {}
    
    # Recorremos los caracteres desde " " hasta "}"
    for decimal in range(32, 126):
        # Encriptamos el caracter y lo guardamos en la tabla de encriptación
        caracter_encriptado = encriptar_caracter(chr(decimal))
        tabla_encriptar[chr(decimal)] = caracter_encriptado
        
        # Guardamos la relación inversa en la tabla de desencriptación
        tabla_desencriptar[caracter_encriptado] = chr(decimal)
        
    return tabla_encriptar, tabla_desencriptar

if __name__ == "__main__":
    # Generamos las tablas hash
    tabla_encriptar, tabla_desencriptar = generar_tablas()

    # Pedimos al usuario que ingrese un mensaje a encriptar
    mensaje = input("Ingrese el mensaje a encriptar: ")

    # Encriptamos el mensaje
    mensaje_encriptado = ''.join([tabla_encriptar.get(caracter, caracter) for caracter in mensaje])

    # Imprimimos el mensaje encriptado y las tablas hash
    print("Mensaje encriptado: ", mensaje_encriptado)
    print("Tabla de encriptación: ", tabla_encriptar)
    print("Tabla de desencriptación: ", tabla_desencriptar)
