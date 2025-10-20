# Informe de Implementación — Problema del Riego Óptimo (Programación Dinámica)

## 0. Resumen

Este documento explica la implementación de la técnica de programación dinámica para resolver el problema del riego óptimo. Se adapta el formato del informe de fuerza bruta para documentar el diseño, formulación, análisis de complejidad, un ejemplo, y las instrucciones para ejecutar los tests y el código en este repositorio.

## 1. Descripción del problema

El problema del riego óptimo consiste en determinar el orden en que deben regarse los tablones de una finca utilizando un único sistema de riego, de modo que se minimice el sufrimiento de los cultivos por falta de agua.

Cada tablón tiene tres características:

- $ts_i$: tiempo máximo que puede sobrevivir sin riego (días),
- $tr_i$: tiempo que tarda en regarse (días),
- $p_i$: prioridad (entero entre 1 y 4, siendo 4 la más alta).

Se riega de forma secuencial y no hay costo por mover el sistema de riego.

## 2. Enfoque dinámico (idea general)

La programación dinámica busca explotar subproblemas solapados y una estructura óptima de subproblemas para reducir el tiempo de cómputo respecto a la fuerza bruta. Para este problema se puede construir una DP indexada por subconjuntos (bitmask) donde el estado representa qué tablones ya fueron regados.

### Definición de estados

- Estado: `dp[mask]` = costo mínimo acumulado al regar exactamente el conjunto de tablones marcado en `mask` (bits 1 = ya regado).
- `mask` varía de `0` (ningún tablón regado) a `2^n - 1` (todos regados).

Además necesitamos conocer el tiempo transcurrido al llegar a ese estado. Podemos reconstruir el tiempo si además guardamos `time[mask]` o derivarlo acumulando los `tr` de los tablones en `mask`.

Sea `T(mask) = sum_{i in mask} tr_i` el tiempo total usado para regar los tablones en `mask`.

### Transición

Para cada estado `mask` y para cada tablón `j` que no esté en `mask`, consideramos regarlo a continuación -> nuevo estado `mask' = mask | (1 << j)`.

- tiempo_inicio para `j` = `T(mask)`
- tiempo_fin para `j` = `T(mask) + tr_j`
- penalización por `j` = `p_j * max(0, tiempo_fin - ts_j)`

Entonces:

dp[mask'] = min(dp[mask'] , dp[mask] + penalizacion_j)

Inicialización: `dp[0] = 0`.

Respuesta: `dp[(1<<n)-1]` y reconstrucción de la permutación óptima guardando predecesores.

## 3. Contrato mínimo de la implementación (inputs/outputs)

