# 📚 Galactic Library – Sistema Intergaláctico de Gestión

Galactic Library es una aplicación de consola en **Python** diseñada para gestionar visitantes intergalácticos y artefactos recuperados durante misiones espaciales. El proyecto integra autenticación, manejo de archivos CSV y uso de colecciones como listas, diccionarios, tuplas y sets.

---

## 🚀 Características Principales

### 🔐 Módulo de Login (Administrador)
- Acceso protegido mediante archivo `admin_access.csv`
- Verificación de **usuario, contraseña y rol**
- Reintentos gestionados con **función recursiva**
- Bloqueo del sistema tras agotar intentos

---

## 👽 Módulo de Visitantes
Permite administrar visitantes humanos, androides o de otras especies.

### Funciones:
- **Registrar visitante**
  - ID único (validado con *set*)
  - Nombre, especie, planeta de origen
  - Estado: *active / retired*
  - Guardado en `visitors.csv`
- **Listar visitantes** (como tuplas)
- **Buscar por ID**
- **Actualizar estado**
- **Eliminar visitante** (fila completa)
- **Estadísticas**
  - Total de visitantes
  - Visitantes por especie
  - Activos vs retirados  
  *(Uso obligatorio de diccionarios y sets)*

---

## 🛸 Módulo de Artefactos Recuperados
Maneja objetos recolectados durante misiones espaciales.

### Funciones:
- **Registrar artefacto**
- **Listar artefactos**
- **Buscar por código**
- **Clasificar por rareza** (uso de `**kwargs`)
- **Mostrar estadísticas**
- **Eliminar artefacto**

Datos almacenados en `artefacts.csv`.

---

## 💾 Persistencia con CSV

El sistema utiliza un módulo `storage.py` que incluye:
- Lectura de CSV → diccionarios
- Escritura de CSV → sobrescritura ordenada
- Guardado incremental
- Prevención de pérdida de datos

Rutas y archivos gestionados automáticamente.

---

## 📂 Estructura Recomendada del Proyecto
galactic_library/
│── main.py
│── auth.py
│── storage.py
│── visitors.py
│── artefacts.py
│── utils.py
│── admin_access.csv
│── visitors.csv
│── artefacts.csv

## 🧠 Conceptos Técnicos Aplicados

- Funciones con `*args` y `**kwargs`
- Funciones recursivas
- Manejo de archivos CSV
- Listas, diccionarios, tuplas, sets
- Validaciones de entrada
- Modularización del código
- Menús interactivos

# 👨‍💻 Developed By:
## Faiber Camacho
