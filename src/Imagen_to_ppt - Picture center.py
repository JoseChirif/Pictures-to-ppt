import os
from pptx import Presentation
from pptx.util import Cm, Pt
from pptx.dml.color import RGBColor
from PIL import Image

def split_filename(filename):
    parts = filename.split('_', 1)
    if len(parts) > 1:
        return parts[0], parts[1]
    else:
        return parts[0], ''

def create_presentation(image_folder, output_pptx):
    # Crear una presentación en blanco con dimensiones específicas
    prs = Presentation()
    prs.slide_width = Cm(33.867)
    prs.slide_height = Cm(19.05)
    
    # Obtener la lista de imágenes en la carpeta
    images = [img for img in os.listdir(image_folder) if img.lower().endswith('.jpg')]
    
    for image in images:
        # Ruta completa de la imagen
        image_path = os.path.join(image_folder, image)
        
        # Obtener dimensiones de la imagen
        with Image.open(image_path) as img:
            img_width, img_height = img.size
        
        # Establecer la altura fija de la imagen
        new_height = Cm(17.43)
        new_width = int((img_width / img_height) * new_height)
        
        if new_width > prs.slide_width:
            new_width = prs.slide_width
            new_height = int((img_height / img_width) * new_width)
        
        # Calcular las posiciones para centrar la imagen
        left = int((prs.slide_width - new_width) / 2)
        top = int((prs.slide_height - new_height) / 2)
        
        # Crear una nueva diapositiva
        slide_layout = prs.slide_layouts[6]  # Usar un diseño de diapositiva en blanco
        slide = prs.slides.add_slide(slide_layout)
        
        # Añadir la imagen centrada con borde negro
        picture = slide.shapes.add_picture(image_path, left, top, width=new_width, height=new_height)
        line = picture.line
        line.color.rgb = RGBColor(0, 0, 0)  # Borde negro
        line.width = Pt(0.75)  # Grosor de borde 0.75 pt
        
        # Obtener el nombre del archivo sin la extensión
        file_name = os.path.splitext(image)[0]
        
        # Añadir el nombre del archivo en la base de la diapositiva
        text_left = Cm(0)  # Centrar el texto horizontalmente
        text_top = prs.slide_height - Cm(1.5)  # Posicionar en la base de la diapositiva
        text_width = prs.slide_width
        text_height = Cm(1)
        
        txBox = slide.shapes.add_textbox(text_left, text_top, text_width, text_height)
        tf = txBox.text_frame
        tf.clear()
        
        p = tf.add_paragraph()
        p.text = file_name
        p.font.size = Pt(10)  # Tamaño del texto 10
        p.font.color.rgb = RGBColor(0, 0, 0)  # Texto negro
        p.font.name = 'Aptos'  # Fuente Aptos
        p.alignment = 2  # Centrado
        
    # Guardar la presentación
    prs.save(output_pptx)
    print(f"Presentación guardada como {output_pptx}")

if __name__ == "__main__":
    image_folder = "imagenes"  # Carpeta de imágenes en el mismo directorio que el script
    output_pptx = "presentacion.pptx"  # Nombre del archivo de salida
    create_presentation(image_folder, output_pptx)
