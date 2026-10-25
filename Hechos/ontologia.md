# Ontologia de Clasificacion de Animales

## Descripcion
Esta ontologia representa el conocimiento obtenido a partir del analisis del texto de la biologa Ana Torres y de las entrevistas realizadas sobre el leon marino y el pato. Se muestran las clases, instancias, propiedades y relaciones utilizadas para clasificar animales.

## Diagrama
![Ontología](ontologia.png)

## Clases
- Animal
- Mamifero
- Ave
- Carnivoro
- Ungulado

## Instancias

### Mamiferos
- LeonMarino
- Foca
- Guepardo
- Tigre
- Jirafa
- Cebra

### Aves
- Pinguino
- Albatros
- Pato
- Ganso

## Propiedades

### Mamiferos
- ViveEnAgua
- TieneAletas
- OrejasExternas
- DaLeche
- ComeCarne
- ColorLeonado
- ManchasOscuras
- RayasNegras
- TienePezunas
- CuelloLargo

### Aves
- TienePlumas
- Nada
- BlancoNegro
- VuelaMuyBien
- PatasPalmeadas
- PicoAnchoPlano
- CuelloCorto
- CuerpoGrande

## Relaciones
- Carnivoro pertenece a Mamifero.
- Ungulado pertenece a Mamifero.
- Mamifero pertenece a Animal.
- Ave pertenece a Animal.
- Guepardo y Tigre pertenecen a Carnivoro.
- Jirafa y Cebra pertenecen a Ungulado.
- LeonMarino y Foca pertenecen a Mamifero.
- Pinguino, Albatros, Pato y Ganso pertenecen a Ave.

## Relación con Python
En el archivo `hechos_animales.py` se utilizaron:
- Diccionarios para almacenar la información de los animales.
- Tuplas para representar hechos.
- Predicados para realizar consultas sobre la base de conocimiento.
