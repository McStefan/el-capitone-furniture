import os
import re

html_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v1.html"
css_v1_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\css\style_v1.css"
css_v2_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\css\style_v2.css"
js_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\js\script.js"

# --- HTML ---
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Hero image priority
html = html.replace(
    '<img src="images/hero-bg.png" alt="Стильный интерьер с мебелью на заказ" loading="lazy">',
    '<img src="images/hero-bg.png" alt="Стильный интерьер с мебелью на заказ" fetchpriority="high">'
)

# 2. Catalog links
html = re.sub(
    r'(<h3>Диваны и кресла</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Интересует%20расчет%20стоимости%20по%20категории%20«Диваны%20и%20кресла»" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)
html = re.sub(
    r'(<h3>Кровати на заказ</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Интересует%20расчет%20стоимости%20по%20категории%20«Кровати%20на%20заказ»" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)
html = re.sub(
    r'(<h3>Мягкие панели</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Интересует%20расчет%20стоимости%20по%20категории%20«Мягкие%20панели»" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)
html = re.sub(
    r'(<h3>Дизайнерские кресла</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Интересует%20расчет%20стоимости%20по%20категории%20«Дизайнерские%20кресла»" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)
html = re.sub(
    r'(<h3>Пуфы и банкетки</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Интересует%20расчет%20стоимости%20по%20категории%20«Пуфы%20и%20банкетки»" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)
html = re.sub(
    r'(<h3>Индивидуальные изделия</h3>\s*<p>.*?</p>\s*)<a href="#contacts" class="btn-text">Узнать стоимость &rarr;</a>',
    r'\1<a href="https://wa.me/1234567890?text=Здравствуйте!%20Хочу%20обсудить%20индивидуальный%20проект%20мебели" target="_blank" class="btn-text">Написать в WhatsApp &rarr;</a>',
    html
)

# 3. Materials
old_materials = """<div class="materials__tags">
                <span class="tag">Велюр</span>
                <span class="tag">Рогожка</span>
                <span class="tag">Букле</span>
                <span class="tag">Экокожа</span>
                <span class="tag">Жаккард</span>
                <span class="tag">Микровелюр</span>
                <span class="tag">ЛДСП</span>
                <span class="tag">МДФ</span>
                <span class="tag">Эмаль</span>
                <span class="tag">Шпон</span>
            </div>"""
        
new_materials = """<div class="materials__swatches">
                <div class="swatch-item"><div class="swatch-color" style="background: linear-gradient(135deg, #1e3b4d, #29526b);"></div><span>Велюр</span></div>
                <div class="swatch-item"><div class="swatch-color" style="background: repeating-linear-gradient(45deg, #d3c7b9, #d3c7b9 2px, #c4b5a3 2px, #c4b5a3 4px);"></div><span>Рогожка</span></div>
                <div class="swatch-item"><div class="swatch-color" style="background: radial-gradient(circle at 50% 50%, #fdfbf7 2px, #e8e2d5 3px); background-size: 8px 8px;"></div><span>Букле</span></div>
                <div class="swatch-item"><div class="swatch-color" style="background: #3e2723;"></div><span>Экокожа</span></div>
                <div class="swatch-item"><div class="swatch-color" style="background: linear-gradient(to right, #8b9dc3, #7a8baf);"></div><span>Жаккард</span></div>
                <div class="swatch-item"><div class="swatch-color" style="background: #a98467;"></div><span>Дерево (ЛДСП/Шпон)</span></div>
            </div>"""
html = html.replace(old_materials, new_materials)

# 4. Lightbox Dialog
lightbox_html = """
    <!-- Lightbox -->
    <dialog class="lightbox-dialog" id="lightbox">
        <button class="lightbox__close" aria-label="Закрыть">&times;</button>
        <img src="" alt="Увеличенное фото" class="lightbox__img">
    </dialog>

    <script src="js/script.js"></script>"""
html = html.replace('<script src="js/script.js"></script>', lightbox_html)

# Add lightbox trigger class
html = html.replace('class="portfolio-item"', 'class="portfolio-item lightbox-trigger"')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)


# --- CSS V1 ---
with open(css_v1_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Add native smooth scroll
css = css.replace(
    'overflow-x: hidden;\n}', 
    'overflow-x: hidden;\n    scroll-behavior: smooth;\n}'
)
# Add text balance
css = css.replace(
    'h1, h2, h3, h4 {\n    font-weight: 600;\n    line-height: 1.2;\n}',
    'h1, h2, h3, h4 {\n    font-weight: 600;\n    line-height: 1.2;\n    text-wrap: balance;\n}'
)

css += """
/* Materials Swatches */
.materials__swatches {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 30px;
    margin-top: 40px;
}
.swatch-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
}
.swatch-color {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    box-shadow: inset 0 0 10px rgba(0,0,0,0.2), 0 5px 15px rgba(0,0,0,0.3);
    border: 3px solid rgba(255,255,255,0.1);
    transition: transform 0.3s ease;
}
.swatch-item:hover .swatch-color {
    transform: scale(1.1);
}
.swatch-item span {
    font-size: 0.9rem;
    font-weight: 500;
}

/* Lightbox Dialog */
.lightbox-dialog {
    margin: auto;
    padding: 0;
    border: none;
    background: transparent;
    max-width: 90vw;
    max-height: 90vh;
}
.lightbox-dialog::backdrop {
    background: rgba(0,0,0,0.85);
    backdrop-filter: blur(5px);
}
.lightbox__img {
    max-width: 100%;
    max-height: 90vh;
    border-radius: 8px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    display: block;
}
.lightbox__close {
    position: fixed;
    top: 20px;
    right: 30px;
    background: none;
    border: none;
    color: #fff;
    font-size: 3rem;
    cursor: pointer;
    z-index: 10;
    transition: color 0.3s;
}
.lightbox__close:hover {
    color: var(--accent-color);
}
.portfolio-item.lightbox-trigger {
    cursor: pointer;
}

/* Mobile Menu Active */
.header__nav.active {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 80px;
    left: 0;
    right: 0;
    background: rgba(252, 252, 252, 0.98);
    padding: 20px;
    border-bottom: 1px solid var(--border-color);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}
"""
with open(css_v1_path, 'w', encoding='utf-8') as f:
    f.write(css)


# --- CSS V2 ---
with open(css_v2_path, 'r', encoding='utf-8') as f:
    css2 = f.read()

# Add native smooth scroll
css2 = css2.replace(
    'overflow-x: hidden;\n}', 
    'overflow-x: hidden;\n    scroll-behavior: smooth;\n}'
)
with open(css_v2_path, 'w', encoding='utf-8') as f:
    f.write(css2)


# --- JS ---
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# Remove smooth scroll polyfill logic
js = re.sub(r"// Smooth scrolling.*?\}\);\n    \}\);\n\n", "", js, flags=re.DOTALL)

new_js = """    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const headerNav = document.querySelector('.header__nav');
    
    if (menuToggle && headerNav) {
        menuToggle.addEventListener('click', () => {
            headerNav.classList.toggle('active');
        });
        
        headerNav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                headerNav.classList.remove('active');
            });
        });
    }

    // Lightbox Logic
    const lightbox = document.getElementById('lightbox');
    if (lightbox) {
        const lightboxImg = lightbox.querySelector('.lightbox__img');
        const lightboxClose = lightbox.querySelector('.lightbox__close');

        document.querySelectorAll('.lightbox-trigger').forEach(item => {
            item.addEventListener('click', () => {
                const img = item.querySelector('img');
                if (img) {
                    lightboxImg.src = img.src;
                    lightbox.showModal();
                }
            });
        });

        lightboxClose.addEventListener('click', () => {
            lightbox.close();
        });

        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) {
                lightbox.close();
            }
        });
    }
"""
js = js.replace("document.addEventListener('DOMContentLoaded', () => {", "document.addEventListener('DOMContentLoaded', () => {\n" + new_js)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print("Done")
