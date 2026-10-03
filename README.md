# AI_Project

Actividad formativa de la asignatura **Inteligencia Artificial basada en prompt**.  
El proyecto implementa un sistema de recomendación sencillo en Python y sirve como práctica de uso de GitHub, Visual Studio Code y GitHub Copilot.

## Objetivo

Construir un programa que recomiende productos a partir de los intereses escritos por el usuario.  
El sistema compara palabras clave de las preferencias con la categoría y las etiquetas de cada producto, asigna un puntaje y muestra las coincidencias más relevantes.

## Archivos del proyecto

- `recommendation_system.py`: programa principal.
- `products.csv`: datos de ejemplo utilizados por el recomendador.
- `requirements.txt`: dependencias del proyecto.
- `.gitignore`: archivos que Git no debe versionar.

## Cómo ejecutar

1. Tener Python 3 instalado.
2. Clonar este repositorio o descargarlo.
3. Abrir una terminal en la carpeta del proyecto.
4. Ejecutar:

```bash
python recommendation_system.py
```

5. Escribir intereses separados por comas. Ejemplo:

```text
tecnologia, musica, fotografia
```

El programa mostrará los productos con mejor coincidencia.

## Funcionamiento

1. Se cargan los productos desde `products.csv`.
2. Se normalizan los intereses ingresados por el usuario.
3. Se comparan los intereses con la categoría, nombre y etiquetas de cada producto.
4. Cada coincidencia suma puntaje.
5. Se ordenan los resultados de mayor a menor puntaje.
6. Se muestran las mejores recomendaciones y una breve explicación.

## Ejemplo

```text
Ingresa tus intereses separados por comas: fotografia, tecnologia
¿Cuántas recomendaciones deseas ver? 3

Recomendaciones:
1. Smartphone Nova X - Puntaje: 4
   Coincidencias: fotografia, tecnologia
2. Cámara PixelPro - Puntaje: 3
   Coincidencias: fotografia
3. Audífonos SoundBeat - Puntaje: 1
   Coincidencias: tecnologia
```

## Uso de GitHub Copilot

La pauta de la actividad solicita utilizar **GitHub Copilot dentro de Visual Studio Code**.  
Antes de entregar, se debe realizar al menos una interacción real con Copilot y registrar evidencia del proceso.

### Paso breve recomendado para la evidencia

Abrir `recommendation_system.py` en VS Code y pedir a Copilot, por ejemplo:

> Agrega una función que explique por qué cada producto fue recomendado según los intereses del usuario.

Luego revisar la sugerencia, aceptarla si corresponde, ejecutar nuevamente el programa y realizar el commit del cambio.

## Evidencias sugeridas para documentar

Para la entrega conviene conservar capturas de:

1. Repositorio creado en GitHub.
2. Proyecto abierto en Visual Studio Code.
3. Interacción o sugerencia de GitHub Copilot.
4. Ejecución correcta del programa en la terminal.
5. Repositorio actualizado después del commit/push.

## Nota académica

Este repositorio contiene una base funcional del ejercicio. La evidencia de uso de GitHub Copilot debe corresponder a una interacción realizada efectivamente por el estudiante, tal como solicita la actividad.
