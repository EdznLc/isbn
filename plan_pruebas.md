# Plan de Pruebas - módulo isbn.py

## 1. Objetivo
Comprobar que el módulo isbn.py funciona correctamente al validar códigos ISBN-10 e ISBN-13, asegurando que detecta correctamente los números válidos e inválidos, además de garantizar que las funciones sean confiables, manejen entradas incorrectas y cumplan con las reglas de ISBN.

## 2. Alcance
Las pruebas verificarán que el programa:

- Limpie y valide correctamente el formato del texto.
- Detecte si un código es ISBN-10, ISBN-13 o inválido.
- Funcione con distintos casos válidos e inválidos.
- Funcione con diferentes longitudes y caracteres no permitidos.
- Permita el uso de la letra 'X' al final en ISBN-10.
- Funcione con códigos sin guiones o espacios.

## 3. Supuestos

- Los ISBN se ingresan como texto.
- No se usan librerías externas.
- El módulo no depende de archivos ni internet.
- La letra 'X' solo es válida al final de un ISBN-10.

## 4. Riesgos

| Riesgo | Efecto | Prevención |
|--------|--------|------------|
| Error en la fórmula del checksum | Validaciones incorrectas | Revisar fórmula antes de pruebas |
| Casos no contemplados (entradas vacías o con símbolos) | Resultados inesperados | Incluir pruebas de error |
| Errores de formato no detectados | Códigos con guiones o símbolos pasan como válidos | Usar normalize_isbn para limpiar y validar |

## 5. Particiones de equivalencia

### ISBN-10

| Tipo | Ejemplos |
|------|----------|
| Válidos con dígitos | 0306406152, 0471958697 |
| Válidos con ‘X’ final | 0-8044-2957-X, 156881111X |
| Inválidos por checksum | 0306406153, 0471958698 |
| Inválidos por longitud | 030640615, 03064061522 |
| Inválidos por carácter | 03A6406152, 03064@6152 |

### ISBN-13

| Tipo | Ejemplos |
|------|----------|
| Válidos | 9780306406157, 9783161484100 |
| Inválidos por checksum | 9780306406158, 9783161484101 |
| Inválidos por longitud | 978030640615, 97803064061570 |
| Inválidos por carácter | 97803A6406157, 9780306406@57 |

## 6. Análisis de fronteras

| Tipo | Casos límite |
|------|--------------|
| ISBN-10 | Longitud 9 (inválido), 10 (válido), 11 (inválido) |
| ISBN-13 | Longitud 12 (inválido), 13 (válido), 14 (inválido) |
| General | Cadena vacía, espacios y guiones múltiples |

## 7. Métricas objetivo

| Métrica | Meta mínima |
|---------|------------|
| Cobertura de líneas | ≥ 90% |
| Cobertura de ramas (branches) | ≥ 85% |
| Casos totales ejecutados | 100% exitosos |
| Casos de error controlado | Todos detectados correctamente |
