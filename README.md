# Proyecto Módulo #4 — Gestor Inteligente de Clientes (GIC)

# Enlace a GITHUB
https://github.com/DemWolfXZ/modulo4


Sistema por consola en **Python 3** para gestionar clientes usando **POO** (encapsulación, herencia y polimorfismo), Sistema **CRUD**, **validaciones + excepciones personalizadas**, **importación/exportación CSV**, **reporte TXT** y **registro de actividad en logs**.

---
## 1) Estructura esperada del proyecto

> Importante: estas rutas son **relativas** a la carpeta raíz del proyecto (donde está `main.py`).
Ruta:

```
./
├── main.py
├── modulos/
│   ├── __init__.py
│   ├── cliente.py
│   ├── cliente_regular.py
│   ├── cliente_premium.py
│   ├── cliente_corporativo.py
│   ├── gestor_clientes.py
│   ├── validaciones.py
│   ├── excepciones.py
│   └── archivos.py
├── datos/
│   ├── clientes_entrada.csv
│   └── clientes.csv
├── reportes/
│   └── resumen.txt
└── logs/
    └── app.log
```

---

## 2) ¿Cuales son los archivos lee / crea el sistema?

### Importación (leer)
- El sistema **lee** desde:
  - `datos/clientes_entrada.csv`
- Si no existe, el sistema debe mostrar un mensaje del tipo **“archivo no encontrado”** (se captura `FileNotFoundError`).

### Exportación (crear/escribir)
- El sistema **crea/actualiza**:
  - `datos/clientes.csv`

### Reporte (crear)
- El sistema **crea/actualiza**:
  - `reportes/resumen.txt`

### Log (crear)
- El sistema **crea/actualiza**:
  - `logs/app.log`

---

## 3) Formato requerido del CSV de entrada

El archivo `datos/clientes_entrada.csv` debe tener **exactamente** estas columnas:

```csv
id,nombre,email,telefono,direccion,tipo,extra
```

Valores permitidos para `tipo`:
- `ClienteRegular`
- `ClientePremium`
- `ClienteCorporativo`

El campo `extra` depende del tipo:
- `ClienteRegular` → descuento (ej: `10.5`)
- `ClientePremium` → puntos (ej: `200`)
- `ClienteCorporativo` → empresa (ej: `Empresa X SPA`)

---

## 4) Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto (la misma donde está `main.py`).
2. Ejecuta:

```bash
python main.py
```

---

## 5) Menú (interfaz por consola)

El sistema funciona con un menú por consola que permite:
- Agregar cliente
- Listar clientes
- Buscar cliente por ID
- Actualizar cliente
- Eliminar cliente
- Exportar clientes a `datos/clientes.csv`
- Importar clientes desde `datos/clientes_entrada.csv`
- Generar reporte en `reportes/resumen.txt`

---

## 6) Entregables solicitados por la prueba

1. **Código fuente**:  proyecto con estructura modular y comentarios.
2. **Documentación técnica**:  descripción del sistema, estructuras de datos y funcionalidades.
3. **Archivo de prueba**: datos de entrada y salida generados por el sistema (CSV/TXT).
4. **Informe de validación**: capturas y análisis del proceso.
5. **Presentación final**: descripción del proyecto y tecnologías.

---

## 7) Archivos de documentación incluidos (entrega)

- `Documentacion_Tecnica_GIC.md`
- `Informe_Validacion_GIC.md`
- `Presentacion_Final_GIC.pptx`
- `Checklist_Evidencia_GIC.txt` (apoyo para reunir evidencia)

