# ЖеДерм (JeuDérm) · ассеты сайта jeuderm-russia.ru

- `tilda/` — HTML-код блоков T123 по страницам (`home.html` — главная).
- `tilda-txt/` — тот же код в .txt, чтобы удобно копировать в Tilda.
- `images/<страница>/` — картинки для страниц. Подключаются через jsDelivr:
  `https://cdn.jsdelivr.net/gh/freyia-me/-@<коммит>/images/home/<файл>`

## Картинки главной (`images/home/`)

| Файл | Где на странице | Сейчас |
|---|---|---|
| `hero.webp` | Первый экран, фото справа (формат 4:5, арка сверху) + фон карточки «Профессиональный уход» | static.tildacdn.com · Copilot_20260526_132.png |
| `science.webp` | Блок «Красота начинается с понимания кожи» (широкое фото) + фон карточки «Домашний уход» | static.tildacdn.com · optimized_skincare_i.jpg |
| `partner-drk.webp` | Блок «Наши партнёры», логотип ДРК (квадрат) | static.tildacdn.com · 1.jpg |

## Остальные папки

- `images/products/` — фото продуктов (1254×1254, webp).
- `images/results/` — фото «до/после».
- `images/decor/` — отобранный декор, прозрачный фон, вырезан заново из исходных листов (без обрезков соседних элементов):
  - `molecule-*`, `sphere-*` — научные акценты (молекулы, ДНК, атом, сферы) — блоки про исследования, вебинары, CTA;
  - `ribbon-*`, `wave-*` — ленты/волны: `wave-mint` → Ato Care, `wave-blue` / `ribbon-iceblue` → Adaptive Skin, `ribbon-blush` → Reform Age / Acno, `ribbon-silver`, `wave-white` — нейтральные;
  - `divider-*` — тонкие разделители между блоками.
  Размер небольшой (130–550 px, разделители 950 px): только как акценты, не растягивать на всю ширину.
- `images/reference/` — образцы стеклянных кнопок, FAQ и инфокарточек. На сайт картинками не идут — воссоздаются в CSS.

Не взяли из архива элементов: уголки с жемчугом, звёзды, радужные пузыри и кольца (выбиваются из строгого стиля),
подиумы (у фото продуктов уже свои подиумы), стеклянные плашки/баннеры (слишком мелкие для фона — делаются в CSS),
поля поиска/выбора и чипсы (на сайте не нужны).

## Страницы линеек

Собираются скриптом: `python3 tools/build_lines.py` → `tilda/<slug>.html` и `tilda-txt/<slug>.txt`.
Тексты и товары — в `tools/build_lines.py` (LINES), дизайн и скрипт — в `tools/line_template.html`.

| Файл | Куда ставить в Tilda |
|---|---|
| `care` (общая страница категорий, `tools/build_hub.py`) | /pro-jeuderm и /homecare-jeuderm |
| `study` (`tools/build_study.py`) | /study |
| `cosmeticru` (`tools/build_drk.py`) | /cosmeticru |
| `reformage` | /reformage-pro и /reformage-homecare |
| `acno` | /acnopro-jeuderm и /acnohome |
| `atocare` | /atocare-pro и /atocare-home |
| `pro` | /pro |
| `renew` | /novazymo-exfoliation |
| `hairgenesis` | /hairgenesis |

Фильтр «Профессиональный / Домашний» выбирается сам по адресу страницы. Ссылка на товар: `адрес#p-<id>`.
