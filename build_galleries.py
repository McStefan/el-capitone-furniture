import os
import glob

catalog_dir = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\images\catalog"
images = glob.glob(os.path.join(catalog_dir, "*.png"))
# Sort them nicely, maybe by page number
def get_page_num(path):
    basename = os.path.basename(path)
    # page_10-img_1.png
    try:
        return int(basename.split('-')[0].replace('page_', ''))
    except:
        return 999

images.sort(key=get_page_num)

# We want relative paths for the HTML
rel_images = [f"images/catalog/{os.path.basename(img)}" for img in images]

# ==========================================
# Generate portfolio_v1.html
# ==========================================
v1_items = ""
for img in rel_images:
    v1_items += f'''
                <div class="portfolio-item lightbox-trigger">
                    <img src="{img}" alt="Модель мебели" loading="lazy">
                    <div class="portfolio-item__overlay">
                        <span>Смотреть</span>
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
        <img src="" alt="Увеличенное фото" class="lightbox__img">
    </dialog>

    <script src="js/script.js"></script>
</body>
</html>
"""
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\portfolio_v1.html", 'w', encoding='utf-8') as f:
    f.write(html_v1)

# ==========================================
# Generate portfolio_v2.html
# ==========================================
v2_items = ""
for img in rel_images:
    v2_items += f'''
                <div class="gal-item"><img src="{img}" alt="Модель мебели" loading="lazy"></div>'''

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

# ==========================================
# Update index_v1.html to link to portfolio
# ==========================================
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v1.html", 'r', encoding='utf-8') as f:
    v1 = f.read()
v1 = v1.replace(
    '<a href="#contacts" class="btn btn-outline">Хочу похожий проект</a>',
    '<a href="portfolio_v1.html" class="btn btn-outline">Смотреть весь каталог (50+ моделей)</a>'
)
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v1.html", 'w', encoding='utf-8') as f:
    f.write(v1)

# ==========================================
# Update index_v2.html to link to portfolio
# ==========================================
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v2.html", 'r', encoding='utf-8') as f:
    v2 = f.read()
v2 = v2.replace(
    '<button class="btn btn-outline" commandfor="calc-dialog" command="show-modal">Заказать похожий проект</button>',
    '<a href="portfolio_v2.html" class="btn btn-outline">Смотреть полную галерею</a>'
)
with open(r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v2.html", 'w', encoding='utf-8') as f:
    f.write(v2)

print("Created portfolio pages successfully.")
