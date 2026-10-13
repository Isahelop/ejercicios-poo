class Usuario:
    def __init__(user,nombre : str = "sin nombre", saldo : float = 0.0):
        user.__nombre = nombre
        user.__saldo = saldo

    def getNombre(user) -> str:
        return user.__nombre

    def getSaldo(user) ->float:
        return user.__saldo

class Scooter:
    def __init__(sctr, id : str = "sin id", bateria : int = 0, disponibilidad : bool = True):
        sctr.__id = id
        sctr.__bateria = bateria
        sctr.__disponibilidad = disponibilidad

    def getId(sctr) -> str:
        return sctr.__id

    def getBateria(sctr) -> int:
        return sctr.__bateria

    def getDisponibilidad(sctr) -> bool:
        return sctr.__disponibilidad

scooter1 = Scooter()
scooter2 = Scooter("S250",50,False)
        
usuario1 = Usuario("Isahel", 100)

print("SCOOTERS")
print(f"scooter 1: {scooter1.getId()} | {scooter1.getBateria()} | {scooter1.getDisponibilidad()}")
print(f"scooter 1: {scooter2.getId()} | {scooter2.getBateria()} | {scooter2.getDisponibilidad()}\n")


print("USUARIO")
print(f"usuario: {usuario1.getNombre()} | {usuario1.getSaldo()}")
    