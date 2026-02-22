import re


def invertir(s):
    if len(s) <= 1:
        return s
    return invertir(s[1:]) + s[0]


def es_palindromo(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and es_palindromo(s[1:-1])


def contar_caracter(s, c):
    if len(s) == 0:
        return 0
    return (1 if s[0] == c else 0) + contar_caracter(s[1:], c)

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def longitud(self):
        return self._longitud_recursiva(self.cabeza)
            
    def _longitud_recursiva(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._longitud_recursiva(nodo.siguiente)
    
    def encontrarDato(self, nodo, dato):
        if nodo is None:
            return False
        elif nodo.dato == dato:
            return True
        return self.encontrarDato(nodo.siguiente, dato)
    
# EL EJERCICIO DEL REPRODUCTOR DE MUSICA HACERLO DE MANERA RECURSIVA


def potencia(a,b):
    if b == 0:
        return 1
    return a * potencia(a, b -1)

def potencia_optimizada(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        mitad = potencia_optimizada(a, b // 2)
        return mitad * mitad
    else:
        return a * potencia_optimizada(a, b - 1)
    
def suma_digitos(n):
    if n < 10:
        return n
    digito = n % 10
    return digito + suma_digitos(n // 10)
    