# 🛡️ Watermark - Generador de DNI Seguro

## 📋 Información del Proyecto

| Campo | Valor |
|-------|-------|
| **Nombre** | watermark_final.py |
| **Lenguaje** | Python 3 |
| **Archivo principal** | `watermark_final.py` |

## 📚 Dependencias

El script usa las siguientes bibliotecas de Python:

- `pypdf` (o `PyPDF2` según la versión instalada)
- `reportlab`

Instalación recomendada:

```bash
python3 -m pip install --user pypdf reportlab
```

Se recomienda Python 3.8+.

---

## 📝 Descripción

`watermark_final.py` aplica una "capa de seguridad" sobre un PDF de entrada (por ejemplo, imagen de un DNI), realizando:

- Censura de la zona MRZ (bloque blanco en la parte inferior).
- Inserción de una marca de agua diagonal (dos líneas de texto) centrada en la página.

Genera un nuevo archivo con el sufijo `_PROTEGIDO.pdf` en el mismo directorio del archivo de entrada.

---

## ⚙️ Uso

El script puede recibír la ruta del PDF como argumento o solicitarla por interacción si no se pasa.

Ejemplos:

```bash
# Usando argumento
python3 watermark_final.py input.pdf

# Ejecutando interactivamente (arrastrar/pegar ruta cuando lo pida)
python3 watermark_final.py
```

Durante la ejecución se solicitan (opcionalmente) las dimensiones del documento en pulgadas y los textos para la marca de agua. Si dejas la entrada vacía, se usan valores por defecto indicados por el programa.

Salida esperada:

```
<nombre_base>_PROTEGIDO.pdf
```

---

## ❗ Comportamiento y errores

- Si el archivo de entrada no existe, el script muestra un mensaje de error y finaliza.
- Si hay un error inesperado (por ejemplo, problemas al leer/escribir o dependencias faltantes), el script imprime un mensaje con la excepción.
- El script no requiere compilación.

---

## ✅ Checklist de Requisitos (sugerido)

- [ ] `watermark_final.py` acepta ruta como argumento
- [ ] Si no hay argumento, solicita la ruta al usuario
- [ ] Verifica existencia del archivo de entrada
- [ ] Genera `*_PROTEGIDO.pdf` con marca de agua y censura MRZ
- [ ] Permite valores por defecto para medidas y texto
- [ ] No deja ficheros temporales abiertos innecesarios

---

## 🧪 Cómo Probar

- Asegúrate de tener instaladas las dependencias (ver arriba).
- Ejecuta con un PDF de una sola página para comprobar visualmente la censura y la marca de agua.

Ejemplo rápido:

```bash
python3 watermark_final.py ejemplo.pdf

# Luego abre 'ejemplo_PROTEGIDO.pdf' con tu visor de PDFs favorito.
```

---

## 📁 Archivos Relacionados

- `watermark_final.py`: Script principal.