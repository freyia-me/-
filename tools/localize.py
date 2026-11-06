#!/usr/bin/env python3
"""Русификация видимого текста страниц JeuDérm (закон о государственном языке).

Латиницей остаётся только зарегистрированный товарный знак JeuDérm (и названия сервисов
WhatsApp / Telegram / MAX, адреса почты и сайтов). Всё остальное — по-русски.
Меняется только то, что видит посетитель: текст, alt, title, aria-label, data-vol / data-care-t / data-ppm / data-copy.
CSS, скрипты, классы, адреса и id товаров не трогаются.

Запуск:  python3 tools/localize.py            — обработать tilda/*.html и обновить tilda-txt/*.txt
Генераторы (build_*.py) вызывают ru() перед записью, поэтому пересборка русификацию не теряет.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Порядок важен: длинные фразы раньше коротких.
PAIRS = [
    # --- бренд и компания ---
    ('JeuDérm', 'JeuDérm'), ('Жедерм', 'JeuDérm'), ('JeuDerm', 'JeuDérm'),
    ('Revolution Bio', 'Революшн Био'), ('Revolution bio', 'Революшн Био'),
    ('VIRTA-MED KOREA Co., LTD', '«Вирта-Мед Корея»'), ('CEO Tatyana Jeon', 'генеральный директор Татьяна Чон'),
    ('JeuDérm International Aesthetic Symposium', 'Международный эстетический симпозиум JeuDérm'),
    ('International Aesthetic Symposium', 'Международный эстетический симпозиум'),
    ('JeuDérm Symposium', 'Симпозиум JeuDérm'), ('Aesthetic Symposium', 'эстетический симпозиум'),
    ('JeuDérm / SCIENCE 01', 'JeuDérm / наука 01'),
    # --- полные названия средств ---
    ('Reform Age Collagen Tonic', 'Реформэйдж коллагеновый тоник'),
    ('Reform Age Mild Cleanser', 'Реформэйдж мягкая пенка'),
    ('Reform Age Micro Touch Mask', 'Реформэйдж маска со спикулами'),
    ('Reform Age Intensive Eye Cream', 'Реформэйдж крем для век'),
    ('Reform Age Intensive Cream', 'Реформэйдж интенсивный крем'),
    ('Reform Age O2 Boto Fluid', 'Реформэйдж кислородный бото-флюид'),
    ('Reform Age O₂ Boto Fluid', 'Реформэйдж кислородный бото-флюид'),
    ('Reform Age Eye Cream', 'Реформэйдж крем для век'),
    ('Ato Care Mild Cleanser', 'Ато Кэр очищающий гель'), ('Ato Care Toner Mousse', 'Ато Кэр тонер-мусс'),
    ('Ato Care Moist Emulsion', 'Ато Кэр увлажняющая эмульсия'), ('Ato Care Intensive Cream', 'Ато Кэр интенсивный крем'),
    ('Acno Mild Cleanser', 'Акно очищающий гель'), ('Acno Multi-Acid Pad', 'Акно мультикислотные диски'),
    ('Acno Clay Mask', 'Акно маска с глиной'), ('Acno Active Gel', 'Акно Актив гель'),
    ('Acno Active Emulsion', 'Акно Актив эмульсия'),
    ('Adaptive Skin Detox Mask', 'Адаптив Скин детокс-маска'),
    ('O₂ Therapy Active Gel', 'кислородный активный гель'), ('O2 Therapy Active Gel', 'кислородный активный гель'),
    ('Therapy Active Gel', 'кислородный активный гель'),
    ('Repair Mask Post-Procedure', 'восстанавливающая маска'), ('Repair Post-Procedure Mask', 'восстанавливающая маска'),
    ('Lift Intense Viso Contour', 'Лифт Интенс Визо Контур'), ('Viso Contour', 'Визо Контур'),
    ('Molecular Twin Exfoliant', 'Молекулярный Твин эксфолиант'), ('Molecular Twin Oil', 'Молекулярный Твин масло'),
    ('Molecular Oil', 'молекулярное масло'), ('Molecular Twin', 'Молекулярный Твин'),
    ('Drainage Physio Gel', 'дренажный физиогель'),
    ('Hair-Growth Concentrate', 'концентрат для роста волос'), ('Hair Growth Stimulator', 'стимулятор роста волос'),
    ('Zymo Complex', 'Зимо Комплекс'), ('Nova Complex', 'Нова Комплекс'),
    ('Zymo Active', 'Зимо Актив'), ('Nova Active', 'Нова Актив'),
    ('AHA Primer', 'АНА-праймер'), ('pH Reductant', 'pH-редуктант'), ('Reductant', 'редуктант'), ('Primer', 'праймер'),
    ('Mild Cleanser', 'Мягкая пенка'), ('Collagen Tonic', 'коллагеновый тоник'), ('Micro Touch Mask', 'маска со спикулами'),
    ('Intensive Eye Cream', 'крем для век'), ('Intensive Cream', 'интенсивный крем'), ('Eye Cream', 'крем для век'),
    ('O₂ Boto Fluid', 'кислородный бото-флюид'), ('O2 Boto Fluid', 'кислородный бото-флюид'), ('Boto Fluid', 'бото-флюид'),
    ('Toner Mousse', 'тонер-мусс'), ('Moist Emulsion', 'увлажняющая эмульсия'), ('Multi-Acid Pad', 'мультикислотные диски'),
    ('Clay Mask', 'маска с глиной'), ('Active Gel', 'гель'), ('Active Emulsion', 'эмульсия'),
    ('Detox Mask', 'детокс-маска'), ('Repair Mask', 'восстанавливающая маска'),
    # --- линии ---
    ('Reform Age', 'Реформэйдж'), ('Acno Active', 'Акно Актив'), ('Ato Care', 'Ато Кэр'), ('Adaptive Skin', 'Адаптив Скин'),
    ('Lift Intense', 'Лифт Интенс'), ('Hair Genesis', 'Хэйр Генезис'), ('Hairgenesis', 'Хэйр Генезис'),
    ('HairGenesis 1.1', 'ХэйрГенезис 1.1'), ('FitoGenesis', 'ФитоГенезис'),
    ('Nova · Zymo', 'Нова · Зимо'), ('Zymo', 'Зимо'), ('Nova', 'Нова'), ('Acno', 'Акно'), ('Renew', 'обновление'),
    ('Viso-Sculpt', 'Визо-скульпт'), ('Professional', 'профессиональная'), ('Homecare', 'домашний уход'),
    ('Active', 'Актив'), ('Oil', 'масло'),
    # --- активы: товарные знаки производителей сырья — русскими буквами ---
    ('Copper Tetrapeptide-52 Dimer', 'тетрапептид меди-52 димер'), ('Copper Tripeptide-1', 'трипептид меди-1'),
    ('Acetyl Hexapeptide-8', 'ацетил гексапептид-8'),
    ('Triple M Complex™', 'Трипл Эм Комплекс'), ('Triple M Complex', 'Трипл Эм Комплекс'),
    ('Acnotide™', 'Акнотайд'), ('Acnotide', 'Акнотайд'), ('Demelaxyl™', 'Демелаксил'), ('Demelaxyl', 'Демелаксил'),
    ('Serilesine™', 'Серилезин'), ('Serilesine', 'Серилезин'), ('Syn®-Ake', 'Син-Эйк'), ('Argireline', 'Аргирелин'),
    ('Matrixyl®', 'Матриксил'), ('Oligo AWP &amp; CBP', 'олигопептиды AWP и CBP'), ('Oligo AWP & CBP', 'олигопептиды AWP и CBP'),
    ('Oligo AWP', 'олигопептид AWP'), ('Oligo CBP', 'олигопептид CBP'),
    ('MOIST-HA5', 'МОИСТ-HA5'), ('MOIST HA5', 'МОИСТ-HA5'), ('MultiEX', 'МультиЭкс'), ('MultiEx', 'МультиЭкс'),
    ('BOTANICEUTICAL PLUS 10', 'Ботаницевтикал Плюс 10'), ('BOTANICEUTICAL Plus 10', 'Ботаницевтикал Плюс 10'),
    ('Pheohydrane', 'Феогидран'), ('Dermaflux', 'Дермафлюкс'), ('Cellular Activator', 'клеточный активатор'),
    ('HERBAL COMPLEX-8', 'растительный комплекс-8'), ('HERBAL Complex', 'растительный комплекс'),
    ('MARINE COMPLEX', 'морской комплекс'), ('HERB STORY', 'травяной комплекс'), ('ANTI ACNE', 'анти-акне'),
    ('Hydro-GF3', 'Гидро-GF3'), ('Acell 300', 'Ацелл 300'), ('Mountain Air', 'Горный воздух'),
    ('sh-олигопептиды и sh-полипептиды', 'олигопептиды и полипептиды'), ('sh-олигопептиды', 'олигопептиды'),
    ('sh-олигопептид-1', 'олигопептид-1'), ('sh-полипептиды', 'полипептиды'),
    ('факторы роста EGF, IGF, bFGF, TGF-β', 'факторы роста (эпидермальный, инсулиноподобный, фибробластов, трансформирующий)'),
    ('(EGF, FGF, TGF)', '(факторы роста)'),
    ('AHA/BHA/PHA', 'АНА/ВНА/РНА'), ('AHA/BHA', 'АНА/ВНА'), ('AHA', 'АНА'), ('BHA', 'ВНА'), ('PHA', 'РНА'),
    ('(PHA)', '(РНА)'), ('натрий PCA', 'пирролидонкарбоксилат натрия'), ('NMF', 'натурального увлажняющего фактора'),
    ('LED (синий)', 'светодиодной терапией (синий свет)'), ('ppm', 'ppm'),
    ('Витамины B3, B5, E', 'витамины B3, B5, E'),
    # --- прочее ---
    ('beauty-сферы', 'индустрии красоты'), ('SOS для кожи', 'скорая помощь для кожи'),
    ('лат. enzyme', 'латинского «энзим»'), ('лат. novem', 'латинского «новем»'),
    ('FAQ', 'Вопросы'), ('E-mail', 'Эл. почта'), ('Da', 'Да'),
]

LATIN_WORD = re.compile(r'[A-Za-z]')
_pairs = sorted(PAIRS, key=lambda p: -len(p[0]))


def _sub_text(t):
    for a, b in _pairs:
        if a == b:
            continue
        if LATIN_WORD.match(a[-1]) or LATIN_WORD.match(a[0]):
            t = re.sub(r'(?<![A-Za-zА-Яа-яё@./-])' + re.escape(a) + r'(?![A-Za-zА-Яа-яё@-])', b, t)
        else:
            t = t.replace(a, b)
    return t


ATTRS = re.compile(r'\b(alt|title|aria-label|data-vol|data-care-t|data-ppm|data-copy)="([^"]*)"')
TOKENS = re.compile(r'(<style\b.*?</style>|<script\b.*?</script>|<!--.*?-->|<[^>]+>)', re.S)


def _cap(m):
    t = m.group(2)
    return m.group(1) + t[:1].upper() + t[1:]


def ru(html):
    out = []
    for part in TOKENS.split(html):
        if not part:
            continue
        if part.startswith(('<style', '<script', '<!--')):
            out.append(part)
        elif part.startswith('<'):
            out.append(ATTRS.sub(lambda m: '%s="%s"' % (m.group(1), _sub_text(m.group(2))), part))
        else:
            out.append(_sub_text(part))
    res = ''.join(out)
    return re.sub(r'(<span class="en">)([^<]+)', _cap, res)


if __name__ == '__main__':
    for f in sorted(ROOT.glob('tilda/*.html')):
        s = f.read_text(encoding='utf-8')
        n = ru(s)
        (ROOT / 'tilda-txt' / (f.stem + '.txt')).write_text(n, encoding='utf-8')
        if n != s:
            f.write_text(n, encoding='utf-8')
            print('localized', f.name)
