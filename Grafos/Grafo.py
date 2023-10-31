from Grafos.Vertice import *
from Grafos.Arista import *
from copy import copy  # para realizar copias de objetos


class Grafo:

    def __init__(self):
        self.ListaVertices = []
        self.ListaAristas = []
        self.visitadosCp = []
        self.visitadosCa = []

    def ingresarVertices(self, dato):
        if not self.verificarExisteV(dato, self.ListaVertices):
            self.ListaVertices.append(Vertice(dato))

    def verificarExisteV(self, dato, lista):
        for i in range(len(lista)):
            if dato == lista[i].getDato():
                return True
        return False

    def mostrar(self, lista):
        for i in range(len(lista)):
            print(lista[i].getDato(), end='')

    def ingresarArista(self, origen, destino, peso):
        if not self.verificarExisteA(origen, destino, self.ListaAristas):  # verifico que no este repetida la arista
            if self.verificarExisteV(origen, self.ListaVertices) and self.verificarExisteV(destino, self.ListaVertices):
                self.ListaAristas.append(Arista(origen, destino, peso))  # ingreso la arista
                self.obtenerOrigen(origen).getListaAdyacentes().append(destino)

    def verificarExisteA(self, origen, destino, lista):  # verificar si existe la arista
        for i in range(len(lista)):
            if origen == lista[i].getOrigen() and destino == lista[i].getDestino():
                return True
        return False  # Porque no existe, permite el ingreso

    def obtenerOrigen(self, origen):
        for i in range(len(self.ListaVertices)):
            if origen == self.ListaVertices[i].getDato():
                return self.ListaVertices[i]

    def imprimirAristas(self):
        print()
        print("Las Aristas")
        for i in range(len(self.ListaAristas)):
            print(
                "origen: {0}- Destino: {1}".format(self.ListaAristas[i].getOrigen(), self.ListaAristas[i].getDestino()))

    def imprimirVertices(self):
        print()
        print("Los Vertices")
        for i in range(len(self.ListaVertices)):
            print("Vertice: {0}".format(self.ListaVertices[i].getDato()))
            self.imprimirAdyacencias(self.ListaVertices[i].getListaAdyacentes())

    def imprimirAdyacencias(self, adyacencias):
        print("Adyacencias: ", end="")
        for i in range(len(adyacencias)):
            print("{0},".format(adyacencias[i]), end="")
        print()

    def imprimirPromedioV(self):
        suma = 0
        n = len(self.ListaAristas)
        for i in range(n):
            suma += self.ListaAristas[i].getPeso()
        if n != 0:
            suma = suma // n
        print(f"\nPromedio de distancia: {suma}")

    def pesoMayor(self):
        mayor = 0
        n = len(self.ListaAristas)

        for i in range(n):
            peso = self.ListaAristas[i].getPeso()
            if peso > mayor:
                mayor = peso
            print(f"\nMayor distancia: {mayor}")
            return
        print("\nNo hay aristas")

    def pesoMenor(self):
        n = len(self.ListaAristas)  # para ahorrar caracteres guardo la longitud de la lista de aristas en una variable
        menor = None  # inicializo la variable de la distancia menor

        for i in range(n):
            peso = self.ListaAristas[i].getPeso()
            if i == 0:  # defino el peso menor como el primer peso de la lista
                menor = peso
            else:
                if peso < menor:
                    menor = peso
        mensaje = f"\nMenor distancia: {menor}" if menor is not None else f"\nNo hay aristas"
        print(mensaje)

    def mayorAdyacencia(self):
        n = len(self.ListaVertices)
        mayorAdy = None

        for i in range(n):
            vertAct = self.ListaVertices[i]
            if i == 0:
                mayorAdy = vertAct
            else:
                if len(mayorAdy.getListaAdyacentes()) < len(vertAct.getListaAdyacentes()):
                    mayorAdy = vertAct
        mensaje = f"\nvertice con mayor adyacencia: {mayorAdy.getDato()}" if mayorAdy is not None else "\nNo hay Vertices"
        print(mensaje)

    def verificarPozos(self):
        print()
        for i in range(len(self.ListaVertices)):
            if not len(self.ListaVertices[i].getListaAdyacentes()):
                print("si, tiene pozos")
                return
        print("No tiene pozos")

    def distanciaTotal(self):
        dist = 0
        for i in range(len(self.ListaAristas)):
            dist += self.ListaAristas[i].getPeso()

        print(f"\ndistancia total: {dist}")

    def masDestinos(self):
        temp = []
        if len(self.ListaAristas) == 0:
            print("sin lista")
            return
        for i in range(len(self.ListaAristas)):
            temp.append(self.ListaAristas[i].getDestino())
        return max(temp, key=temp.count)

    def RecorridoProfundidad(self, dato):  # dato es en que vertice empieza el recorrido
        if dato in self.visitadosCp:
            return
        else:
            vertice = self.obtenerOrigen(dato)
            if vertice is not None:
                self.visitadosCp.append(vertice.getDato())
                for dato in vertice.getListaAdyacentes():
                    self.RecorridoProfundidad(dato)

    def getVisitadosp(self):
        return self.visitadosCp

    def getVisitadosca(self):
        return self.visitadosCa

    def obtenerOrigen(self, origen):
        vertices = self.ListaVertices
        for i in range(len(vertices)):
            if origen == vertices[i].getDato():
                return vertices[i]

    def Ordenar(self, Aristas):
        for i in range(len(Aristas)):
            for j in range(len(Aristas)):
                if Aristas[i].getPeso() < Aristas[j].getPeso():  # menor a mayor
                    temp = Aristas[i]
                    Aristas[i] = Aristas[j]
                    Aristas[j] = temp
        # Prim para grafos dirigidos un solo sentido

    def Prim(self):
        CopiaAristas = copy(self.ListaAristas)  # copia de las aristas
        Conjunto = []
        AristaPrim = []  # creo una lista con las aristas
        AristasTemp = []  # Todas las adyacencias

        self.Dobles(CopiaAristas)

        self.Ordenar(CopiaAristas)  # ordeno las aristas
        # self.Repetidas(CopiaAristas)#elimino los caminos dobles, ya que no nos interesan las dobles conexiones

        menor = CopiaAristas[0]
        Conjunto.append(menor.getOrigen())
        pos = True
        while (pos):  # nuevo
            for Vertice in Conjunto:
                self.Algoritmo(CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos)
            if len(Conjunto) == len(self.ListaVertices):  # nuevo
                pos = False  # nuevo
        print("los vertices visitados fueron: {0} ".format(Conjunto))

        for dato in AristasTemp:
            print("temporal Origen: {0} destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(),
                                                                       dato.getPeso()))
        print("Aristas de prim")
        for dato in AristaPrim:
            print("Origen: {0} destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(), dato.getPeso()))

    def Algoritmo(self, CopiaAristas, AristaPrim, Conjunto, Vertice, AristasTemp, pos):
        ciclo = False
        # lo debo buscar en la lista de arista en ambas direcciones
        self.AgregarAristasTemp(CopiaAristas, Vertice, Conjunto, AristasTemp)
        menor = self.BuscarmenorTemp(AristasTemp, AristaPrim,
                                     CopiaAristas)  # obtengo la arista menor de los nodos que he visitado
        if menor is not None:
            if menor.getOrigen() in Conjunto and menor.getDestino() in Conjunto:  # es porque cierra un ciclo
                ciclo = True

            if ciclo is False:  # si es falso es porq puede ingresar
                if not menor.getDestino() in Conjunto:
                    Conjunto.append(menor.getDestino())
                AristaPrim.append(menor)

    def AgregarAristasTemp(self, CopiaAristas, Vertice, Conjunto, AristasTemp):
        for Aristas in CopiaAristas:
            if Vertice == Aristas.getOrigen():
                if self.verificarTemp(Aristas, AristasTemp):  # si no esta
                    AristasTemp.append(Aristas)  # Agrego todas las aristas

    def BuscarmenorTemp(self, AristasTemp, AristaPrim, CopiaAristas):
        menor = CopiaAristas[len(CopiaAristas) - 1]  # el mayor como esta ordenado, es el ultimo
        for i in range(len(AristasTemp)):
            if AristasTemp[i].getPeso() <= menor.getPeso():
                if not self.BuscarPrim(AristaPrim, AristasTemp[i]):
                    menor = AristasTemp[i]

        AristasTemp.pop(AristasTemp.index(menor))
        return menor

    def BuscarPrim(self, AristaPrim, menor):
        for Aristap in AristaPrim:
            if Aristap.getOrigen() == menor.getOrigen() and Aristap.getDestino() == menor.getDestino():
                return True
            if Aristap.getOrigen() == menor.getDestino() and Aristap.getDestino() == menor.getOrigen():
                return True
        return False

    def verificarTemp(self, Aristan, AristasTemp):
        for arista in AristasTemp:
            if arista.getOrigen() == Aristan.getOrigen() and arista.getDestino() == Aristan.getDestino():
                return False

        return True

        ##Elimina los repetidos porque en prim no toma en cuenta las direcciones del grafo, por consiguiente con un enlace es mas que suficiente

    def Repetidas(self, CopiaAristas):
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if elemento.getOrigen() == CopiaAristas[i].getDestino() and elemento.getDestino() == CopiaAristas[i].getOrigen():
                    CopiaAristas.pop(i)  # elimino
                    break

    def Dobles(self, CopiaAristas):
        doble = False
        for elemento in CopiaAristas:
            for i in range(len(CopiaAristas)):
                if elemento.getOrigen() == CopiaAristas[i].getDestino() and elemento.getDestino() == CopiaAristas[i].getOrigen():
                    doble = True
            if doble is False:
                CopiaAristas.append(Arista(elemento.getDestino(), elemento.getOrigen(), elemento.getPeso()))
            doble = False
