# Advanced Python #3: Generators
Un generador en Python es una función especial que permite generar una secuencia de valores de forma eficiente. En lugar de devolver una sola vez un valor utilizando `return`, un generador produce una serie de valores utilizando la palabra clave `yield`. Esto significa que el estado de la función se conserva entre las llamadas, permitiendo que la función se "pausa" y "resuma" según sea necesario.

Aquí tienes un ejemplo simple de cómo se ve un generador en Python:

```python
def contador(max):
    n = 0
    while n < max:
        yield n
        n += 1

# Creamos un generador llamando a la función contador
mi_generador = contador(5)

# Iteramos sobre los valores generados
for numero in mi_generador:
    print(numero)
```

En este ejemplo, `contador` es una función generadora que produce una secuencia de números del 0 al `max - 1`. En cada iteración del bucle `for`, la función `contador` se pausa en la línea con `yield`, devolviendo el valor actual de `n`. Cuando se reanuda, la función continúa desde donde se detuvo, con `n` conservando su estado.

Algunas características importantes de los generadores:

- Los generadores son más eficientes en términos de memoria, ya que no generan todos los valores de una vez, sino que los generan uno a la vez según sea necesario.
- Permiten trabajar con secuencias potencialmente infinitas de datos.
- Se pueden utilizar en bucles `for`, como en el ejemplo anterior, o con otras funciones que acepten iterables, como `sum()` o `list()`.

Los generadores son muy útiles cuando necesitas trabajar con grandes conjuntos de datos o cuando deseas generar secuencias de valores de manera eficiente sin cargar todo en la memoria al mismo tiempo.