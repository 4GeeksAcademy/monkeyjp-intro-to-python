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



#/-----------------------------------------------DIA DOS -----------------------------------#

# 🧩 1. Tuplas — Los Power-ups que no cambian
# 🎮 ¿Qué son?
# Las tuplas son como los poderes originales de Mario: una vez que los tiene, no cambian. Son listas inmutables.

# 🧪 Sintaxis:

power_up = ("super hongo", "estrella", "flor de fuego")


# 🔍 Acceder a elementos:

print(power_up[0])  # "super hongo"


# 🛡️ ¿Por qué usar tuplas?
# Cuando necesitás que los datos nunca cambien.

# Ejemplo: coordenadas fijas de un castillo.


def posicion_castillo():
    return (100, 200)

x, y = posicion_castillo()
print(f"Castillo en ({x}, {y})")



# ⚡ 2. Funciones Lambda — Los movimientos rápidos de Mario
# 🎮 ¿Qué son?
# Las funciones lambda son como un salto rápido: hacen algo pequeño y rápido, sin definir una función completa.


sumar_vidas = lambda vidas, extra: vidas + extra
print(sumar_vidas(3, 1))  # 4

# 🧠 Se usan mucho con map() y filter().




# 🔁 3. map() y filter() — Efectos especiales sobre listas
# 🍄 map() aplica un poder a cada ítem:

puntos = [10, 20, 30]
dobles = list(map(lambda x: x * 2, puntos))  # Mario duplica sus puntos
print(dobles)  # [20, 40, 60]

# 👀 filter() descarta lo que no sirve:

enemigos = [5, 10, 15, 2]  # Fuerza de enemigos
fuertes = list(filter(lambda e: e > 5, enemigos))  # Solo los fuertes quedan
print(fuertes)  # [10, 15]



# 🎯 4. List Comprehensions — Mario salta más alto con estilo

puntos = [50, 100, 150]
vidas_extra = [p for p in puntos if p >= 100]
print(vidas_extra)  # [100, 150]

# 🍌 Más ejemplos:

items = ["moneda", "hongo", "estrella"]
mensaje = [f"¡Mario encontró un {i}!" for i in items]



# 👥 5. Recorrer una lista de diccionarios — Aliados de Mario

aliados = [
    {"nombre": "Toad", "rol": "ayudante"},
    {"nombre": "Peach", "rol": "princesa"},
    {"nombre": "Luigi", "rol": "hermano"}
]

# Extraer nombres
nombres = [a["nombre"] for a in aliados]
print(nombres)  # ['Toad', 'Peach', 'Luigi']

# Saludo personalizado
saludos = [f"{a['nombre']} dice: ¡Vamos Mario!" for a in aliados]
print(saludos)




# 🤔 6. ¿for-in o map()? — Qué camino tomar

# 🛤️ Situación	                                    ✅ Recomendación
# Necesitás claridad y pasos extra                	for-in
# Querés hacer una sola operación	                    map() o comp.
# Vas a filtrar algo	                                filter()
# Vas a crear una nueva lista	                        List comprehension