class Book:
    #Función asociada a un objeto
    def __init__(self, t, a, s, p, id):
        self._titulo = t
        self._autor = a
        self._stock = s
        self._precio = p
        self._oid = id

    def obtener_inf(self):
        return f'Título: {self._titulo}\nAutor: {self._autor}\nStock: {self._stock}\nPrecio: {self._precio}\nID: {self._oid}'


    #Setter para obtener título
    def get_titulo(self):
        return self._titulo
    
    #Setter para cambiar título
    def set_titulo(self, nuevo_titulo):
        try:
            self._titulo = nuevo_titulo
        except:
            print('Caracter inválido')

    #Getter y seter precio
    def get_precio(self):
        return self._precio
    
    def set_precio(self, nuevo_precio):
        try:
            if nuevo_precio > 0:
                self._precio = nuevo_precio
            else:
                print('El precio no puede ser igual o menor a cero.')
        except:
            print('Caracter inválido')
    
    #Getter y Setter Autor
    def get_autor(self):
        return self._autor
    
    def set_autor(self, nuevo_autor):
        try:
            self._autor = nuevo_autor

        except:
           print('Caracter inválido')
    
    #Getter y Setter Stock
    def get_stock(self):
        return self._stock
    
    def set_stock(self,nuevo_stock):
        try:
            if nuevo_stock >= 0:
                self._stock = nuevo_stock
            else:
                print('El stock no puede ser menor a 0')
        except:
            print('Caracter inválido')
        
    #Getter y Setter ID
    def get_id(self):
        return self._oid
    
    def set_id(self, nuevo_oid):
        print(f'No puede cambiar al ID: {nuevo_oid}, ya que no esta permitido cambiar el ID del libro')
    
#Nueva clase
class Comic(Book):
    def __init__(self, t, a, s, p, id, ilustradores, volumen):
        super().__init__(t, a, s, p, id)
        self._ilustradores = ilustradores
        self._volumen = volumen
    
    #Polimorfismo
    def obtener_inf(self):
        info = super().obtener_inf()
        str_ilustradores = ', '.join(self._ilustradores)
        return f'{info}\nIlustradores: {str_ilustradores}\nVolumen: {self._volumen}'
    
    def get_ilustradores(self):
        return ', '.join(self._ilustradores)

    def set_ilustradores(self,n_ilustradores):
        try:
            self._ilustradores = n_ilustradores
        except:
            print('Caracter inválido')
    
    def get_volumen(self):
        return self._volumen
    
    def set_volumen(self, n_volumen):
        try:
            self._volumen = n_volumen
        except:
            print('Caracter inválido')
    
#Instanciar libro
book1 = Book('Toscano o la conformidad', 'Azorín', 100, 1000 ,1)
book2 = Book('1984', 'G. Orwell', 1200, 50, 2)
#print(book1)

#Instanciar Comic
comic1 = Comic('Batman', 'Alan Mure', 200, 250, 1, ['Desconocido para mí', 'Otro igual'], 1)
print(comic1.obtener_inf())

#Modificar ilustradores
# comic1.set_ilustradores(['Unos más', 'Otro más'])
# print(comic1.get_ilustradores())


#Obtener información con función incluida en el objeto
# print(book2.obtener_inf())


# book1.set_titulo('Hola Mundo')
# print(book1.get_titulo())

#Modificar precio
# book1.set_precio(1200)
# print(book1.get_precio())

#Modificar stock
# book1.set_stock(1)
# print(book1.get_stock())

#Modificar autor
# book1.set_autor('Nuevo autor')
# print(book1.get_autor())

#Modificar ID
# book1.set_id(4)
# print(book1.get_id())

