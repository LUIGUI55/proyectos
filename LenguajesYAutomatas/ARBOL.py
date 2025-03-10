# Arbol.py
class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = [] if hijos is None else hijos
        self.padre = None
        self.set_hijos(self.hijos)

    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos is not None:
            for h in self.hijos:
                h.padre = self

    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre
        self.hijos = []
        self.set_hijos(self.hijos)

    def get_hijos(self):
        return self.hijos

    def set_datos(self, datos):
        self.datos = datos

    def igual(self, nodo):
        return self.datos == nodo.datos

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def get_datos(self):
        return self.datos

    def __str__(self):
        return f"Nodo({self.datos})"


