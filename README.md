# 🛡️ Watermark — Generador de DNI Seguro

Breve herramienta en Python para aplicar una capa de seguridad visual a PDFs de documentos tipo DNI: censura de la zona MRZ (Machine Readable Zone) y marcas de agua diagonales personalizables.

---

**Descripción**
- **Proyecto:** Añade una capa de protección visual a documentos escaneados (por ejemplo, DNI/carnés) usando `reportlab` para generar la capa y `pypdf` para fusionarla con el PDF original.
- **Lenguaje:** Python
- **Archivo principal:** `watermark_final.py`

**Qué hace**
- Crea un rectángulo blanco en la parte inferior del documento para cubrir la MRZ (zona legible por máquinas).
- Añade dos líneas de marca de agua diagonales (rotadas 45°) centradas en la página.
- Fusiona la capa generada con el PDF original y guarda una nueva copia con sufijo `_PROTEGIDO.pdf`.

---

**Dependencias**
- `pypdf` (antes `PyPDF2`): manipulación y fusión de PDFs.
- `reportlab`: generación de la capa de marca de agua y elementos gráficos.

Instalación rápida (recomendado usar un virtualenv):

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install pypdf reportlab
```

---

**Uso**

Modo interactivo (recomendado):

```bash
python watermark_final.py path/al/documento.pdf
```

Si no pasas la ruta como argumento, el script preguntará interactívamente la ruta y parámetros:
- Ancho y alto en pulgadas (valores por defecto sugeridos: `2.29` x `1.39`).
- Texto para las dos líneas de la marca de agua (si no se introduce, la primera línea por defecto será `COPIA DE SEGURIDAD`).

Salida:
- Se genera un archivo con el mismo nombre que el original más el sufijo `_PROTEGIDO.pdf` en la misma carpeta.

Ejemplo rápido:

```bash
python watermark_final.py ./mi_dni.pdf
# O abrir el script sin argumentos y pegar la ruta cuando pida
```

---

**Cómo funciona (resumen técnico)**
- El script calcula el tamaño en puntos (pts) a partir de las medidas en pulgadas (1 pulgada = 72 pts).
- Con `reportlab` genera una página en memoria que contiene:
	- Un rectángulo blanco en la parte inferior para cubrir la MRZ.
	- Texto gris semitransparente rotado 45° y centrado como marca de agua.
- Con `pypdf` se fusiona la capa con cada página del PDF original.

---

**Posibles aplicaciones en el mundo real**
- **Protección de privacidad:** Redacción de datos sensibles (MRZ) antes de compartir documentos para trámites o auditorías.
- **Control de versiones / Copias de seguridad:** Añadir marcas de agua que indiquen "COPIA" o "MUESTRA" para evitar usos indebidos.
- **Flujo documental en empresas y administraciones:** Generar copias protegidas para uso interno sin exponer datos legibles por máquinas.
- **Entregas a terceros/partners:** Prevenir extracción automática (por OCR/MRZ) al compartir copias de documentos.
- **Entrenamiento de modelos y datasets:** Preparar copias de documentos con datos censurados para entrenar modelos sin exponer información personal.

---

**Responsabilidad y consideraciones legales**
- Este proyecto modifica visualmente documentos PDF; no garantiza anonimización completa contra técnicas avanzadas (por ejemplo, reconstrucción de imagen).
- No uses esta herramienta para ocultar fraude o manipular documentos con fines ilegales.
- Revisa la normativa local sobre protección de datos (GDPR/LPD) antes de almacenar o compartir copias.