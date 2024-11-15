class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos: list[Asiento] = asientos
        self.marca = marca
        self.motor: Motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        contador_asientos = 0
        for i in range(len(self.asientos)):
            if self.asientos[i] != None:
                contador_asientos += 1
        return contador_asientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for asiento in range(len(self.asientos)):
                if isinstance(self.asientos[asiento], Asiento):
                    if self.asientos[asiento].registro == self.registro:
                        return "Auto original"
                    else:
                        return "Las piezas no son originales"
        return "Las piezas no son originales"

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo
