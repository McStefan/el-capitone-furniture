import os
import glob
import fitz
import re

catalog_dir = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\images\catalog"
pdf_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\Каталог_новый.pdf"

images = glob.glob(os.path.join(catalog_dir, "*.png"))

def get_page_num(path):
    basename = os.path.basename(path)
    try:
        return int(basename.split('-')[0].replace('page_', ''))
    except:
        return 999

images.sort(key=get_page_num)

doc = fitz.open(pdf_path)

def clean_label(text):
    # Remove newlines and extra spaces
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove trailing isolated numbers (page numbers)
    text = re.sub(r'\s+\d+$', '', text)
    # Fix common font rendering issues seen in the PDF
    text = text.replace('Capi t on]', 'Capitone')
    text = text.replace('Capiton]', 'Capitone')
    text = text.replace('Lakshmˆ', 'Lakshmi')
    text = text.replace('Lakshm ', 'Lakshmi ')
    text = text.replace('Ros]', 'Rose')
    text = text.replace('M inio·', 'Minion')
    text = text.replace('M onr¾', 'Monro')
    text = text.replace('Aeli·', 'Aelin')
    text = text.replace('LorQ', 'Lord')
    text = text.replace('ChesterfielQclassiE', 'Chesterfield Classic')
    text = text.replace('Baxteê', 'Baxter')
    text = text.replace('Bruc¾', 'Bruce')
    text = text.replace('Brocc(sof(', 'Brocca sofa')
    text = text.replace('ClouQ', 'Cloud')
    text = text.replace('Ko‚-ˆ-Nooê', 'Koh-i-Noor')
    text = text.replace('LofýLuğ', 'Loft Lux')
    text = text.replace('Ocea·', 'Ocean')
    text = text.replace('M êBobbģ', 'Mr Bobby')
    text = text.replace('b9itali(tuftģtim]', 'B&B Italia Tufty Time')
    text = text.replace('extr(lonwsof(', 'Extra Long Sofa')
    text = text.replace('Camaleond(', 'Camaleonda')
    text = text.replace('AntiEBñ', 'Antic Bed')
    text = text.replace('Bert(', 'Berta')
    text = text.replace('Ceppˆ', 'Ceppi')
    text = text.replace('Colett¾', 'Coletto')
    text = text.replace('Decor¾', 'Decoro')
    text = text.replace('Dezerˆ', 'Dezeri')
    text = text.replace('Julieý', 'Juliet')
    text = text.replace('Libertģ', 'Liberty')
    text = text.replace('M alibĊ', 'Malibu')
    text = text.replace('Arieª', 'Ariel')
    text = text.replace('Skģ', 'Sky')
    text = text.replace('Tatli·', 'Tatlin')
    return text.strip()

# ==========================================
# Generate portfolio_v1.html
# ==========================================
v1_items = ""
for img_path in images:
    page_num = get_page_num(img_path)
    label = "Модель мебели"
    if page_num < len(doc):
        raw_text = doc.load_page(page_num).get_text("text")
        cleaned = clean_label(raw_text)
        if cleaned:
            label = cleaned
            
    rel_img = f"images/catalog/{os.path.basename(img_path)}"
    v1_items += f'''
                <div class="portfolio-item lightbox-trigger">
                    <img src="{rel_img}" alt="{label}" loading="lazy">
                    <div class="portfolio-item__overlay">
                        <span>{label}</span>
                    </div>
                </div>'''

html_v1 = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Полный каталог работ — El Capitone</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style_v1.css">
    <style>
        .page-header {{ padding: 120px 0 60px; text-align: center; background: var(--surface-color); border-bottom: 1px solid var(--border-color); }}
        .page-header h1 {{ font-size: 3rem; margin-bottom: 15px; }}
        .page-header p {{ color: var(--text-muted); max-width: 600px; margin: 0 auto; }}
        .full-portfolio {{ padding: 80px 0; }}
        
        /* Ensure overlay text is visible and styled nicely */
        .portfolio-item__overlay span {{
            font-size: 1.1rem;
            text-align: center;
            padding: 0 15px;
            line-height: 1.4;
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container header__inner">
            <a href="index_v1.html" class="header__logo" style="text-decoration:none; color:inherit;">El Capitone</a>
            <nav class="header__nav">
                <a href="index_v1.html#catalog">Каталог</a>
                <a href="index_v1.html#process">Как заказать</a>
                <a href="portfolio_v1.html">Наши работы</a>
                <a href="index_v1.html#contacts">Контакты</a>
            </nav>
            <div class="header__actions">
                <a href="https://wa.me/1234567890" class="btn-text">WhatsApp</a>
                <a href="index_v1.html#contacts" class="btn btn-outline">Рассчитать стоимость</a>
            </div>
            <button class="menu-toggle" aria-label="Открыть меню">
                <span></span><span></span><span></span>
            </button>
        </div>
    </header>

    <div class="page-header">
        <div class="container">
            <h1>Полный каталог изделий</h1>
            <p>Изучите все наши модели мебели из актуального каталога. Любое изделие может быть адаптировано под ваши размеры и выполнено в нужной ткани.</p>
        </div>
    </div>

    <section class="full-portfolio">
        <div class="container">
            <div class="portfolio__grid">
                {v1_items}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer__inner">
            <div class="footer__brand">El Capitone</div>
            <div class="footer__copy">© 2026 Все права защищены. Изготовление мягкой мебели на заказ.</div>
        </div>
    </footer>

    <!-- Lightbox -->
    <dialog class="lightbox-dialog" id="lightbox">
        <button class="lightbox__close" aria-label="Закрыть">&times;</button>
        <div style="text-align:center;">
            <img src="" alt="Увеличенное фото" class="lightbox__img">
            <h3 class="lightbox__caption" style="color:white; margin-top:15px; font-weight:400;"></h3>
        </div>
    </dialog>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            const lightbox = document.getElementById('lightbox');
            if (lightbox) {{
                const lightboxImg = lightbox.querySelector('.lightbox__img');
                const lightboxCaption = lightbox.querySelector('.lightbox__caption');
                const lightboxClose = lightbox.querySelector('.lightbox__close');

                document.querySelectorAll('.lightbox-trigger').forEach(item => {{
                    item.addEventListener('click', () => {{
                        const img = item.querySelector('img');
                        const span = item.querySelector('span');
                        if (img) {{
                            lightboxImg.src = img.src;
                            if(span && lightboxCaption) lightboxCaption.textContent = span.textContent;
                            lightbox.showModal();
                        }}
                    }});
                }});

                lightboxClose.addEventListener('click', () => {{
                    lightbox.close();
                }});

                lightbox.addEventListener('click', (e) => {{
                    if (e.target === lightbox) {{
                        lightbox.close();
                    }}
                }});
            }}
        }});
    </script>
</body>
</html>
"""
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\portfolio_v1.html", 'w', encoding='utf-8') as f:
    f.write(html_v1)

# ==========================================
# Generate portfolio_v2.html
# ==========================================
v2_items = ""
for img_path in images:
    page_num = get_page_num(img_path)
    label = "Модель мебели"
    if page_num < len(doc):
        raw_text = doc.load_page(page_num).get_text("text")
        cleaned = clean_label(raw_text)
        if cleaned:
            label = cleaned
            
    rel_img = f"images/catalog/{os.path.basename(img_path)}"
    v2_items += f'''
                <div class="gal-item">
                    <img src="{rel_img}" alt="{label}" loading="lazy">
                    <div class="gal-item__caption">{label}</div>
                </div>'''

html_v2 = f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Полная галерея — El Capitone</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600&family=Montserrat:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style_v2.css">
    <style>
        .page-header {{ padding: 160px 0 80px; text-align: center; background: #000; color: #fff; }}
        .page-header h1 {{ font-size: 4rem; margin-bottom: 20px; }}
        .page-header p {{ opacity: 0.8; max-width: 600px; margin: 0 auto; font-size: 1.1rem; }}
        .gallery-full {{ padding: 100px 0; }}
        .gallery-full .gallery__masonry {{ grid-template-columns: repeat(4, 1fr); }}
        @media (max-width: 1200px) {{ .gallery-full .gallery__masonry {{ grid-template-columns: repeat(3, 1fr); }} }}
        @media (max-width: 992px) {{ .gallery-full .gallery__masonry {{ grid-template-columns: repeat(2, 1fr); }} }}
        @media (max-width: 576px) {{ .gallery-full .gallery__masonry {{ grid-template-columns: 1fr; }} }}
        
        /* Custom caption styling for v2 */
        .gal-item {{
            position: relative;
        }}
        .gal-item__caption {{
            position: absolute;
            bottom: 0; left: 0; right: 0;
            background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
            color: #fff;
            padding: 30px 20px 15px;
            font-size: 1.1rem;
            text-align: center;
            opacity: 0;
            transition: opacity 0.4s;
            pointer-events: none;
        }}
        .gal-item:hover .gal-item__caption {{
            opacity: 1;
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container header__inner">
            <a href="index_v2.html" class="header__logo" style="text-decoration:none; color:#fff;">El Capitone</a>
            <nav class="header__nav">
                <a href="index_v2.html#collections">Коллекции</a>
                <a href="portfolio_v2.html">Галерея</a>
                <a href="index_v2.html#materials">Ткани</a>
            </nav>
            <a href="index_v2.html#materials" class="btn btn-outline header__btn">Связаться</a>
        </div>
    </header>

    <div class="page-header">
        <div class="container">
            <h1>Полная коллекция</h1>
            <p>Погрузитесь в эстетику форм и фактур. Все представленные модели доступны к заказу.</p>
        </div>
    </div>

    <section class="gallery-full">
        <div class="container">
            <div class="gallery__masonry">
                {v2_items}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container footer__inner">
            <div class="footer__logo">El Capitone</div>
            <div class="footer__links">
                <a href="https://wa.me/1234567890">WhatsApp</a>
                <a href="https://t.me/username">Telegram</a>
            </div>
        </div>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
"""
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\portfolio_v2.html", 'w', encoding='utf-8') as f:
    f.write(html_v2)

print("Updated galleries with extracted labels.")
