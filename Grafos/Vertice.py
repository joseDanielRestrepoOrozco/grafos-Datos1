class Vertice:

    def __init__(self, dato):
        self.dato = dato
        self.ListaAdyacentes = []

    def getDato(self):
        return self.dato

    def setDato(self, dato):
        self.dato = dato

    def getListaAdyacentes(self):
        return self.ListaAdyacentes

    def setListaAdyacentes(self, ListaAdyacentes):
        self.ListaAdyacentes = ListaAdyacentes
