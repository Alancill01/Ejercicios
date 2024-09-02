try:
    archivito=open(r"C:\Users\Alanr\OneDrive\Documentos\Paradigmas de programacion")
    data=archivito.read()
    print(data)
except IOError:
    print("Error al leer el archivo")
finally:
    archivito.close()