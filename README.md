# poo en python 

. el paradigna de poo esta basada en una abstracion del mundo real que nos va a permitir desarrollar programas de forra mas cercana a como vemos el mundo.pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos.

# clase

- una clase es un tipo de dato cuyas variables se llaman objetos o istancias
- la clave es la definicion del concepto del mundo real y los objetos o istancias.son el "propio" objeto del mundo real.

### atributos 
- informacion que almacena la clase 


### metodos 
-operaciones que pueden realizar las clases.

## definicion de una clase en python

```python
class nomreclase:

    def _inif_(selt,variable1,variable2):
        self.atributo1 = valor1
        self.atributo = valor2

        def nombremetodo(self):
            bloquecodigo 
```
### componentes

```class```:palabra reservada en python para definir una clase.

``nombreclase``: nombre de clase que quieres crear.

```def``:palabra reservada en python que se utiliza para definir tanto el construtor de la clase (metdo que se ejecuta la primera vez que usas una clase)como los diferentes metodos que tiene.

``_inif_```:palabra reservada en python para definir el metodo construtor de la clase. es la primera que ejecuta cuando crear un objeto de una clase.

``(self,variablex)``: parametro del costrutor de la clase. el parametro self es obligatorio  y despues puedes tener tantos parametros como quieras.la forma de añadir parametros es la misma que las funciones.

``self.atributox``: forma de utilizacion y acceso a los atributos de la clase.

`ǹombremetodo`: nombre bdel metodo de la clase 

``(self)``: parametro del metodo el parametro selft es obligatorio y despues tener tantos parametros como quieras. la forma de añadir parametros es la misma que en las funciones

``bloquecodigo``: instrucciones que ejecutarian el metodo,

-cuamdo defines una clasen debes tener en cuenta los siguientes puntos:
-puedes difinir tantos atributos como nesesites
-puedes definir tantos metodos como nesesites
-puedes definir tantos parametros en el construtor y los metodos que nesesites,

## composicion
- consiste en la creacion de nuevas clases a partir de otras clases ya existentes que actuan como elementos compositores de la nueva.
-las clases existentes seran a tributos de la nueva clase.
- un poo la composicion significa que entre las dos clases existe una relacion del tipo"tiene un".
-ejemplo:una cordenada en dos dimenciones esta compuesta por dis valores, el valor en el eje de las y, esto podria ser una clase. un cuadrado esta compuesto por cuatro coordenadas que son los cuatro verticis, esto podria ser una clase que esta compuesta por cuatro  clases del objeto cordenado.