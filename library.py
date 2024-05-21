class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        
class Inventario:
    def __init__(self):
        self.libros = []
        
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print("Libro agregado:", libro.titulo)
        
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                print("Libro encontrado:")
                print("Titulo", libro.titulo)
                print("Autor", libro.autor)
                print("Precio", libro.precio)
                return
            print("El libro no se encuentra en el inventario.")
            
    def registrar_venta(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                print("Venta realizada:", libro.titulo)
                self.libros.remove(libro)
            return
        print("El libro no se encuentra en el inventario")
        
def main():
    inventario = Inventario()
    #libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 15.99)
    #libro2 = Libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 19.99)

    #inventario.agregar_libro(libro1)
    #inventario.agregar_libro(libro2)

    titulo = input("Introduce el título del libro nuevo: ")
    autor = input("Introduce el autor del libro nuevo: ")
    precio = input("Introduce el precio del libro nuevo: ")
    
    libro = Libro(titulo, autor, precio)
    inventario.agregar_libro(libro)
    
    #inventario.buscar_libro("El principito")
    #inventario.registrar_venta("El principito")
if __name__ == "__main__":
    main()
        