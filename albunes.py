catalogo=[]
class album:
    def __init__(self,nombre,artista,genero,precio,cantidad):
        self.nombre=nombre
        self.artista=artista
        self.genero=genero
        self.precio=precio
        self.cantidad=cantidad
    def __str__(self):
        return f"{self.nombre}-{self.artista} | {self.genero} | $ {self.precio} | stock:{self.cantidad}"