class Empleado:
    def __init__(self, rol, nombre, cedula):
        self.rol = rol
        self.nombre = nombre
        self.cedula = cedula

empleados = {"empleado1": {"nombre": "diego", "balance": 1000}, "empleado2": {"nombre": "gian", "balance": 2000}}

empleados["empleado1"]["balance"] += 500
print(empleados["empleado1"]["balance"])

def retirar_dinero(self, empleados, cantidad):
    if empleado in empleados:
        balance_actual = empleados[empleado]["balance"]
        if cantidad <= balance_actual:
            empleados[empleado]["balance"] -= cantidad
            print("Retiro exitoso. Nuevo balance:", empleados[empleado]["balance"])
        else:
            print("No tienes suficientes fondos para realizar el retiro")
    else:
        print("El empleado no existe")

def pago_de_salario(self, empleados, cantidad):
    for empleado in empleados:
        empleados[empleado]["balance"] += cantidad 
    print("Pago de salario exitoso. Nuevo balance:", empleados[empleado]["balance"])

class Nomina:
    def __init__(self, presupuesto, cantidad_dinero_disponible):
        self.presupuesto = presupuesto
        self.cantidad_dinero_disponible = cantidad_dinero_disponible
        empleados = []

    def pagar_nomina_empleados(self, empleado, monto_pago):
        if monto_pago != empleado.salario:
            return False
        return True

    def registrar_empleados(self, rol):
        rol = input("Ingrese el rol del empleado: ")
        nombre = input("Ingrese el nombre del empleado: ")
        cedula = input("Ingrese la cedula del empleado: ")

    def agregar_saldo_presupuesto_nomina(self, nomina, saldo_a_agregar):
        nomina += saldo_a_agregar
        return nomina

presupuesto_nomina = 15000
saldo_agregar = 7500
presupuesto_nomina = saldo_agregar
print("El presupuesto de la nomina es:", presupuesto_nomina)

def mostrar_empleados():
    print("Lista de empleados:")
    for empleado in empleados:
        print(f"{empleado}: {empleados[empleado]['nombre']}, balance: {empleados[empleado]['balance']}")

def menu():
    while True:
        print("\nBienvenido al sistema de gestión de empleados.")
        print("Seleccione una opción:")
        print("1. Registrar un nuevo empleado")
        print("2. Mostrar la lista de empleados")
        print("3. Pagar la nómina de los empleados")
        print("4. Agregar presupuesto a la nómina")
        print("5. Salir del sistema")

        opcion = input(">> ")

        if opcion == "1":
            rol = input("Ingrese el rol del empleado: ")
            nombre = input("Ingrese el nombre del empleado: ")
            cedula = input("Ingrese la cedula del empleado: ")
            nuevo_empleado = Empleado(rol, nombre, cedula)
            empleados[f"empleado{len(empleados) + 1}"] = {"nombre": nombre, "balance": 0}
            print(f"Empleado {nombre} registrado exitosamente.")

        elif opcion == "2":
            mostrar_empleados()

        elif opcion == "3":
            monto_pago = float(input("Ingrese el monto a pagar a cada empleado: "))
            for empleado in empleados:
                empleados[empleado]["balance"] += monto_pago
            print("Pago de salario exitoso.")

        elif opcion == "4":
            saldo_a_agregar = float(input("Ingrese el saldo a agregar a la nómina: "))
            presupuesto_nomina += saldo_a_agregar
            print("Saldo agregado exitosamente.")

        elif opcion == "5":
            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()

print("Arreglo agregado")
print("Versión final")