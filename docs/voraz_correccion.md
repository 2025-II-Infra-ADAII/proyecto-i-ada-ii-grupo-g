# Informe de Corrección – Estrategia Voraz (roV)

## 1. Definición de la función

**Función:**  
f : Entrada → Salida

**Descripción general:**  
El algoritmo voraz (roV) busca determinar un **orden de riego de los tablones** que minimice el costo total de penalización acumulada, **tomando decisiones locales óptimas** en cada paso.  

En este caso, la estrategia selecciona los tablones **en orden descendente de la razón p/tr**, es decir, **priorizando los tablones con mayor penalización relativa por unidad de tiempo**.

---

## 2. Parámetros y estructuras

**Entrada:**  
- Archivo de texto con el siguiente formato:  
  - Primera línea: número de tablones `n`.  
  - Siguientes líneas: `ts, tr, p` para cada tablón, donde:  
    - `ts` = tiempo de inicio deseado  
    - `tr` = tiempo de riego  
    - `p` = penalización

**Salida:**  
- Archivo con:  
  - Primera línea: costo total obtenido.  
  - Siguientes líneas: orden de riego (índices de tablones).

---

## 3. Procedimiento del algoritmo

**Idea central:**  
Seleccionar primero los tablones que generan **mayor pérdida por unidad de tiempo** si se retrasan.  

**Pseudocódigo resumido:**

```text
roV(input_file):
    leer n y lista de tablones (ts, tr, p)
    para cada tablón calcular clave = p / tr
    ordenar los tablones por clave descendente

    tiempo_actual = 0
    costo_total = 0
    para cada tablón en el orden:
        penalización = max(0, (tiempo_actual + tr) - ts)
        costo_total += p * penalización
        tiempo_actual += tr

    devolver orden, costo_total
```

**Notación formal:**  
Sea \( T = \{1, 2, ..., n\} \) el conjunto de tablones.  
Se busca minimizar:

\(
C = \sum_{i=1}^{n} p_i \cdot \max(0, (t_{acum}(i) + tr_i - ts_i))
\)

donde \( t_{acum}(i) \) es el tiempo acumulado hasta el tablón i.

---

## 4. Caso base y ejemplo

**Caso base:**  
Cuando `n = 1`, el algoritmo simplemente calcula la penalización del único tablón:

\(
C = p_1 \cdot \max(0, tr_1 - ts_1)
\)

**Ejemplo (entrada_juguete.txt):**  

```
3
4,2,6
3,1,4
6,3,5
```

**Cálculo paso a paso:**  
1. Se calcula la clave p/tr: [3.0, 4.0, 1.66]  
2. Orden descendente por clave → índices [1, 0, 2]  
3. Evaluando penalizaciones acumuladas:  
   - Tablón 1: penalización = 0  
   - Tablón 0: penalización = 0  
   - Tablón 2: penalización = 4  
   - Costo total = 20  

**Resultado:**  
Orden óptimo (heurístico): [1, 0, 2]  
Costo total aproximado: 20

---

## 5. Complejidad

### 5.1 Temporal
- Ordenamiento: \( O(n \log n) \)
- Cálculo del costo: \( O(n) \)
- **Complejidad total:** \( O(n \log n) \)

### 5.2 Espacial
- Se almacenan las tuplas de tablones y el orden resultante: \( O(n) \)
- **Complejidad espacial:** \( O(n) \)

---

## 6. Observaciones finales

- Este enfoque **no garantiza la solución óptima global**, pero reduce drásticamente el tiempo de ejecución frente a la fuerza bruta o la programación dinámica.  
- Es ideal para **instancias grandes (n > 20)** donde los otros métodos se vuelven inviables.  
- En la práctica, su desempeño suele ser **muy cercano al óptimo**, especialmente cuando los valores de penalización y tiempos están balanceados.

---

**Conclusión:**  
El algoritmo voraz para el riego implementa una estrategia eficiente de decisión local, ordenando los tablones por su impacto relativo de penalización. Su simplicidad y velocidad lo hacen adecuado para problemas de gran escala, aunque sacrifica exactitud frente a los métodos exhaustivos o dinámicos.
