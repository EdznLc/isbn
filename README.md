# Validador de ISBN: De lo Básico a lo Robusto (Proyecto Integrador I)

Este repositorio contiene la implementación de un validador de códigos ISBN-10 e ISBN-13 en Python, junto con una suite de pruebas robusta que alcanza el 100% de cobertura de líneas y ramas mediante la integración continua (CI/CD). 

## 1. Métricas de Calidad (Logradas)

Métrica | Meta Mínima (Plan de Pruebas) | Resultado Final
--- | --- | ---
Cobertura de Líneas | ≥ 90% | 100%
Cobertura de Ramas | ≥ 85% | 100%
Estado del CI/CD | Verde | Verde

##  2. Cómo Correr y Verificar Pruebas

Para ejecutar las pruebas y generar el reporte de cobertura localmente, sigue estos pasos:

### 2.1. Instalación de Dependencias

Instala pytest y la librería de cobertura ejecutando:

`pip install pytest pytest-cov`

### 2.2. Ejecutar Pruebas y Cobertura (Localmente)

Ejecuta el siguiente comando en la raíz del repositorio. Esto correrá todos los tests (unidades, propiedades y stubs) y medirá la cobertura sobre el código fuente (src/):

`pytest --cov=src --cov-report=term-missing --cov-report=html`

### 2.3. Ver el Reporte Detallado de Cobertura

La forma más precisa de ver la cobertura de ramas (branches) es a través del artefacto HTML generado por el CI/CD:

1. Ve a la pestaña 'Actions' en este repositorio de GitHub.  
2. Haz clic en la última ejecución exitosa del workflow "CI - Pruebas y Cobertura de ISBN".  
3. Descarga el archivo ZIP etiquetado como `coverage-report-html` en la sección "Artifacts".  
4. Descomprime el archivo y abre `index.html` para ver el reporte detallado del 100% de cobertura de ramas.

##  3. Decisiones y Supuestos (Punto 7)

### Supuestos Clave

1. Los códigos ISBN se ingresan como cadenas de texto (string).  
2. El módulo es puro: no depende de librerías externas, archivos o acceso a internet.  
3. La letra 'X' solo es válida como el último carácter en un ISBN-10.  

### Decisiones de Diseño de Pruebas

Técnica Utilizada | Razón Estratégica
--- | ---
Mock/Stub (@patch) | Se utilizó para aislar la función `detect_isbn` del colaborador `is_valid_isbn10`. Esto permite probar la lógica de flujo (if-elif-else) de `detect_isbn` de manera determinista, sin que el resultado dependa del cálculo complejo del checksum.
Property-Based Testing | Se implementó para verificar la Idempotencia de la función `normalize_isbn`. Esto garantiza que la función mantiene un comportamiento consistente (reglas matemáticas) ante un gran volumen de entradas dinámicas.
CI/CD con Ramas | La configuración del `ci.yml` asegura que el cumplimiento del 100% de cobertura de líneas y ramas se verifique automáticamente en cada cambio de código.
