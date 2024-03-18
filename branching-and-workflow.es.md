# Estrategia y Flujo de Trabajo de Ramificación en Git

## Estrategia de Ramificación en Git

Este repositorio tendrá ramas para cada tarea con una nomenclatura como esta `tas-<número-de-tarea>-<nombre-de-tarea>`, como en el diagrama a continuación, donde tendremos todas las ramas en el repositorio como una guía visual a través de la estructura del repositorio:

```
└── main 
    ├── tas-12-data-acquisition
    └── tas-34-analysis-and-preprocessing
```


## Guía Paso a Paso

### Clonación del Repositorio o Creación de Codespace
1. **Codespace:**
   1. Una vez en el repositorio, haz clic en el botón verde `Code`
   2. Haz clic en la pestaña de Codespace
   3. Crea o abre un Codespace
2. **Clonación en Local**
   1. Una vez en el repositorio, haz clic en el botón verde `Code`
   2. Selecciona **HTTPS** y copia el enlace
   3. Abre tu terminal, CMD o Powershell
   4. Escribe el comando `git clone` y pega el enlace que copiaste
   5. Presiona Enter

### Configuración del Entorno
1. Una vez en tu Codespace o terminal local, escribe los siguientes comandos en orden
   1. `python -m venv .<nombre-del-entorno>`
   2. Activa el entorno siguiendo la documentación sobre venv de Python relacionada con tu sistema operativo y línea de comandos
   3. `pip install -r requirements.txt`
   4. `code .`

### Creación o Cambio de la Rama de Git
1. Crear Rama
   1. En la rama principal escribe en la terminal `git branch <nombre-de-la-rama>`
2. Cambiar Rama
   1. En cualquier rama escribe en la terminal `git checkout <nombre-de-la-rama>`

### Actualizar el Repositorio con tus Cambios
1. Ejecuta los siguientes comandos en orden
   1. `git add .`
   2. `git commit -m 'Mensaje del Commit'`
   3. `git push origin <nombre-de-la-rama>`

### Notas
* Cada vez que uses el repositorio después de un tiempo, especialmente la rama principal, debes ejecutar el siguiente comando `git pull`


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
