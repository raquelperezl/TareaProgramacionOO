'''
Abstraccion de 2 objetos cualquiera
'''

# PRIMER OBJETO

class Lavadora():
    def __init__(self, marca, modelo, color, potencia):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
    def __str__(self):
        return "Marca: {}, Modelo: {}, Color: {}, Potencia: {} W".format(self.marca, self.modelo, self.color, self.potencia)
    def encender(self):
        print('Encendido!')
    def apagar(self):
        print('Apagado!')
    def recomendado(self):
        if self.potencia > 2200 or self.potencia < 1500:
            print('No recomendado :(')
        else:
            print('Recomendado :)')
    def opciones(self):
        print('''
        ================ M E N U ================
        1. Empezar lavado
        2. Enjuagar
        3. Centrifugar
        ''')
        opcion = int(input('Ingrese opcion: '))
        if opcion == 1:
            print('Lavando...')
        elif opcion == 2:
            print('Enjuagando...')
        elif opcion == 3:
            print('Centrifugando...')
        else:
            print('Opcion no disponible')

lavadora1 = Lavadora('LG', 'Doble tina', 'Blanco', 1500)
print(lavadora1)
lavadora1.encender()
lavadora1.recomendado()
lavadora1.opciones()
lavadora1.apagar()

# SEGUNDO OBJETO

class Mochila():
    def __init__(self, marca, color, tamaño):
        self.marca = marca
        self.color = color
        self.tamaño = tamaño
    def __str__(self):
        return "Marca: {}, Color: {}, Tamaño: {}".format(self.marca, self.color, self.tamaño)
    def abrir(self):
        print('Abierto')
    def cerrar(self):
        print('Cerrado')
    def cargar_articulos(self, val):
        lista = []
        self.val = val
        self.lista = lista
        print('Agregue los articulos ')
        for articulos in range(self.val):
            art = input()
            self.lista.append(art)
        print('Articulos en la mochila:')
        print(self.lista)
    def sacar_articulos(self):
        #print('articulos en la mochila ', self.lista)
        quitar = input('Articulo a quitar: ')
        if quitar in self.lista:
            self.lista.remove(quitar)
        else:
            print('no hay ese articulo en la mochila')
        print('articulos en la mochila ', self.lista)
        
mochila1 = Mochila('JanSport', 'Azul', 'Oficio')
print(mochila1)
mochila1.abrir()
mochila1.cargar_articulos(2)
mochila1.sacar_articulos()
mochila1.cerrar()




