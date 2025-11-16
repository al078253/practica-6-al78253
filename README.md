# Práctica 6: Modelado de problemas en Ingeniería Civil

## Introducción
El desarrollo de infraestructura vial requiere un planeamiento detallado de los materiales y costos, así como la evaluación de riesgos geotécnicos asociados a la construcción de pavimentos y terracerías. La correcta estimación de volúmenes, costos y riesgos permite optimizar recursos, minimizar fallas estructurales y asegurar la durabilidad de la vía.

El presente código tiene como objetivo principal **automatizar los cálculos de materiales, costos y riesgos** para distintos tramos de carretera, permitiendo al usuario generar reportes detallados de manera rápida y confiable.

---

## 🎯 Objetivo del Código
El objetivo del proyecto es:

- Calcular de forma automática el **volumen de pavimento y materiales requeridos** para cada tramo de carretera.
- Estimar el **costo económico** de la construcción considerando materiales, mano de obra y maquinaria.
- Analizar los **riesgos geotécnicos** asociados al tipo de suelo y cantidades de materiales.
- Proporcionar un **reporte consolidado** que incluya información por tramo y del proyecto completo.

Este sistema permite al ingeniero civil o proyectista evaluar escenarios, comparar alternativas de pavimentación y optimizar la planificación de la obra.

---

## 📋 Desarrollo del Código

El código está estructurado en **módulos** para facilitar su comprensión, mantenimiento y escalabilidad. Cada módulo aborda un aspecto específico del problema:

1. **Cálculo de materiales (`calcular_materiales`)**  
   Determina el volumen de pavimento y la distribución de cemento, asfalto, grava y acero de refuerzo según el tipo de pavimento y dimensiones del tramo.

2. **Cálculo de costos (`calcular_costos`)**  
   Calcula el costo de materiales, mano de obra y maquinaria, entregando un total por tramo y el acumulado del proyecto.

3. **Evaluación de riesgos geotécnicos (`riesgos_geotecnicos`)**  
   Analiza posibles problemas según el tipo de suelo y las cantidades de materiales, incluyendo riesgos de fisuración, asentamiento, corrosión o licuefacción.

4. **Cálculo de terracería y drenaje (`calcular_terraceria` y `calcular_drenaje`)**  
   Estima los volúmenes de corte y relleno, y la longitud de drenaje necesaria para cada tramo, considerando factores según el tipo de suelo.

5. **Gestión de múltiples tramos**  
   Permite agregar tramos dinámicamente, almacenar su información en estructuras de datos, calcular materiales y costos por tramo y consolidar un reporte final.

6. **Interfaz gráfica**  
   La interfaz con Tkinter permite al usuario:
   - Ingresar dimensiones, tipo de pavimento y tipo de suelo por tramo.
   - Visualizar los tramos agregados en un árbol.
   - Generar reportes detallados directamente en la aplicación.

---

## ✅ Conclusión
El código proporciona una **herramienta integral** para la planificación de carreteras, combinando cálculos geométricos, económicos y geotécnicos en una sola aplicación. Su modularidad permite:

- **Escalabilidad:** agregar más tipos de pavimento o análisis adicionales.
- **Actualización sencilla:** modificar precios y parámetros sin afectar la lógica.
- **Uso práctico:** generación de reportes claros y confiables para la toma de decisiones.

En síntesis, esta herramienta **automatiza y optimiza el diseño preliminar de carreteras**, facilitando un enfoque profesional y seguro en la ingeniería vial.
