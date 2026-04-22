# Lista de usuarios registrados
usuarios = []

# Lista de ventas del restaurante
ventas_restaurante = [
    {"idVenta": 1,  "nombreCliente": "Carlos Perez",    "numeroMesa": 3,  "platoPrincipal": "Bandeja Paisa",       "valorConsumo": 32000, "metodoPago": "EFECTIVO",      "estadoPedido": "ENTREGADO"},
    {"idVenta": 2,  "nombreCliente": "Maria Lopez",     "numeroMesa": 1,  "platoPrincipal": "Ajiaco",              "valorConsumo": 25000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 3,  "nombreCliente": "Juan Torres",     "numeroMesa": 5,  "platoPrincipal": "Churrasco",           "valorConsumo": 48000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "PENDIENTE"},
    {"idVenta": 4,  "nombreCliente": "Ana Gomez",       "numeroMesa": 2,  "platoPrincipal": "Cazuela de Mariscos", "valorConsumo": 55000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 5,  "nombreCliente": "Luis Ramirez",    "numeroMesa": 7,  "platoPrincipal": "Pollo Asado",         "valorConsumo": 28000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
    {"idVenta": 6,  "nombreCliente": "Sofia Herrera",   "numeroMesa": 4,  "platoPrincipal": "Trucha",              "valorConsumo": 38000, "metodoPago": "TRANSFERENCIA", "estadoPedido": "ENTREGADO"},
    {"idVenta": 7,  "nombreCliente": "Andres Castro",   "numeroMesa": 6,  "platoPrincipal": "Costillas BBQ",       "valorConsumo": 62000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 8,  "nombreCliente": "Camila Vargas",   "numeroMesa": 8,  "platoPrincipal": "Sancocho",            "valorConsumo": 22000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
    {"idVenta": 9,  "nombreCliente": "Diego Morales",   "numeroMesa": 3,  "platoPrincipal": "Lomo al Trapo",       "valorConsumo": 75000, "metodoPago": "TARJETA",       "estadoPedido": "ENTREGADO"},
    {"idVenta": 10, "nombreCliente": "Valentina Rios",  "numeroMesa": 2,  "platoPrincipal": "Arroz con Pollo",     "valorConsumo": 19000, "metodoPago": "EFECTIVO",      "estadoPedido": "PENDIENTE"},
]

# 2.   Función para registrar un nuevo usuario

def registrar_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    correo = input("Correo: ").strip()

    for usuario in usuarios:
        if usuario["correo"] == correo:
            print("Ese correo ya está registrado.")
            return

    password = input("Password: ").strip()
    usuarios.append({"correo": correo, "password": password})
    print("Usuario registrado correctamente.")


def iniciar_sesion():
    print("\n--- INICIO DE SESION ---")
    max_intentos = 4

    for intento in range(max_intentos):
        correo   = input("Correo: ").strip()
        password = input("Password: ").strip()

        for usuario in usuarios:
            if usuario["correo"] == correo and usuario["password"] == password:
                print("Login exitoso. Bienvenido,", correo)
                return True

        intentos_restantes = max_intentos - (intento + 1)
        if intentos_restantes > 0:
            print(f"Credenciales incorrectas. Intentos restantes: {intentos_restantes}")
        else:
            print("Cuenta bloqueada temporalmente.")
            return False

    return False