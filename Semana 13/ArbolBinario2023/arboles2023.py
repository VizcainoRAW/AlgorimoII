#Clase Arbol
class ArbolBinario:
    def __init__(self, dato, arbol_izquierdo = None, arbol_derecho = None) -> None:
        self.valor_nodo = dato
        self.hijo_izquierdo = arbol_izquierdo
        self.hijo_derecho = arbol_derecho     

    def esHoja(self):
        return self.hijo_izquierdo == None and self.hijo_derecho == None
    
    def __str__(self) -> str:
        return str(self.valor_nodo)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ArbolBinario):
            return False
        return self.valor_nodo == otro.valor_nodo

    #Visualización Arbol      
    def verArbol(self) -> str: 
        return self.__verArbol(self,"")
    
    def __verArbol(self, arbol:"ArbolBinario", recorrido:str, nivel = 0) -> str:
        espaciado = "\t" * nivel        
        if arbol is None:
            return ""
        recorrido =  espaciado + str(arbol.valor_nodo) + "\n" \
            + str(self.__verArbol(arbol.hijo_izquierdo, recorrido, nivel+1)) + \
            str(self.__verArbol(arbol.hijo_derecho, recorrido, nivel + 1)) + recorrido
        return recorrido        
    
    #RECORRIDOS
    #Preorden
    def preOrden(self):
        visitados = list()
        self.__preOrden(self, visitados)
        return visitados
    
    def __preOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados.append(arbol)
            visitados = self.__preOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__preOrden(arbol.hijo_derecho, visitados)
        return visitados
    #EnOrden
    def enOrden(self):
        visitados = list()
        self.__enOrden(self, visitados)
        return visitados
    
    def __enOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__enOrden(arbol.hijo_izquierdo, visitados)
            visitados.append(arbol)
            visitados = self.__enOrden(arbol.hijo_derecho, visitados)
        return visitados
    #PosOrden
    def posOrden(self):
        visitados = list()
        self.__posOrden(self, visitados)
        return visitados
    
    def __posOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__posOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__posOrden(arbol.hijo_derecho, visitados)
            visitados.append(arbol)
        return visitados
    #listar hojas  
    def listarHojas(self):
        lista_visitados= self.preOrden()
        lista_hojas = self.__listarHojas(self, lista_visitados)
        return lista_hojas
    
    def __listarHojas(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            lista_hojas=list()
            for i in visitados:
                if i.hijo_izquierdo == None and i.hijo_derecho == None:
                    lista_hojas.append(i)
        return lista_hojas
    
    def contarNodos(self):
        lista_nodos=self.preOrden()
        numero_nodos=len(lista_nodos)
        return numero_nodos
    
    def determinarAltura(self):
         nodos=list()
         lista_prfundidad=list()
         self.__determinarAltura(self, lista_prfundidad,nodos)
         return max(lista_prfundidad)
    
    def __determinarAltura(self, arbol:"ArbolBinario", profundida:list, nodos:list ,nivel = 0):
        if arbol is not None:
            nodos.append(arbol)
            profundida.append(nivel)
            nodos, profundidad= self.__determinarAltura(arbol.hijo_izquierdo, profundida,nodos, nivel +1)
            nodos, profundidad= self.__determinarAltura(arbol.hijo_derecho, profundida,nodos, nivel +1)
        return nodos , profundida
    
    def determinaNiveles(self):
        nodos=list()
        lista_prfundidad=list()
        self.__determinarAltura(self, lista_prfundidad,nodos)
        return nodos , "niveles de los nodos",lista_prfundidad

    def determinarCompleto(self):
         visitados=list()
         visitados , completo =  self.__determinarcompleto(self,visitados,True)
         if completo==True:
            return True
         if completo==False:
             return False
    
    def __determinarcompleto(self, arbol:"ArbolBinario", visitados:list,completo:True):
        if arbol is not None:
            if arbol.hijo_izquierdo == None and arbol.hijo_derecho is not None:
                completo=False
            if arbol.hijo_izquierdo is not None and arbol.hijo_derecho == None: 
                completo=False
            visitados.append(arbol)
            visitados, completo = self.__determinarcompleto(arbol.hijo_izquierdo, visitados,completo)                      
            visitados, completo = self.__determinarcompleto(arbol.hijo_derecho, visitados,completo)       
        return visitados, completo 
    

    
    
