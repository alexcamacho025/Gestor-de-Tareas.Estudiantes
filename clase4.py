class Tarea:
    def __init__(self, titulo, descripcion, prioridad="Media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = " Completada" if self.completada else "⏳ Pendiente"
        return f"[{self.prioridad}] {self.titulo}: {self.descripcion} - {estado}"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print(" No hay tareas registradas.")
        for tarea in self.tareas:
            print(tarea)

    def mostrar_pendientes(self):
        pendientes = [t for t in self.tareas if not t.completada]
        if not pendientes:
            print("🎉 No hay tareas pendientes.")
        for tarea in pendientes:
            print(tarea)

    def mostrar_completadas(self):
        completadas = [t for t in self.tareas if t.completada]
        if not completadas:
            print(" No hay tareas completadas.")
        for tarea in completadas:
            print(tarea)

def menu():
    gestor = GestorTareas()

    while True:
        print("\n MENÚ DE TAREAS")
        print("1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Mostrar tareas pendientes")
        print("4. Mostrar tareas completadas")
        print("5. Marcar tarea como completada")
        print("6. Salir")

        opcion = input("👉 Elige una opción: ")

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            prioridad = input("Prioridad (Alta/Media/Baja): ")
            tarea = Tarea(titulo, descripcion, prioridad)
            gestor.agregar_tarea(tarea)
            print(" Tarea agregada con éxito.")

        elif opcion == "2":
            gestor.mostrar_tareas()

        elif opcion == "3":
            gestor.mostrar_pendientes()

        elif opcion == "4":
            gestor.mostrar_completadas()

        elif opcion == "5":
            gestor.mostrar_tareas()
            indice = int(input("Número de tarea a marcar como completada (empezando desde 1): ")) - 1
            if 0 <= indice < len(gestor.tareas):
                gestor.tareas[indice].marcar_completada()
                print(" Tarea marcada como completada.")
            else:
                print(" Número de tarea inválido.")

        elif opcion == "6":
            print(" Saliendo del gestor de tareas...")
            break

        else:
            print(" Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    menu()
