class Carro:
    def __init__(self,color: str = "Sin definir", año: int = 0, serie: str = "0000-0000"):
        self.__color = color
        self.__año = año
        self.__serie = serie

    def get_color(self) -> str:
        return self.__color

    def get_año(self) -> int:
        return self.__año

    def get_serie(self) -> str:
        return self.__serie

    def set_color(self, color : str):
        self.__color = color

    def set_año(self, color : int):
        self.__año = año

    def set_serie(self, color : str):
        self.__serie = serie

class Main:

    carro_1 = Carro()

    carro_2 = Carro("Negro",2024,"XV-1245")

    print("CARRO 1 (Constructor vacio): ")
    print(f"Color: {carro_1.get_color()} | Año: {carro_1.get_año()} | Serie: {carro_1.get_serie()}\n ")

    print("CARRO 2 (Constructor con parametros): ")
    print(f"Color: {carro_2.get_color()} | Año: {carro_2.get_año()} | Seire: {carro_2.get_serie()}\n")
    