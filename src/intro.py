# 1. Introducción al Backend (10–15 min)
# Explicación clara y visual (usar pizarra o dibujo):

# Frontend	                            Backend
# Lo que ve el usuario	                Lo que sucede en el "servidor"
# HTML, CSS, JS	                        Python, Node.js, Java, etc.
# Corre en el navegador	                Corre en una computadora (servidor)
# Limitado por el navegador	            Acceso total a archivos, red, base de datos, etc.

# Ejemplos para dar contexto real:

# Frontend = Pantalla de login

# Backend = Verifica en la base de datos si el usuario existe

# Puntos clave:

# Backend ≠ navegador

# Backend puede hacer cosas que JS no puede (leer archivos, acceder a base de datos, etc.)

# Python es uno de los lenguajes más usados para backend

# ✳️ 2. ¿Qué es Python? (10 min)
# Un lenguaje de backend muy fácil de leer

# No necesita compilarse, solo ejecutarse (python archivo.py)

# Se usa en: backend web, data science, automatización, IA, etc.


nombre = "Mario"
edad = 25
pais = "Mushroom Kingdom"

# No hay constantes verdaderas, pero puedes escribir en MAYÚSCULAS para marcar que "no debería cambiarse":

PI = 3.1416

texto = "¡Mamma Mia!"
numero = 42
tiene_bigote = True
powerups = ["estrella", "hongo", "flor de fuego"]
princesa = {
    "nombre": "Peach",
    "edad": 25,
    "cabello": "amarillo"
}

 
#OPERADORES

#MATEMATICOS
vida_extra = 10 + 5
golpe = int("20") - int("3")

#COMPARACION
vidas = 3
vidas > 1      # True
vidas == 3     # True
vidas != 0     # True

#LOGICOS
tiene_llave = True
puerta_abierta = False

tiene_llave and puerta_abierta  # False
tiene_llave or puerta_abierta   # True
not tiene_llave                 # False


#FUNCIONES 

def saltar():
    print("¡Mario saltó!")

saltar()  # ¡Mario saltó!


def saludar(nombre):
    return f"Hola {nombre}!"

print(saludar("Toad"))


#CONDICIONALES
tiene_estrella = False

if tiene_estrella:
    print("¡Invencible! Corre sin miedo.")
else:
    print("Cuidado con los Goombas.")

puntos = 80

if puntos >= 100:
    print("¡Vida extra!")
elif puntos >= 50:
    print("¡Buen trabajo!")
else:
    print("¡Sigue intentándolo!")


#BUCLES
objetos = ["hongo", "flor", "estrella"]

for item in objetos:
    print("Mario encontró un", item)


# WHILE LOOP
vidas = 3

while vidas > 0:
    print("¡Sigue jugando!")
    vidas -= 1



print(golpe)