# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

num_entero = 36
print(num_entero)

# 2) Imprimir el tipo de dato de la constante 8.5

const = 8.5
print(type(const))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print(type(num_entero))

# 4) Crear una variable que contenga tu nombre

mi_nombre = 'Bruno'
print(mi_nombre)

# 5) Crear una variable que contenga un número complejo

num_complejo = num_entero + 5j
print(num_complejo)

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print(type(num_complejo))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

var_pi = 4.1416
print(var_pi)

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var_True1 = 'True'
var_True2 = True
print(type(var_True1))
print(type(var_True2))

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print(type(var_True1))
print(type(var_True2))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

var_suma = num_entero + const
print(var_suma)

# 11) Realizar una operación de suma de números complejos

var_sum_complejos = (11 + 1j) + (12 + 2j)
print(var_sum_complejos)
print(type(var_sum_complejos))

# 12) Realizar una operación de suma de un número real y otro complejo

print(const + var_sum_complejos)

# 13) Realizar una operación de multiplicación

print(const * num_entero)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

var_div = 27 / 4
print(var_div)

# 16) De la división anterior solamente mostrar la parte entera

print(int(var_div))
print(27 // 4)

# 17) De la división de 27 entre 4 mostrar solamente el resto

print(27 % 4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

print(4 * (27 // 4) + (27 % 4))

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

print('2F3G4G' + '27623H')

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print('2' == 2)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(int('2') == 2)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

a = float('3.8')
print(a)

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

variable = 3
variable -= 2
print(variable)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

print(11 << 4 << 65)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

print(str(2) + '2')
print(2 + int('2'))

# 26) Realizar una operación válida entre valores de tipo entero y string

print('2'*5)