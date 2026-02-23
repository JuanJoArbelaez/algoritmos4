class Paciente:
    def __init__(self, nombre, documento, tipo):
        self.nombre = nombre
        self.documento = documento
        self.tipo = tipo
        self.siguiente = None

class Clinica:
    def __init__(self):
        self.primero = None

    # metodo recursivo para agregar paciente 
    def agregar_paciente(self, nombre, documento):
        nuevo_paciente = Paciente(nombre, documento, "Normal")
        if self.primero is None:
            self.primero = nuevo_paciente
        else:
            self._agregar_normal_recursivo(self.primero, nuevo_paciente)

    def _agregar_normal_recursivo(self, nodo_actual, nuevo_paciente):
        if nodo_actual.siguiente is None:
            nodo_actual.siguiente = nuevo_paciente
        else:
            self._agregar_normal_recursivo(nodo_actual.siguiente, nuevo_paciente)

    # metodo para agregar paciente de emergencia 
    def agregar_paciente_emergencia(self, nombre, documento):
        nuevo_paciente = Paciente(nombre, documento, "Emergencia")
        nuevo_paciente.siguiente = self.primero
        self.primero = nuevo_paciente

    # metodo para mostrar la lista
    def mostrar_lista(self):
        if self.primero is None:
            print("No hay pacientes en espera.")
        else:
            paciente_actual = self.primero
            while paciente_actual:
                print(f"Nombre: {paciente_actual.nombre}, Documento: {paciente_actual.documento}, Tipo de atención: {paciente_actual.tipo}")
                paciente_actual = paciente_actual.siguiente
            print("-----------------------")

    # metodo para atender o eliminar
    def atender_paciente(self):
        if self.primero is None:
            print("No hay pacientes para atender.")
        else:
            paciente_atendido = self.primero
            self.primero = self.primero.siguiente
            print(f"Paciente atendido: {paciente_atendido.nombre}, Documento: {paciente_atendido.documento}")

clinica = Clinica()

while True:
    print("Bienvenidos al hospital \n paso al infierno")
    print("\n¿Que deseas hacer?")
    print("1. Agregar paciente normal")
    print("2. Agregar paciente de emergencia")
    print("3. Mostrar lista de pacientes en espera")
    print("4. Atender paciente")
    print("0. Salir")
    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        nombre = input("Ingresa el nombre del paciente: ")
        documento = input("Ingresa el documento del paciente: ")
        clinica.agregar_paciente(nombre, documento)
    elif opcion == 2:
        nombre = input("Ingresa el nombre del paciente de emergencia: ")
        documento = input("Ingresa el documento del paciente de emergencia: ")
        clinica.agregar_paciente_emergencia(nombre, documento)
    elif opcion == 3:
        clinica.mostrar_lista()
    elif opcion == 4:
        clinica.atender_paciente()
    elif opcion == 0:
        print("Gracias")
        break
    else:
        print("Opcion erronea")