# Estrategia y Flujo de Trabajo de Ramificación en Git

## Estrategia de Ramificación en Git

1. **Rama Principal (main):**
   * Esta rama contendrá el código estable y listo para producción.
   * El código de esta rama debería ser desplegable en cualquier momento.
   * Solo se fusiona en esta rama desde ramas de características después de pruebas exhaustivas y revisión de código.

2. **Rama de Desarrollo (dev):**
   * Esta rama sirve como la rama de integración para el trabajo en curso.
   * Los miembros del equipo fusionan sus ramas de características en esta rama para pruebas de integración.
   * Se incorporan regularmente cambios desde la rama principal para asegurarse de que la rama de desarrollo esté actualizada con la última versión estable.
   * Todas las ramas de características deben derivarse y fusionarse de nuevo en dev.

3. **Ramas de Características:**
   * Cada característica o tarea debe tener su propia rama dedicada.
   * Los miembros del equipo trabajan en ramas separadas para diferentes características o tareas.
   * Los nombres de las ramas deben ser descriptivos de la característica o tarea en la que se está trabajando (por ejemplo, feature/data-acquisition, feature/model-building).
   * Una vez que una característica está completa, se somete a revisión de código y pruebas antes de fusionarse en la rama dev.

4. **Ramas de Trabajo Individual (Opcional):**
   * Si los miembros del equipo están trabajando en tareas individuales dentro de una característica más grande, pueden crear ramas personales basadas en la rama de características.
   * Estas ramas tienen una vida corta y deben fusionarse de nuevo en la rama de características correspondiente una vez que se complete la tarea individual.

5. **Ramas de Lanzamiento (Opcional):**
   * Si es necesario, se puede crear una rama de lanzamiento desde la rama dev para pruebas finales y preparación antes del despliegue.
   * No se agregan nuevas características a las ramas de lanzamiento; son únicamente para correcciones de errores y preparación para el despliegue.
   * Una vez que el lanzamiento esté listo, se puede fusionar la rama de lanzamiento en la rama principal para el despliegue.

## Flujo de Trabajo:

**1. Planificación del Sprint:**
   * Al comienzo de cada sprint, decida las características o tareas en las que se trabajará.
   * Asigne a los miembros del equipo para trabajar en tareas específicas.

**2. Ramificación:**
   * Cada miembro del equipo crea una rama de característica basada en la tarea en la que están trabajando.
   * Trabaje de forma independiente en las tareas asignadas dentro de las ramas de características.

**3. Integración Continua:**
   * Fusiona regularmente cambios desde la rama dev en las ramas de características para asegurar la integración y evitar conflictos.
   * La integración continua y las pruebas deben realizarse en la rama dev.

**4. Revisión de Código:**
   * Antes de fusionarse en la rama dev, todos los cambios de código deben pasar por una revisión exhaustiva de código por otro miembro del equipo.

**5. Fusión:**
   * Una vez que una característica está completa y ha pasado la revisión de código y las pruebas, se fusiona en la rama dev.

**6. Pruebas:**
   * Se deben realizar pruebas de integración en la rama dev para asegurar que todas las características funcionen juntas sin problemas.

**7. Lanzamiento:**
   * Si es necesario, cree una rama de lanzamiento desde la rama dev para pruebas finales y preparación.
   * Fusiona la rama de lanzamiento en la rama principal para el despliegue después de pruebas exhaustivas.

**8. Despliegue:**
   * Despliega el código desde la rama principal al entorno de producción.
   * Siguiendo esta estrategia de ramificación, su equipo puede colaborar efectivamente en el proyecto, gestionar cambios y garantizar un código estable y desplegable en todo momento.
