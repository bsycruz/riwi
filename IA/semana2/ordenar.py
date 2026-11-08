a = int(input("Primer #"))
b = int(input("Segundo #"))
c = int(input("Tercer #"))

if a <= b:
    if b <= c:
        print(a, b, c)
    elif a <= c:
        print(a, c, b)
    else:
        print(c, a, b)
else:
    if a <= c:
        print(b, a, c)
    elif b <= c:
        print(b, c, a)
    else:
        print(c, b, a)

#Después de realizar la consulta con los de modelo IA, en este caso se preguntó Con Gimini y Qwen para saber la respuesta

#El prompt que se entregó a los dos fue:
'''Escribe un programa en Python que pida tres números enteros y los muestre de menor a mayor. Usa solo input, if, else 
y comparaciones: sin listas, ciclos ni sorted(). Explica en tres líneas cómo funciona.'''

'QWEN - Gemini'

#Ambos modelos generaron el mismo tipo codigo, ninguno generó un codigo refactorizacion o más optimizado.


'''a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b


print(a, b, c)'''