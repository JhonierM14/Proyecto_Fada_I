from data_structures import abb
from form.encuestado import Encuestado

class Pregunta:
    def __init__(self, nombre, encuestados):
        self.nombre = nombre
        self.encuestados = encuestados
    
    def getNombre(self):
        return self.nombre
    
    def getEncuestados(self):
        return self.encuestados
    
    def getOpiniones(self):
        return [e.opinion for e in self.encuestados]

    def getExperticias(self):
        return [e.experticia for e in self.encuestados]
    
    def setEncuestados(self, encuestados):
        self.encuestados = encuestados

            # ----------------------------------------------- ABB -----------------------------------------------

    def get_ids_encuestados(self):
        def insertar_id(arbol, id_val):
            if arbol.val is None:
                arbol.val = id_val
                return
            if id_val < arbol.val:
                if arbol.left:
                    insertar_id(arbol.left, id_val)
                else:
                    arbol.left = abb(id_val)
            else:
                if arbol.right:
                    insertar_id(arbol.right, id_val)
                else:
                    arbol.right = abb(id_val)

        def recorrer_y_insertar(nodo_enc, arbol_ids):
            if nodo_enc is None or nodo_enc.val is None:
                return
            recorrer_y_insertar(nodo_enc.left, arbol_ids)
            insertar_id(arbol_ids, nodo_enc.val.id)
            recorrer_y_insertar(nodo_enc.right, arbol_ids)

        arbol_ids = abb()
        recorrer_y_insertar(self.encuestados, arbol_ids)
        return arbol_ids

    def promedio_opinion(self):
        def _suma_opiniones(nodo: abb):
            if nodo is None or nodo.val is None:
                return 0, 0  # suma, cantidad
            suma_izq, cant_izq = _suma_opiniones(nodo.left)
            suma_der, cant_der = _suma_opiniones(nodo.right)
            
            encuestado : Encuestado = nodo.getVal()
            suma_total = suma_izq + encuestado.getOpinion() + suma_der
            cantidad_total = cant_izq + 1 + cant_der
            return suma_total, cantidad_total

        suma, cantidad = _suma_opiniones(self.getEncuestados())
        return suma / cantidad if cantidad > 0 else 0