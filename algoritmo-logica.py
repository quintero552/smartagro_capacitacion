"""
Algoritmos y Lógica

Definición: Un algoritmo es una secuencia de pasos lógicos para resolver un problema.
Características: Finito, preciso y definido.
Ejemplo: Instrucciones para sumar dos números
1.- Leer el primer número
2.- Leer el segundo número
3.- Sumar los dos números
4.- Imprimir el resultado
"""

is_valid = False
while is_valid is False:
    try:
        primer_numero = int(input("Ingresa el primer número: "))
        is_valid = True
    except e :
        print("El valor ingresado no es un número")
        is_valid = False

segundo_numero = int(input("Ingresa el segundo número: "))
suma = primer_numero + segundo_numero
print(f"La suma de {primer_numero} + {segundo_numero} es: {suma}")

"""
Ejemplo: Freir un huevo
1.- Calentar la sartén
2.- Agregar aceite
3.- Romper el huevo
4.- Agregar el huevo a la sartén
5.- Cocinar el huevo
6.- Servir el huevo
"""


# java
String nombre_de_la_variable;

nombre_de_la_variable = "Hola Mundo";

System.out.println(nombre_de_la_variable);
## -----

String variable_2 = "Hola Mundo";

System.out.println(variable_2);

# Javascript
var nombre_de_la_variable= "Hola Mundo";
let variable_2 = "Hola Mundo";
const variable_3 = "Hola Mundo";
const OBJETO_1 = {
    nombre: "Hola Mundo",
    edad: 30
}

objeto.nombre = "Hola Mundo 2";


console.log(nombre_de_la_variable); # undefined

integer numero = 10;
Integer numero = 10;

string cadena="Hola Mundo";
String cadena = "Hola Mundo";


let numero1 = 1
numero1 = "hola mundo"

# TypeScript
let numerox: number = 10;
numerox = "Hola Mundo"; # error por que es un numero

# TIPOS DE DATOS
### Numericos:
# Enteros (int), decimales(float/double)
# Texto: Cadena de caracteres (string)
# Boleanos: True/False (bool) 
# Otros: Listas, Objetos, etc

# representar la complejidad de una funcion creo que se hace con 
# O(n)
# complejidad linea
# O(1)

seto.has(1) # O(1)

listas = [] / list()
tuplas = () / tuple()
dictionary = { } / dict()

let array = []
let objSet = new Set();
let objeto = { data = [], nombre = "Angel", edad = 30, funcion = () => console.log("Hola Mundo") }

class x {

}

x1 = new x();

let arreglo = ['1',{ nombre:'angel' },[1,2,3,4],() => console.log("hola"),x1,];
let objeto = {
    nombre: "Angel",
    apellido: "Gonzalez",
    edad:12
}
let objeto2 =  function (var1) {
    console.log(var1);
}

let objeto3 = (nombre) => console.log(`Hola ${nombre}`);

# lambda en python example

def suma(a,b):
    return a + b

suma1 = suma
suma = lambda a,b: a + b

sum(1,2)

suma1(1,2)

### Javascript
# Array // []
# Set 
# Map<key, value> // {}
# Object // {}
# Function // () => console.log("Hola Mundo")
# Class // class x { }
# Instance // new x()

### Python
# List // []
# Tuple // ()
# Dictionary // {}
# Function // def x(): pass
# Lambda // lambda x: x
# Class // class x: pass
# Instance // x()

#### OPERADORES
# Aritmeticos: +, -, *, /, %, **, //
# Relacionales: >, <, >=, <=, ==, !=
# Logicos: and, or, not

# Estructuras de control
# Condicional: if, else, elif
# Repetitivas: for, while, do while, case

# --- evaluda la condicion al inicio, podria no ejecutar su conetenido nunca
while True:
    print("Hola Mundo")

# --- se ejecuta al menos una ves, ya que evalua la condicion al final
do 
    print("Hola Mundo")
while True:
    

# Syntax - Sintaxis


# Estructura de datos ***

conjuntos = {1,2,3}

# Entrada y salida ****
input("Ingre un valor")
# salida
print("Hola Mundo")

# Maenjo de errores ****

try:
    print("Hola Mundo")

    with open("filex.txt", "r") as file:
        file.read()

# except ReadFile as e:
#     print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Adios")

try{
    console.log("Hola Mundo");
    throw new Error("Error");
}catch(e){
    console.log("Error", e);
}

#Conceptos básicos de orientación a objetos
Clase: Define un tipo de objeto.
Objeto: Instancia de una clase.
Atributos: Propiedades de un objeto.
Métodos: Acciones que un objeto puede realizar.

class Persona:

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
        self.x=1
    
    def saludar_(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años"

persona1 = Persona("Angel", 30)
persona1.saludar()

print("hola mundo")
"""
Esta clase permite calcular una remendacion de riego
Input: Temperatura, Humedad, Viento
Output: Recomendacion de riego
"""
Class Main {
    static void main(String[] args){
        System.out.println("Hola Mundo");
    }
}

# 10. Buenas prácticas
Documentación: Explica qué hace el código.
Nombres significativos: Usa nombres descriptivos para variables y funciones.
Indentación: Organiza el código para que sea legible.
Pruebas: Verifica que el código funcione correctamente.

# Test 
def test_suma(n1, n2):
    return n1 + n2

assert test_suma(1,2) == 3
assert test_suma(5,5) == 10

# Paradigma Imperativo
total = 0
for i in range(1, 6):
    total += i
print(total)

#Paradigma Declarativo
from functools import reduce
total = reduce(lambda x, y: x + y, range(1, 6))
print(total)

#Paradigma Orientado a Objetos (OOP)
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.nombre}"

p = Persona("Carlos")
print(p.saludar())

#Paradigma Procedural
def suma(a, b):
    return a + b

print(suma(3, 5))

#Paradigma Orientado a Eventos
document.getElementById("boton").addEventListener("click", () => {
    alert("Botón presionado");
});

#Paradigma Concurrente
import asyncio

async def tarea(nombre):
    print(f"Iniciando {nombre}")
    await asyncio.sleep(2)
    print(f"Terminando {nombre}")

asyncio.run(tarea("Tarea 1"))

#Paradigma Funcional
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]
cuadrados = map(cuadrado, numeros)

[].foreach(x => console.log(x))