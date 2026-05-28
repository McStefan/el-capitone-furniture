import re

html_path = r"C:\Users\Дмитрий\Desktop\Создать лендин\Мебель\index_v2.html"

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the "Заказать похожий проект" button with the portfolio link
html = html.replace(
    '<button class="btn btn-outline" data-modal="calc">Заказать похожий проект</button>',
    '<a href="portfolio_v2.html" class="btn btn-outline">Смотреть полную галерею (50+ фото)</a>'
)

# 2. Update Header button
html = html.replace(
    '<button class="btn btn-outline header__btn" commandfor="calc-dialog" command="show-modal">Связаться</button>',
    '<a href="#contacts" class="btn btn-outline header__btn">Связаться</a>'
)

# 3. Update Hero button
html = html.replace(
    '<button class="btn btn-primary" commandfor="calc-dialog" command="show-modal">Оставить заявку</button>',
    '<a href="#contacts" class="btn btn-primary">Связаться в WhatsApp</a>'
)

# 4. Update Collections buttons
html = html.replace('commandfor="calc-dialog" command="show-modal"', '')
html = html.replace('<button class="coll-card coll-card--large" >', '<a href="portfolio_v2.html" class="coll-card coll-card--large">')
html = html.replace('<button class="coll-card" >', '<a href="portfolio_v2.html" class="coll-card">')
html = html.replace('</button>', '</a>')

# Wait, the replace of `</button>` -> `</a>` is dangerous if there are other buttons. Let's be precise.
html = html.replace(
    '''                    <div class="coll-card__text">
                        <h3>Диваны</h3>
                        <span>Смотреть варианты</span>
                    </div>
                </a>''',
    '''                    <div class="coll-card__text">
                        <h3>Диваны</h3>
                        <span>Смотреть варианты</span>
                    </div>
                </a>'''
) # Just in case

# 5. Remove the form in .mc-contact and replace with direct contacts
contact_html = """            <div class="mc-contact" id="contacts">
                <div class="minimal-form" style="text-align: center;">
                    <h3 style="margin-bottom: 20px;">Свяжитесь с нами</h3>
                    <p style="color: var(--text-muted); margin-bottom: 30px;">Обсудим ваш проект и поможем с выбором тканей.</p>
                    <a href="https://wa.me/1234567890" class="btn btn-primary btn-block" style="margin-bottom: 15px; background-color: #25D366; color: #fff;">WhatsApp</a>
                    <a href="https://t.me/username" class="btn btn-outline btn-block" style="margin-bottom: 30px;">Telegram</a>
                    <a href="tel:+71234567890" style="font-size: 1.5rem; font-weight: 600; color: var(--text-color); text-decoration: none;">+7 (123) 456-78-90</a>
                </div>
            </div>"""

html = re.sub(
    r'<div class="mc-contact">.*?</div>\s*</div>\s*</section>',
    contact_html + '\n        </div>\n    </section>',
    html,
    flags=re.DOTALL
)

# 6. Remove the modal dialog and polyfill completely
html = re.sub(
    r'<!-- Modal -->\s*<dialog class="modal-dialog" id="calc-dialog">.*?</dialog>',
    '',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<script type="module">\s*if \(!\(\'commandForElement\'.*?</script>',
    '',
    html,
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index_v2.html")
