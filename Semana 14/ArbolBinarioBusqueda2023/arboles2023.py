#Clase Arbol Binario General
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

#Clase Arbol Binario de Búsqueda (ABB)
class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.raiz = None
    
    def estaVacio(self) -> bool:
        return self.raiz == None
    
    def __str__(self) -> str:
        if not self.estaVacio():
            return self.raiz.verArbol()
        return ""
    
    def __repr__(self) -> str:
        return self.__str__()
    
    #Recorrido
    def enOrden(self):
        if not self.estaVacio():
            return self.raiz.enOrden()
        return None

    #Insercion
    def insertar(self, elemento):
        if self.estaVacio():
            self.raiz = ArbolBinario(elemento)
        self.__insertar(self.raiz, elemento)

    def __insertar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is None:
                arbol.hijo_izquierdo = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_izquierdo, elemento)
        else:
            if arbol.hijo_derecho is None:
                arbol.hijo_derecho = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_derecho, elemento)
    
    #Búsqueda
    def buscar(self, elemento) -> ArbolBinario:
        if not self.estaVacio():
            return self.__buscar(self.raiz, elemento)
        return None
    
    def __buscar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return arbol
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is not None:
                return self.__buscar(arbol.hijo_izquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijo_derecho is not None:
                return self.__buscar(arbol.hijo_derecho, elemento)
            else:
                return None
    #Eliminar
    def eliminar(self, elemento):
        if not self.estaVacio():
            return self.__eliminar(self.raiz, elemento, None)
        return False
    
    def __eliminar(self, arbol:ArbolBinario, elemento, padre:ArbolBinario):
        if arbol is None:
            return False
        if elemento < arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_izquierdo, elemento, arbol)
        elif elemento > arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_derecho, elemento, arbol)
        else:
            #Caso Nodo hoja
            if arbol.esHoja():
                #Caso Nodo Hoja y Raiz
                if arbol == self.raiz:
                    self.raiz = None
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = None
                else:
                    padre.hijo_derecho = None
                return True
            #Caso Nodo con un hijo
            if arbol.hijo_izquierdo is None and arbol.hijo_derecho is not None:
                #Nodo con hijo derecho únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_derecho
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_derecho
                else:
                    padre.hijo_derecho = arbol.hijo_derecho
                return True
            if arbol.hijo_izquierdo is not None and arbol.hijo_derecho is None:
                #Nodo con hijo izquierdo únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_izquierdo
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_izquierdo
                else:
                    padre.hijo_derecho = arbol.hijo_izquierdo
                return True
            #Caso Nodo interno
            nodo_izquierdo:ArbolBinario = arbol.hijo_izquierdo
            nodo_temporal:ArbolBinario = None            
            while nodo_izquierdo.hijo_derecho is not None:
                nodo_temporal = nodo_izquierdo
                nodo_izquierdo = nodo_izquierdo.hijo_derecho
            arbol.valor_nodo = nodo_izquierdo.valor_nodo
            if nodo_temporal is None:
                arbol.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_izquierdo == nodo_izquierdo:
                nodo_temporal.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_derecho == nodo_izquierdo:
                nodo_temporal.hijo_derecho = nodo_izquierdo.hijo_izquierdo
            return True
    
    def bucarPadre(self, elemento):
        if not self.estaVacio():
            return self.__buscarPadre(self.raiz, elemento)
        return None
    
    def __buscarPadre(self, arbol:ArbolBinario, elemento): 
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is not None:
                if arbol.hijo_izquierdo.valor_nodo == elemento:
                    return arbol
                else:
                    return self.__buscarPadre(arbol.hijo_izquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijo_derecho is not None:
                if elemento == arbol.hijo_derecho.valor_nodo:
                    return arbol
                else:
                    return self.__buscarPadre(arbol.hijo_derecho, elemento)
            else:
                return None
            
    def maximaProfundidad(self):
        return self.raiz.determinarAltura()
    
    def valorMasCercanoArriba(self,elemento):
        lista_nodos=list()
        lista_nodos=self.raiz.preOrden()
        return self.__valorMasCercanoArriba(lista_nodos,elemento)
    
    def __valorMasCercanoArriba(self,lista_nodos:list,elemento):
        lista_nodos= self.raiz.enOrden()
        lista_diferencia=list()
        for i in range(len(lista_nodos)-1):
            diferencia=int(lista_nodos[i].valor_nodo)-elemento
            if diferencia<=0:
                diferencia=10*10**10
            lista_diferencia.append(diferencia)
        indice=0
        diferencia_minima=lista_diferencia[0]
        for i in range(len(lista_diferencia)-1):
            if diferencia_minima>lista_diferencia[i]:
                diferencia_minima=lista_diferencia[i]
                indice=i
        
        return lista_nodos[indice]
        


        

        
