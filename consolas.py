
def validar_sigla(sigla, consolas):
    return 2 <= len(sigla) <= 5 and sigla.isupper() and sigla not in consolas

def validar_nombre(nombre):
    
    return 3 <= len(nombre) <= 40

def validar_fabricante(fabricante):
    return 2 <= len(fabricante) <= 30

def validar_anio(anio):
    if not anio.isdigit():
        return False
    return 1972 <= int(anio) <= 2025

def validar_precio(precio):
    try:
        return float(precio) > 0
    except ValueError:
        return False

def validar_stock(stock):
    return stock.isdigit() and int(stock) >= 0


def solicitar_datos_consola(consolas):
    sigla = input("Ingrese Sigla (2-5 caracteres, MAYÚSCULAS): ").strip()
    if not validar_sigla(sigla, consolas):
        print("[ERROR]Sigla inválida o ya registrada en el sistema.")
        return None

    nombre = input("Ingrese Nombre (3-40 caracteres): ").strip()
    if not validar_nombre(nombre):
        print("[ERROR] El nombre debe tener entre 3 y 40 caracteres.")
        return None

    fabricante = input("Ingrese Fabricante (2-30 caracteres): ").strip()
    if not validar_fabricante(fabricante):
        print("[ERROR] El fabricante debe tener entre 2 y 30 caracteres.")
        return None

    anio = input("Ingrese Año de lanzamiento (1972-2025): ").strip()
    if not validar_anio(anio):
        print("[ERROR] Año inválido. Debe ser un AÑO entre 1972 y 2025.")
        return None

    precio = input("Ingrese Precio (Mayor a 0): ").strip()
    if not validar_precio(precio):
        print("[ERROR] Precio inválido. Debe ser un número MAYOR a 0.")
        return None

    stock = input("Ingrese Stock (Mayor o igual a 0): ").strip()
    if not validar_stock(stock):
        print("[ERROR] Stock inválido. Debe ser un entero MAYOR o IGUAL a 0.")
        return None

    
    return sigla, nombre, fabricante, int(anio), float(precio), int(stock)


def agregar_consola(consolas, ventas):
    print("\n--- AGREGAR NUEVA CONSOLA ---")
    datos = solicitar_datos_consola(consolas)
    
    if datos is not None:
        sigla, nombre, fabricante, anio, precio, stock = datos
        consolas[sigla] = [nombre, fabricante, anio]
        ventas[sigla] = [precio, stock]
        print(f"\n¡Consola [{sigla}] agregada exitosamente!")


def buscar_consola(sigla, consolas):
    return sigla in consolas


def consultar_consola(consolas, ventas):
    print("\n--- BUSCAR CONSOLA ---")
    sigla = input("Ingrese la sigla de la consola a buscar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        nombre, fabricante, anio = consolas[sigla]
        precio, stock = ventas[sigla]
        
        print("\n=== Consola Encontrada ===")
        print(f"Sigla       : {sigla}")
        print(f"Nombre      : {nombre}")
        print(f"Fabricante  : {fabricante}")
        print(f"Año lanz.   : {anio}")
        print(f"Precio      : ${precio}")
        print(f"Stock       : {stock} unidades")
    else:
        print("Error: La consola no se encontró en el sistema.")


def eliminar_consola(consolas, ventas):
    print("\n--- ELIMINAR CONSOLA ---")
    sigla = input("Ingrese la sigla de la consola a eliminar: ").strip().upper()
    
    if buscar_consola(sigla, consolas):
        del consolas[sigla]
        del ventas[sigla]
        print(f"¡Consola [{sigla}] eliminada de ambos registros correctamente!")
    else:
        print("Error: No se puede eliminar, la consola no existe.")


def mostrar_consola(consolas, ventas):
    if not consolas:
        print("\nEl sistema está vacío. No hay consolas registradas.")
        return

    print("\n==============================")
    print("LISTADO COMPLETO DE CONSOLAS")
    print("==============================")
    
    for sigla in consolas:
        nombre, fabricante, anio = consolas[sigla]
        precio, stock = ventas[sigla]
    
        print(f"Sigla: {sigla} | {nombre} | {fabricante} | {anio} | ${precio} | Stock: {stock}")
        
    print("==============================")
    print(f"Total de consolas: {len(consolas)}")




def op_menu():
    print("\n========================================")
    print("  SISTEMA DE GESTIÓN DE CONSOLAS")
    print("========================================")
    print("1. Agregar consola")
    print("2. Buscar consola por sigla")
    print("3. Eliminar consola")
    print("4. Mostrar todas las consolas")
    print("5. Salir")
    print("========================================")
    return input("Seleccione una opción (1-5): ").strip()


def main():
    dicc_consolas = {}
    dicc_ventas = {}
    
    while True:
        opcion = op_menu()
        
        if opcion == "1":
            agregar_consola(dicc_consolas, dicc_ventas)
        elif opcion == "2":
            consultar_consola(dicc_consolas, dicc_ventas)
        elif opcion == "3":
            eliminar_consola(dicc_consolas, dicc_ventas)
        elif opcion == "4":
            mostrar_consola(dicc_consolas, dicc_ventas)
        elif opcion == "5":
            print("\nSaliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()