# Clase para modelar un autor
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

# Clase para modelar un libro
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def informacion(self):
        return f"'{self.titulo}' por {self.autor.nombre} ({self.anio_publicacion})"

# Clase para modelar una biblioteca
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if self.libros:
            print(f"Libros en la biblioteca '{self.nombre}':")
            for libro in self.libros:
                print(libro.informacion())
        else:
            print(f"La biblioteca '{self.nombre}' no tiene libros.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear autores
    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    autor2 = Autor("Jane Austen", "Británica")

    # Crear libros
    libro1 = Libro("Cien años de soledad", autor1, 1967)
    libro2 = Libro("Orgullo y prejuicio", autor2, 1813)

    # Crear una biblioteca
    mi_biblioteca = Biblioteca("Biblioteca Central")

    # Agregar libros a la biblioteca
    mi_biblioteca.agregar_libro(libro1)
    mi_biblioteca.agregar_libro(libro2)

    # Mostrar libros en la biblioteca
    mi_biblioteca.mostrar_libros()
