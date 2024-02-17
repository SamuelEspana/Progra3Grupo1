import graphviz

class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    @staticmethod
    def generar_grafico(filename, cabeza):
        dot = graphviz.Digraph(comment='Tarea Progra 4')
        actual = cabeza
        while actual:
            dot.node(str(id(actual)), f"{actual.nombre} {actual.apellido}\n({actual.carnet})")
            if actual.siguiente:
                dot.edge(str(id(actual)), str(id(actual.siguiente)), constraint='true')
            if actual.anterior:
                dot.edge(str(id(actual.anterior)), str(id(actual)), constraint='false', style='dotted')
            actual = actual.siguiente
        dot.render(filename, format='png', cleanup=True)

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo_nodo = Nodo(nombre, apellido, carnet)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar_por_valor(self, carnet):
        actual = self.cabeza
        while actual is not None:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente

                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.cola = actual.anterior

                del actual
                return
            actual = actual.siguiente

    def mostrar_lista(self):
        actual = self.cabeza
        lista_str = "None <- "
        while actual:
            lista_str += f"{actual.nombre} {actual.apellido} ({actual.carnet}) <-> "
            actual = actual.siguiente
        lista_str += "-> None"
        print(lista_str)

if __name__ == "__main__":
    lista = ListaDoblementeEnlazada()
    while True:
        print(" ")
        print("Menu del Sistema:")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")
        print(" ")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = input("Ingrese nombre del estudiante: ")
            apellido = input("Ingrese apellido del estudiante: ")
            carnet = input("Ingrese carnet del estudiante: ")
            lista.insertar_al_principio(nombre, apellido, carnet)
            lista.mostrar_lista()
            ListaDoblementeEnlazada.generar_grafico("Tarea1_Progra3.png", lista.cabeza)
        elif opcion == "2":
            nombre = input("Ingrese nombre del estudiante: ")
            apellido = input("Ingrese apellido del estudiante: ")
            carnet = input("Ingrese carnet del estudiante: ")
            lista.insertar_al_final(nombre, apellido, carnet)
            lista.mostrar_lista()
            ListaDoblementeEnlazada.generar_grafico("Tarea1_Progra3.png", lista.cabeza)
        elif opcion == "3":
            lista.mostrar_lista()
            carnet = input("Ingrese el carnet del estudiante a eliminar: ")
            lista.eliminar_por_valor(carnet)
            lista.mostrar_lista()
            ListaDoblementeEnlazada.generar_grafico("Tarea1_Progra3.png", lista.cabeza)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            print("Buen día")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción correcta.")
