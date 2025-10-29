# REPORTE TÉCNICO: Diseño y Ejecución de Pruebas para un Validador de ISBN

## Alumnos
1. Bueno Cao Romero Erik Gabriel  
2. Guillen López José Alberto  
3. Jimenez Delgado Luis Hector  
4. Lomas Corral Edson  
5. Meraz Sida Fernando  

---

## I. Plan de Pruebas (Resumen)
El objetivo fue comprobar que el módulo `isbn.py` funciona correctamente al validar códigos ISBN-10 e ISBN-13, garantizando que las funciones sean confiables y manejen entradas incorrectas.

### 1. Supuestos y Riesgos

**Supuestos**:

- Los ISBN se ingresan como texto.  
- No se usan librerías externas.  
- La letra 'X' solo es válida al final de un ISBN-10.

**Riesgos**:

| Riesgo | Efecto | Prevención |
|--------|--------|------------|
| Error en la fórmula del checksum | Validaciones incorrectas | Revisar fórmula antes de pruebas |
| Casos límite no contemplados (entradas vacías o con símbolos) | Resultados inesperados | Incluir pruebas de error |

---

### 2. Particiones de Equivalencia y Fronteras

| Tipo | Categoría / Caso Límite |
|------|-------------------------|
| ISBN-10 | Válidos con dígitos y con ‘X’ final; Inválidos por checksum y por carácter |
| ISBN-13 | Válidos; Inválidos por checksum y por carácter |
| Fronteras | Longitudes 9/11 (ISBN-10) y 12/14 (ISBN-13); Cadena vacía |

---

## II. Trazabilidad Requisito → Caso → Test

| Requisito / Caso (Plan) | Tipo de Prueba | Función de Prueba (Archivo) |
|-------------------------|----------------|----------------------------|
| ISBN-10 Válido con 'X' | Partición de Equivalencia | `test_isbn10_valido` (`test_happy_paths.py`) |
| ISBN-13 Inválido por Checksum | Partición de Equivalencia | `test_isbn13_invalido` (`test_unhappy_paths.py`) |
| Frontera: Cadena Vacía | Análisis de Fronteras | `test_detect_invalid_general` (`test_unhappy_paths.py`) |
| Inválido por Carácter (no 'X') | Partición de Equivalencia | `test_normalize_caracter_ilegal` (`test_unhappy_paths.py`) |
| Requisito: Doble de Prueba | Mock/Stub | `test_detect_isbn_stub_forces_isbn10_pass` (`test_stub.py`) |
| Requisito: Propiedad de Normalización | Property-Based Test | `test_idempotencia` (`test_properties.py`) |

---

## III. Evidencias de Ejecución y CI/CD

### 1. Ejecución de CI/CD y Estado
- El workflow de **Integración Continua** fue configurado en **GitHub Actions** para ejecutarse automáticamente en cada push.  
- El flujo de trabajo finalizó exitosamente, demostrando que el código y las pruebas son estables y pasan en un ambiente limpio.

### 2. Cobertura Final de Caja Blanca

| Métrica | Meta Mínima | Resultado Final |
|---------|------------|----------------|
| Cobertura de Líneas | ≥ 90% | 100% |
| Cobertura de Ramas (Branches) | ≥ 85% | 100% |

---

## IV. Discusión Crítica

### 1. Análisis de Metas y Gaps Resueltos
El logro del **100% de cobertura** de líneas y ramas confirma que todos los caminos de ejecución y puntos de decisión dentro de `isbn.py` fueron verificados. Esto valida el diseño de casos de **Caja Blanca**, ya que se logró cubrir las rutas que inicialmente estaban faltantes (líneas 7, 36 y 40).

### 2. Justificación de Pruebas Avanzadas

- **Doble de Prueba (Mock/Stub):**  
  Se implementó un Mock (@patch) para la función `is_valid_isbn10`. Esto fue crucial para aislar la función `detect_isbn` (SUT) y probar su lógica de decisión (`if-elif-else`) de manera determinista, sin depender de que la fórmula de checksum se ejecutara correctamente.

- **Property-Based Testing:**  
  Se utilizaron dos propiedades: **Idempotencia** y **Estabilidad ante formato**. Esto demostró la robustez de `normalize_isbn`, asegurando que el comportamiento de la función es consistente bajo una amplia gama de entradas, y no solo para los casos estáticos definidos.

### 3. Conclusión
El proceso de diseño y ejecución de pruebas, culminado con la automatización en **CI/CD**, garantiza que el módulo validador de ISBN:

- Cumple con los requisitos funcionales (validación de ISBN-10 y 13).  
- Es robusto y verificable.  
- Es mantenible bajo estándares de calidad (100% de cobertura).

