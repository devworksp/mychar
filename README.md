# Proyecto PPS01: Gestión Segura de Cadenas de Texto

## 1. Información General
*   **Título:** Herramienta de validación y limpieza de caracteres `mychar.py`.
*   **Descripción:** Este software está diseñado para procesar entradas de usuario de forma segura, eliminando espacios innecesarios y gestionando la lógica de cadenas para evitar errores de procesamiento.
*   **Tecnologías utilizadas:** 
    *   Python 3.x
    *   Entorno de desarrollo: Windows PowerShell
    *   Sistema de control de versiones: Git

## 2. Guía de despliegue
Para instalar y ejecutar este programa, siga estos pasos:
1.  Asegúrese de tener Python instalado en su sistema.
2.  Clone o descargue este repositorio en su máquina local.
3.  Abra una terminal (PowerShell o CMD) en la carpeta del proyecto.
4.  Ejecute el script con el siguiente comando:
    ```bash
    python mychar.py
    ```

## 3. Tabla de Trazabilidad
| Fecha | Versión | Descripción de cambios |
| :--- | :--- | :--- |
| 02/05/2026 | v1.0 | Creación del script inicial con lógica de limpieza de espacios. |
| 02/05/2026 | v1.1 | Refuerzo de seguridad en el tratamiento de cadenas y corrección de lógica. |
| 02/05/2026 | v1.2 | Implementación de documentación README.md y cierre de rama de desarrollo. |

## 4. Checklist de Seguridad
Se han tomado las siguientes decisiones técnicas para proteger la integridad del proyecto:
*   **Archivo/Carpeta:** `__pycache__/`
    *   **Acción:** Ignorado / Protegido.
    *   **Razón Técnica:** Contiene archivos de bytecode compilados que son específicos de la máquina local y no deben distribuirse por seguridad y limpieza del repositorio, evitando fugas de información sobre la estructura del sistema.
*   **Gestión de Ramas:** Se utiliza una rama `desarrollo-seguro` para pruebas antes de integrar cambios en `main`, garantizando que la versión estable nunca se vea comprometida por código no verificado.