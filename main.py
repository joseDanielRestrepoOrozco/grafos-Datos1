from Grafos.Grafo import *
from Grafos.Arista import *

A = Grafo()
A.ingresarVertices("A")
A.ingresarVertices("B")
A.ingresarVertices("C")
A.ingresarVertices("D")
A.ingresarVertices("F")
A.ingresarVertices("F")

A.mostrar(A.ListaVertices)

# ingreso las Aristas
A.ingresarArista("A", "B", 2)
# A.ingresarArista("B", "A", 50)

A.ingresarArista("B", "C", 20)
# A.ingresarArista("C", "B", 50)

A.ingresarArista("C", "D", 10)
# A.ingresarArista("D", "C", 50)

A.ingresarArista("D", "F", 5)

# A.ingresarArista("F", "D", 50)
A.ingresarArista("F", "A", 13)
# A.ingresarArista("A", "F", 50)

A.imprimirAristas()

A.imprimirVertices()

A.imprimirPromedioV()

A.pesoMayor()

A.pesoMenor()

A.mayorAdyacencia()

A.verificarPozos()

A.distanciaTotal()

print(A.masDestinos())

A.RecorridoProfundidad("D")

print(A.getVisitadosp())

print("arbol de expancion: \n")

A.Prim()
