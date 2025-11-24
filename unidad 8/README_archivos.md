
# Práctica - Programación 1 - Archivos

Este proyecto contiene la solución completa de la práctica sobre manejo de archivos en Python.

## Funcionalidades implementadas

### 1. Crear archivo inicial
Si `productos.txt` no existe, se crea automáticamente con 3 productos precargados.

### 2. Leer y mostrar productos
Se leen las líneas del archivo, se convierten en diccionarios y se muestran con formato legible.

### 3. Agregar productos desde teclado
El usuario puede ingresar nombre, precio y cantidad, que se agregan al archivo sin borrar contenido previo.

### 4. Cargar productos en una lista de diccionarios
Se genera una lista:
```python
[
  {"nombre": "...", "precio": ..., "cantidad": ...},
  ...
]
```

### 5. Buscar producto por nombre
Se solicita al usuario un nombre y se muestran sus datos si existe, o se indica error.

### 6. Guardar productos actualizados
Se sobrescribe el archivo con todos los productos presentes en la lista final.

## Ejecución
En consola:

```bash
python archivos_practica.py
```

## Estructura del archivo generado
```
nombre,precio,cantidad
Lapicera,120.5,30
```

## Autor
Generado automáticamente según el práctico enviado.
