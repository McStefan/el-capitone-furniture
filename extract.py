import fitz
import os

pdf_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\Каталог_новый.pdf"
output_dir = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\images\catalog"

doc = fitz.open(pdf_path)
for page_index in range(len(doc)):
    page = doc.load_page(page_index)
    image_list = page.get_images()
    
    for image_index, img in enumerate(page.get_images(), start=1):
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        
        if pix.n - pix.alpha < 4:       # this is GRAY or RGB
            pix.save(os.path.join(output_dir, f"page_{page_index}-img_{image_index}.png"))
        else:               # CMYK: convert to RGB first
            pix1 = fitz.Pixmap(fitz.csRGB, pix)
            pix1.save(os.path.join(output_dir, f"page_{page_index}-img_{image_index}.png"))
            pix1 = None
        pix = None

print(f"Extracted images to {output_dir}")
