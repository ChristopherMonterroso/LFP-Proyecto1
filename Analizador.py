class analizador:
    def __init__(self) -> None:
        self.cadena = ""
        self.linea=0
        self.columna=0
        self.lista=0

    def compile(self):
        archivo= open("prueba.txt","r")
        contenido = archivo.readlines()
        archivo.close 

        print("")

analizador().compile()