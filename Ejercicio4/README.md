# Principios SOLID

## Single Responsibility

En el ejemplo mostrado, la classe Logger tiene una única responsabilidad, que es loggear información.

## Open Closed

En el ejemplo mostrado, la clase Employee no requiere que sea modificada si se quiere agregar una nueva
clase hija. Sin embargo, sí está abierta a expansión por medio de la abstracción del método say_hi que 
cada clase hija toma como desea.

## Liskov Substitution

En el ejemplo mostrado, dado que todas las clases hijas heredan y mantienen la misma estructura base que 
la clase Animal, a la hora de iterar por el arreglo de las hijas, su comportamiento no cambia.

## Interface Segregation

En el ejemplo mostrado, cada interfaz o función que puede tener un teléfono se segrega en clases separadas
(hacer llamadas, tomar fotos, jugar un juego). Así, cada hija de la clase Phone solo utiliza las 
interfaces que requiere.

## Dependency Inversion

En el ejemplo mostrado, la clase AudioPlayer depende del tipo de audio que procesa. Sin embargo, se agrega la
abstracción DataSource para evitar acoplamiento entre clases.