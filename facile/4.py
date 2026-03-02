class producto():
    def __init__(self, nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def mostrar_info(self):
        print(f"tus productos son{self.nombre} y precio es : {self.precio}  y lo ultimo {self.stock}" )
    
    def get_nombre(self):
        return self.nombre
    def get_precio(self):
        return self.precio
    def get_stock(self):
        return self.stock
    
class alimento(producto):
    def __init__(self, nombre, precio, stock, fecha):
        super().__init__(nombre, precio, stock)
        self.fecha=fecha
class electronico(producto):
    def __init__(self, nombre, precio, stock, garantia):
        super().__init__(nombre, precio, stock)
        self.garantia=garantia

p=producto("pan",2000, 20)
print (p.mostrar_info)


