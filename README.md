# Numeros Complejos
Numeros complejos es un proyecto en el cual se encuentra la librería complex_numbers, librería la cual tiene como funcion realizar 
operaciones basicas de los números complejos, cabe aclarar que se entiende un número complejo como un número con una parte real, y
una parte imaginaria, en el programa el número complejo se __muestra__ como __real + imaginario*i__, sin embargo al momento de crearlo se presenta como una __tupla(real,img)__.
Para facilitar la experiencia del usuario, en el siguiente documento se le explica, como se debe usar la libreria, de igual manera, 
la libreria contiene comentarios en cada una de sus funciones en donde se explica que hace cada funcion.  

## Funciones
- __Para facilitar la experiencia del usuario todos los números en este programa son redondeados a dos cifras.__
- Suma de números complejos.
    + Retorna un número complejo en forma cartesiana.
    + Sean dos númeroscomplejos _C1(a1,b1)_ y _C2(a2,b2)_, el resulatdo de la suma de estos dos es un número complejo en forma cartesiana _C3(a1+a2, b1+b2)_.
- Resta de número complejos.
    + Retorna un número complejo en forma cartesiana.
    + Sean dos númeroscomplejos _C1(a1,b1)_ y _C2(a2,b2)_, el resulatdo de la resta de estos dos es un número complejo en forma cartesiana _C3(a1-a2, b1-b2)_.
- Producto entre números complejos.  
    + Retorna un número complejo en forma cartesiana.
    + Sean dos número complejos _C1(a1,b1)_ y _C2(a2,b2)_, se realiza el producto entre números complejos, dando asi como resultado un número complejo _C3(a1*a2 - b1*b2, a1*b2 + a2*b1)_
- Division entre números complejos.  
    + Retorna un número complejo en forma cartesiana.
    + Sean dos números complejos _C1(a1,b)_ y _C2(a2,b2)_, se realiza el cocientre dando como resultado un número complejo _C3((a1*a2 + b1*b2)/b1^2, (b1*a2 - a1*b2)/b2^2))_
- Módulo o norma de un número complejo.  
    + Retorna el un número con el valor del módulo del número complejo.
    + Sea un número complejo _C(a,b)_, su módulo se da por _mod = sqrt(a^2+b^2)_.
- Conjugado de un número complejo.  
    + Retorna un número complejo en forma cartesiana.
    + Sea un número complejo _C1(a1,b1)_, su conjugado sería _C2(a1,-b1)_.
- Coordenadas de un número complejo de cartesianas a polares. 
    + Retorna un número complejo en froma polar.
    + Sea unnúmero complejo _C1(a,b)_, su forma polar es _C1(modulo, fase)_.
- Fase de un número complejo.
    + Reetorna un número con el valor de la fase o ángulo de un número complejo.
    + Sea _C(a,b)_ un número complejo, su fase esta dada por _arctan(b/a)_.
- Coordenadas de un número complejo de polar a cartesianas.  
    + Retorna un número complejo en forma cartesiana.
    + Sea un número complejo en forma polar _C(r,tetha)_, su forma cartesiana esta dada por _C(rcos(tetha),rsen(tetha))_.
 
 ## Ejecución  
 
 Para ejecutar de manera eficiente y correcta la libreria complex_numbers siga estos pasos...
 + Descargue el archivo __complex_numbers.py__ del repositorio.
 + Una vez descargado el archivo.py, abra la aplicacion IDLE(Python...), una vez dentro abra el archivo descargado anteriormente y oprima __F5__.
 + Para crear un número complejo, asigne a una variable  __complex_cart(real,img)__, entre el parentesis debe ingresar el valor de la 
   parte real del número complejo, seguido el valor de la parte imaginaria del número.    
   
   ![Imgur](https://i.imgur.com/TNsnpXW.png)
 + Para ejecutar una operacion entre números complejos(+,-,*,/), asigne a dos variable un número complejo, siguiendo el paso anterior, posterior a esto  operelas
   como lo haría normalmente.   
   
   ![Imgur](https://i.imgur.com/M9Y5Vzn.png)
 + Para ejecutar las fucniones de __modulo,fase,polar,conjugado__, debe llamar cada una de las funciones de la siguiente mánera.    
 
   ![Imgur](https://i.imgur.com/RvCz1Ev.png)
 + Para ejecutar la función __cartesiana__, debe crear un número complejo en forma polar de la misma mánera que se creó un número complejo en forma cartesiana. Sin embargo en este   caso se le asigna a la variable __complex_polar(norma,ángulo)__ , asi ya puede hacer uso de la función __cartesiana__. De la siguiente mánera.   
 
   ![Imgur](https://i.imgur.com/6q1LP7x.png)
 + Para ejecutar la librería Test_complex siguiendo el primer paso, descargue la libreria y abra el archivo en el __IDLE__. 
     + Para ejecutar la librería simplemente oprima __F5__ en su teclado, el archivo se ejecutara. En la consola, se le mostrará el número de pruebas que se 
     realizaron en el programa, en este caso son 9, una por cada funcion de el programa complex_numbers. 
     ![Imgur](https://i.imgur.com/3nmPvyb.png)
 + Para modificar los valores de prueba, abra el archivo de Test_complex. En el encontrara la def __setUp__, en esta se inicializa cada uno de los números complejos. Si es de su agrado puede cambiar los valores o el nombre de las variables establecidos en el archivo, simplemente mantenga antes de cada nombre el __self.___, asi si desea cambiar la variable self.complex_a por comp1, este pasaría a ser self.comp1. Los valores se cambian en la linea complex_cart(/,/) ó complex_polar(/,/) dependiendo de la forma del número copmlejo, simplemente cambie los valores que se encuentran en los espacios del parentesis. De la siguiente mánera. 
 ![Imgur](https://i.imgur.com/xMbjswT.png)  
     + Para modificar las pruebas de cada función, simplemente cambie el contenido del __str()__, las pruebas estan formadas por dos partes la prueba, y el resultado esperado.
     __self.assertEqual(str(prueba),str(resultado))__. Debe tener en cuenta que retorna cada función (entero, tupla, decimal) además que recibe cada función(complex_cart(),complex_polar())
     ![Imgur](https://i.imgur.com/fb07UKm.png)
     
 
 
     
 
 ## Autor
   ___Cristian Andres Castellanos Fino___
