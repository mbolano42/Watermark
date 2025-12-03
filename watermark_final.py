import io
import sys
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

def crear_capa_seguridad(output_pdf, ancho_pts, alto_pts, t1, t2):
    c = canvas.Canvas(output_pdf, pagesize=(ancho_pts, alto_pts))
    
    # --- 1. CENSURA (Bloqueo visual de datos MRZ) ---
    altura_mrz = alto_pts * 0.22 
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.white)
    c.rect(0, 0, ancho_pts, altura_mrz, fill=1, stroke=1)
    
    # --- 2. MARCA DE AGUA ---
    c.translate(ancho_pts / 2, alto_pts / 2)
    c.rotate(45)
    
    tamano_letra = ancho_pts / 12
    if tamano_letra < 8: tamano_letra = 8 
    
    c.setFillColor(colors.grey, alpha=0.4) 
    c.setFont("Helvetica-Bold", tamano_letra)
    
    separacion = tamano_letra * 0.7
    
    c.drawCentredString(0, separacion, t1)
    c.drawCentredString(0, -separacion, t2)
    
    c.save()

def procesar_pdf(archivo_entrada, ancho_in, alto_in, texto1, texto2):
    nombre_base = os.path.splitext(archivo_entrada)[0]
    archivo_salida = f"{nombre_base}_PROTEGIDO.pdf"
    
    ancho_pts = ancho_in * 72
    alto_pts = alto_in * 72
    
    packet = io.BytesIO()
    crear_capa_seguridad(packet, ancho_pts, alto_pts, texto1, texto2)
    packet.seek(0)
    
    capa_seguridad = PdfReader(packet)
    original = PdfReader(archivo_entrada)
    writer = PdfWriter()
    
    for page in original.pages:
        page.merge_page(capa_seguridad.pages[0])
        writer.add_page(page)
        
    with open(archivo_salida, "wb") as f:
        writer.write(f)
    
    return archivo_salida

# --- BLOQUE PRINCIPAL CORREGIDO ---
if __name__ == "__main__":
    print("\n--- 🛡️ GENERADOR DE DNI SEGURO 🛡️ ---")
    
    # 1. OBTENCIÓN Y LIMPIEZA DE LA RUTA
    archivo_origen = ""
    
    if len(sys.argv) > 1:
        archivo_origen = sys.argv[1]
    else:
        raw_input = input("📂 Arrastra el PDF aquí o escribe su nombre: ")
        # --- AQUÍ ESTÁ LA CORRECCIÓN ---
        # Quitamos espacios, comillas dobles (") y comillas simples (')
        archivo_origen = raw_input.strip().strip('"').strip("'").strip()

    # Verificamos que existe
    if not os.path.exists(archivo_origen):
        print(f"\n❌ Error: No encuentro el archivo.")
        print(f"Ruta que estoy intentando leer: {archivo_origen}")
        print("Asegúrate de no haber borrado caracteres al pegar.")
        sys.exit()

    try:
        # 2. SOLICITUD DE DATOS
        print(f"Procesando: {os.path.basename(archivo_origen)}")
        
        print("\n--- MEDIDAS DEL DOCUMENTO ---")
        ancho_str = input("📏 Ancho en pulgadas (Enter para usar 2.29): ") or "2.29"
        alto_str = input("📏 Alto en pulgadas  (Enter para usar 1.39): ") or "1.39"
        
        ancho = float(ancho_str)
        alto = float(alto_str)
        
        print("\n--- MENSAJE DE LA MARCA DE AGUA ---")
        txt_1 = input("✏️  Línea 1 (ej. USO EXCLUSIVO): ")
        if not txt_1: txt_1 = "COPIA DE SEGURIDAD" 
            
        txt_2 = input("✏️  Línea 2 (ej. SEGUROS AXA): ")
        
        # 3. EJECUCIÓN
        print("\n🔄 Aplicando censura y marcas de agua...")
        salida = procesar_pdf(archivo_origen, ancho, alto, txt_1, txt_2)
        
        print(f"✅ ¡ÉXITO! Documento guardado como: {salida}")
        
    except ValueError:
        print("❌ Error: Las medidas deben ser números.")
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")