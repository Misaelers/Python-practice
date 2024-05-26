import hashlib
from cryptography.fernet import Fernet

# Función para cifrar datos utilizando Fernet
def cifrar_datos(data, clave):
    cifrador = Fernet(clave)
    datos_cifrados = cifrador.encrypt(data.encode())
    return datos_cifrados

# Función para descifrar datos utilizando Fernet
def descifrar_datos(datos_cifrados, clave):
    cifrador = Fernet(clave)
    datos_descifrados = cifrador.decrypt(datos_cifrados).decode()
    return datos_descifrados

# Función para generar una clave para cifrar y descifrar datos
def generar_clave():
    return Fernet.generate_key()

# Función para cifrar contraseñas utilizando hashing
def cifrar_contrasena(contrasena):
    hash_cifrado = hashlib.sha256(contrasena.encode()).hexdigest()
    return hash_cifrado

# Función para verificar una contraseña cifrada
def verificar_contrasena(contrasena, hash_cifrado):
    hash_entrada = cifrar_contrasena(contrasena)
    return hash_entrada == hash_cifrado

# Ejemplo de uso

# Generar una clave para cifrar y descifrar datos
clave = generar_clave()

# Datos a cifrar
datos = "Información confidencial"

# Cifrar los datos
datos_cifrados = cifrar_datos(datos, clave)
print("Datos cifrados:", datos_cifrados)

# Descifrar los datos
datos_descifrados = descifrar_datos(datos_cifrados, clave)
print("Datos descifrados:", datos_descifrados)

# Ejemplo de hashing de contraseñas
contrasena = "contraseña123"
hash_cifrado = cifrar_contrasena(contrasena)
print("Contraseña cifrada:", hash_cifrado)

# Verificación de la contraseña
if verificar_contrasena("contraseña123", hash_cifrado):
    print("Contraseña válida.")
else:
    print("Contraseña inválida.")
