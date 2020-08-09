from os import system
system("cls")

from lista_circular_doble_enlazada import ListaCirculaDobleEnlazada

lista = ListaCirculaDobleEnlazada()
cantidadnodos = 10

for x in range(cantidadnodos):
    lista.agregar_final(x + 1)

lista.recorrer_inicio_a_fin()
print('*' * 25)

while cantidadnodos > 0:
    contador = 0
    for x in range(100000):
        print("Contador", contador)
        contador = contador + 1
        if contador > 10000:
            contador = 1
        elif contador == 10000:
            if not lista.vacia():
                print("------------------->> Nodo eliminado: -->>", lista.ultimo.dato)
                lista.eliminar_ultimo()
                cantidadnodos = cantidadnodos - 1