- Entrada: archivo de texto con formato:
  - Primera línea: `n` (# tablones)
  - Siguientes `n` líneas: `ts,tr,p` separados por comas
- Salida: par `(orden, costo)` donde `orden` es una lista de índices (0..n-1) con el orden de riego y `costo` es el costo total (int). También se escribe un archivo de salida con el costo en la primera línea y luego los índices en líneas posteriores (como exige la suite de tests).
- Error modes: si `input_file` o `output_file` no se proveen en entornos sin GUI, la función devuelve `None, None` o persiste en pedir diálogo; la implementación en `main/src/dinamica.py` evita errores de import en entornos sin tkinter.

## 4. Complejidad y casos límite

- Estados: `2^n`.
- Para cada estado se prueban `O(n)` transiciones (escoger el siguiente tablón).
- Tiempo: `O(n * 2^n)`.
- Espacio: `O(2^n)` para `dp` y `O(2^n)` para predecesores (posible `O(n * 2^n)` si guardamos más datos).

Casos límite/edge cases:
- `n = 0` -> devolver `([], 0)`
- Valores grandes de `n` (≥20) se vuelven impracticables en tiempo/espacio.
- Datos mal formateados -> excepciones controladas de parsing.

## 5. Ejemplo ilustrativo

Usamos el ejemplo pequeño (5 tablones) adaptado:

Finca:

```
T[0] = 10,3,4
T[1] = 5,3,3
T[2] = 2,2,1
T[3] = 8,1,1
T[4] = 6,4,2
```

Aplicando una DP por subconjuntos obtendremos (en este caso) la misma solución óptima que la fuerza bruta, pero con menor trabajo si se reusa información entre estados.

## 6. Implementación (resumen de las funciones relevantes)

A continuación se describe el comportamiento adaptado de lo que hay en `main/src/dinamica.py`:

- `roD(input_file=None, output_file=None)`
  - Lee la finca desde `input_file` (o pide diálogo si no se provee y tkinter está disponible).
  - Ejecuta la rutina de programación dinámica por subconjuntos.
  - Escribe el archivo `output_file` con el formato esperado por los tests.
  - Devuelve `(orden_lista, costo_total)`.

- Notas sobre el archivo `main/src/dinamica.py` actual:
  - Importa `tkinter` solo cuando es necesario (evita romper en CI sin GUI).
  - Usa una estructura de heap en su versión actual (esto corresponde más a una heurística voraz que a la DP). Si se desea la DP exacta, se puede reimplementar la parte interior por la versión de bitmask `dp`.

### Esqueleto de la DP (pseudocódigo)

```
read finca -> lista finca de n tuplas (ts, tr, p)
compute sum_tr_mask quickly (precompute sum_tr for masks or compute on the fly)
initialize dp[0] = 0 and dp[mask>0] = inf
initialize parent[mask] = -1
for mask in 0 .. (1<<n)-1:
    tiempo = sum_tr(mask)
    for j in 0..n-1:
        if bit j not in mask:
            mask2 = mask | (1<<j)
            penal = p_j * max(0, (tiempo + tr_j) - ts_j)
            if dp[mask] + penal < dp[mask2]:
                dp[mask2] = dp[mask] + penal
                parent[mask2] = j
reconstruct orden from parent
return orden, dp[(1<<n)-1]
```

## 7. Diagrama de flujo

```mermaid
flowchart TD
  A[Inicio] --> B[Leer archivo]
  B --> C[Inicializar dp y parent]
  C --> D[Iterar máscaras 0..2^n-1]
  D --> E[Calcular tiempo acumulado T(mask)]
  E --> F[Probar transiciones para cada j no en mask]
  F --> G[Actualizar dp y parent]
  G --> H[mask siguiente]
  H --> I[Reconstruir orden y escribir archivo]
  I --> J[Fin]
```

## 8. Verificación y pruebas en este repositorio

- Tests: `main/tests/dinamica_test.py` aplica las siguientes verificaciones:
  - Existen los archivos de entrada `entrada_juguete.txt`, `entrada_pequena.txt`, `entrada_mediana.txt`.
  - Para cada archivo, llama `roD(input, output)` y verifica:
    - El retorno `orden` es una lista y `costo` es un entero.
    - El archivo de salida fue creado y contiene en su primera línea el costo (número entero) y luego una lista de índices (uno por línea) que forman una permutación válida `0..n-1`.

- Cómo ejecutar (Windows PowerShell):

```powershell
# desde la raíz del repositorio
python -m pip install pytest
pytest -q main/tests/dinamica_test.py::test_roD_funciona_con_FILES -q
```

Nota: si no tiene `pytest` instalado, instálelo con `python -m pip install pytest`.

## 9. Resultado de la verificación local (esta sesión)

- Observación: al ejecutar `pytest` en el entorno de esta sesión, `pytest` no estaba disponible. Esto se documenta y se indica cómo ejecutar localmente.
- Se aplicó una mejora en `main/src/dinamica.py` para evitar errores de import al importar el módulo en entornos sin GUI (mover import de `tkinter` al interior de la función y manejar su ausencia).

## 10. Recomendaciones y mejoras futuras

- Implementar la versión exacta por programación dinámica (bitmask) dentro de `main/src/dinamica.py` o en `main/src/dinamica_dp.py` y añadir tests que validen resultados contra la fuerza bruta en instancias pequeñas.
- Añadir pruebas unitarias adicionales que validen casos límite (n=0, n=1, instancias con todos los `p` iguales, etc.).
- Incluir un script `benchmarks/` para comparar tiempos entre fuerza bruta, voraz y dinámica en instancias pequeñas/medias.
- Documentar dependencia y pasos de CI en `.github/workflows`.

## 11. Conclusión

La técnica de programación dinámica por subconjuntos ofrece una solución exacta con complejidad O(n * 2^n) que es mucho más eficiente que la fuerza bruta para casos moderados (p. ej. hasta n≈20 dependiendo de recursos). En este repositorio ya existe una implementación que realiza una ordenación/heurística con heap; el siguiente paso es completar la implementación DP para comparar y añadir medidas empíricas.

---

Archivo generado automáticamente por la revisión de implementación del equipo. Ajuste ejemplos y resultados experimentales con las ejecuciones locales.
