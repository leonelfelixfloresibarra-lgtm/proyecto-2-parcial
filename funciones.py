from albunes import album, catalogo
def registrar_album():
    print("\n === REGISTRAR ALBUM ===")
    nombre=input("nombre del album: ")
    artista=input("artista/banda: ")
    genero=input("genero musical: ")
    precio=float(input("precio: "))
    cantidad=int(input("cantidad en stock : "))
    album=album (nombre,artista,genero,precio,cantidad)
    catalogo.append(album)
    print(f"album ´{nombre}´ de {artista} agregado correctamente")