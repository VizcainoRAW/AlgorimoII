from arboles2023 import ArbolBinario
#Creacion de Nodos
raiz = ArbolBinario("A")
nodo01 = ArbolBinario("B")
nodo02 = ArbolBinario("C")
nodo03 = ArbolBinario("D")
nodo04 = ArbolBinario("E")
nodo05 = ArbolBinario("F")
nodo06 = ArbolBinario("Ñ",ArbolBinario(23),ArbolBinario(24))
#Conexion de nodos
raiz.hijo_izquierdo = nodo01
raiz.hijo_derecho = nodo02
nodo02.hijo_izquierdo = nodo03
nodo02.hijo_derecho = nodo04
nodo03.hijo_derecho = nodo05
nodo03.hijo_izquierdo = nodo06

#Visualización
print("Arbol:\n",raiz.verArbol())
print("Hoja del arbol: ",raiz,"\n",raiz.listarHojas())
print("Numero de nodos del arbol: ",raiz.contarNodos())
print("Altura del arbol: ",raiz.determinarAltura())

