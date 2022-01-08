# centrar_ventana.py
# función centrar.
def centrar(ancho, alto, app):
    x = app.winfo_screenwidth() // 2 - ancho // 2
    y = app.winfo_screenheight() // 2 - alto // 2

    posi = str(ancho) + 'x' + str(alto) + '+' + str(x) + '+' + str(y)

    return posi

if __name__ == '__main__':
    pass
