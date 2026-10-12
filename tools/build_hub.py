#!/usr/bin/env python3
"""Общая страница категорий «Профессиональный уход» / «Домашний уход».

Один код ставится на две страницы Tilda: /pro-jeuderm и /homecare-jeuderm.
Режим выбирается сам по адресу (в адресе есть «home» → домашний), можно задать ?care=pro / ?care=home.
Запуск:  python3 tools/build_hub.py  →  tilda/care.html и tilda-txt/care.txt
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = 'https://cdn.jsdelivr.net/gh/freyia-me/-@c5739fe/images/'
SITE = 'https://jeuderm-russia.ru/'
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 8h13M9 3l5 5-5 5"/></svg>'

# Направления. pro/home: (адрес страницы, число средств, фото) или None, если в этом уходе направления нет.
DIRS = [
    dict(c='#cd555b', short='Возрастной уход', line='Reform Age',
         text='Антивозрастной уход с пептидами и факторами роста: упругость, плотность и сияние кожи 30+.',
         pro=('reformage-pro', 6, 'products/reform-age-micro-touch-mask.webp'),
         home=('reformage-homecare', 5, 'products/reform-age-intensive-eye-cream.webp')),
    dict(c='#ab0a3d', short='Проблемная кожа', line='Acno Active',
         text='Уход за жирной и проблемной кожей, склонной к акне: очищение, баланс себума, ровный тон.',
         pro=('acnopro-jeuderm', 5, 'products/acno-clay-mask.webp'),
         home=('acnohome', 4, 'products/acno-active-gel-120ml.webp')),
    dict(c='#76bc21', short='Чувствительная кожа', line='Ato Care',
         text='Негормональный уход за сухой, чувствительной и реактивной кожей, в том числе склонной к дерматитам.',
         pro=('atocare-pro', 3, 'products/ato-care-moist-emulsion-150ml.webp'),
         home=('atocare-home', 4, 'products/ato-care-intensive-cream.webp')),
    dict(c='#65666b', short='ПРО-уход', line='ПРО',
         text='Препараты для кабинета вне линеек: маски, массажное масло, эксфолиант и гели для аппаратных процедур.',
         pro=('pro', 7, 'products/lift-intense-viso-contour.webp'), home=None),
    dict(c='#2b2a2c', short='Обновление кожи', line='Nova · Zymo',
         text='Трёхэтапные системы обновления с кислотами и энзимами — без агрессивного повреждения и реабилитации.',
         pro=('novazymo-exfoliation', 2, 'products/nova-complex.webp'), home=None),
    dict(c='#ae57b9', short='Кожа головы', line='Hair Genesis',
         text='Пептидный уход за кожей головы и волосами: при выпадении, истончении и замедленном росте волос.',
         pro=('hairgenesis?care=pro', 1, 'products/hair-growth-concentrate.webp'),
         home=('hairgenesis?care=home', 1, 'products/hair-genesis-stimulator.webp')),
]


def count_word(n):
    if n % 10 == 1 and n % 100 != 11:
        return '%d средство' % n
    if n % 10 in (2, 3, 4) and n % 100 not in (12, 13, 14):
        return '%d средства' % n
    return '%d средств' % n


def tile(i, d):
    modes = ' '.join(m for m in ('pro', 'home') if d[m])
    first = d['pro'] or d['home']
    attrs = ''
    for m in ('pro', 'home'):
        if d[m]:
            url, n, img = d[m]
            attrs += f' data-{m}-href="{SITE}{url}" data-{m}-img="{IMG}{img}" data-{m}-n="{count_word(n)}"'
    url, n, img = first
    return f'''      <a class="tl rv" style="--c:{d['c']}" data-care="{modes}" href="{SITE}{url}"{attrs}>
        <span class="tl-ph"><img src="{IMG}{img}" alt="{d['short']} — ЖеДерм {d['line']}" loading="lazy"><span class="tl-chip"><i></i>{d['line']}</span></span>
        <span class="tl-bd"><span class="code tl-n">{count_word(n)}</span><h3>{d['short']}</h3><p>{d['text']}</p><span class="more">Смотреть средства</span></span>
      </a>'''


def build():
    tpl = (ROOT / 'tools' / 'line_template.html').read_text(encoding='utf-8')
    base_css = re.search(r'<style>(.*?)</style>', tpl, re.S).group(1)
    # из шаблона линеек берём только общие стили: шрифты, кнопки, метки, CTA с картинкой, анимация
    keep = []
    for line in base_css.split('\n'):
        if re.match(r'\s*#jdl \.(card|grid|pr|procs|pd|tags|tag|seg|keys|dlg|x|meta|top|note|bar)\b', line) or 'dialog' in line or '@keyframes' in line:
            continue
        keep.append(line)
    css = '\n'.join(keep).replace('#jdl', '#jdh').replace('--c:#cd555b;', '--c:#cd555b;')
    css = re.sub(r'@media \(max-width:\d+px\)\{\s*\}', '', css)

    hub_css = f'''
/* ===== Хаб «Профессиональный / Домашний уход» ===== */
#jdh .hb{{padding-top:clamp(40px,5vw,72px)}}
#jdh .hb-g{{display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:clamp(32px,5vw,80px);align-items:center}}
#jdh .hb h1{{font-size:clamp(32px,3.6vw,52px);margin:20px 0 18px}}
#jdh .hb .lead{{font-size:16.5px;max-width:520px;margin-bottom:28px}}
#jdh .hb-img{{border-radius:4px;overflow:hidden;aspect-ratio:4/3;background:var(--soft)}}
#jdh .hb-img img{{width:100%;height:100%;object-fit:cover}}
#jdh .sw{{display:inline-flex;padding:4px;border:1px solid var(--line);border-radius:999px;margin-bottom:30px}}
#jdh .sw a{{padding:10px 20px;border-radius:999px;font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--gray);transition:background .3s,color .3s}}
#jdh .sw a[aria-current="page"]{{background:var(--ink);color:#fff}}
#jdh .sw a:not([aria-current="page"]):hover{{color:var(--ink)}}
#jdh[data-mode="pro"] [data-show="home"],#jdh[data-mode="home"] [data-show="pro"]{{display:none!important}}
#jdh .tls{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
#jdh[data-mode="home"] .tls{{grid-template-columns:repeat(4,1fr)}}
#jdh .tl{{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:4px;overflow:hidden;transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s}}
#jdh .tl[hidden]{{display:none}}
#jdh .tl:hover{{transform:translateY(-4px);box-shadow:0 22px 50px -40px rgba(60,40,40,.45)}}
#jdh .tl:before{{content:"";display:block;height:3px;background:var(--c)}}
#jdh .tl-ph{{position:relative;display:block;aspect-ratio:4/3;overflow:hidden;background:var(--soft)}}
#jdh .tl-ph img{{width:100%;height:100%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}}
#jdh .tl:hover .tl-ph img{{transform:scale(1.05)}}
#jdh .tl-chip{{position:absolute;left:12px;bottom:12px;display:inline-flex;align-items:center;gap:8px;padding:7px 12px;border-radius:999px;background:rgba(255,255,255,.9);font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}}
#jdh .tl-chip i{{width:8px;height:8px;border-radius:50%;background:var(--c)}}
#jdh .tl-bd{{display:flex;flex-direction:column;flex:1;padding:22px 22px 24px}}
#jdh .tl-bd h3{{margin:8px 0 10px}}
#jdh .tl-bd p{{font-size:14.5px;line-height:1.55;flex:1}}
#jdh .tl .more{{display:inline-flex;align-items:center;gap:10px;margin-top:18px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}}
#jdh .tl .more:after{{content:"→";color:var(--c);transition:transform .3s}}
#jdh .tl:hover .more:after{{transform:translateX(4px)}}
#jdh .tl:hover .tl-chip{{background:var(--c);color:#fff}}
#jdh .tl:hover .tl-chip i{{background:#fff}}
#jdh .steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;counter-reset:s}}
#jdh .st{{counter-increment:s;padding:28px 26px;border:1px solid var(--line);border-radius:4px;background:#fff}}
#jdh .st:before{{content:counter(s,decimal-leading-zero);display:block;font-family:var(--hf);font-size:30px;color:var(--c);margin-bottom:14px}}
#jdh .st h3{{margin-bottom:8px}}
#jdh .st p{{font-size:14.5px}}
#jdh .head{{display:block;margin-bottom:34px}}
#jdh .head h2{{margin-top:16px}}
#jdh .cta-img{{--bg:url('{IMG}home/skin-renewal.webp')}}
@media (max-width:1000px){{
  #jdh .hb-g,#jdh .cta{{grid-template-columns:1fr}}
  #jdh .tls,#jdh[data-mode="home"] .tls{{grid-template-columns:repeat(2,1fr)}}
  #jdh .steps{{grid-template-columns:1fr}}
}}
@media (max-width:640px){{
  #jdh .tls,#jdh[data-mode="home"] .tls{{grid-template-columns:1fr 1fr;gap:12px}}
  #jdh .tl-bd{{padding:14px}}
  #jdh .tl-bd h3{{font-size:16px}}
  #jdh .tl-bd p{{display:none}}
  #jdh .tl-chip{{left:8px;bottom:8px;padding:5px 8px;font-size:9px}}
  #jdh .tl .more{{margin-top:10px;font-size:11px}}
  #jdh .sw{{display:flex}}
  #jdh .sw a{{flex:1;text-align:center;padding:10px 6px;font-size:11px}}
}}
'''
    css = css.replace('</style>', '') + hub_css

    tiles = '\n'.join(tile(i, d) for i, d in enumerate(DIRS))
    body = f'''<div id="jdh" data-mode="pro">

<!-- ================= ШАПКА ================= -->
<section class="hb">
  <div class="w hb-g">
    <div>
      <nav class="sw rv" aria-label="Тип ухода">
        <a href="{SITE}pro-jeuderm" data-sw="pro">Профессиональный</a>
        <a href="{SITE}homecare-jeuderm" data-sw="home">Домашний</a>
      </nav>
      <span class="lab rv" data-show="pro"><i></i>Серия · Professional</span>
      <span class="lab rv" data-show="home"><i></i>Серия · Homecare</span>
      <h1 class="rv" data-show="pro">Профессиональный уход <em>ЖеДерм</em></h1>
      <h1 class="rv" data-show="home">Домашний уход <em>ЖеДерм</em></h1>
      <p class="lead rv" data-show="pro">Средства для процедур с пептидами и пробиотиками: восстанавливают, увлажняют и омолаживают кожу, усиливают результат аппаратных и ручных методик. Выберите задачу кожи — внутри препараты для кабинета и протоколы.</p>
      <p class="lead rv" data-show="home">Профессиональные формулы в формате ежедневного ухода: очищение, увлажнение и антивозрастной эффект. Средства продлевают результат процедуры дома и подходят для разных типов кожи, включая чувствительную.</p>
      <div class="btns rv">
        <a class="btn btn-a" href="#getprice_main">Запросить цены {ARROW}</a>
        <a class="btn btn-o" href="#getconsult" data-show="home">Подобрать уход</a>
        <a class="btn btn-o" href="#getprotocol" data-show="pro">Получить протоколы</a>
      </div>
    </div>
    <div class="hb-img rv">
      <img data-show="pro" src="{IMG}home/banner-professional.webp" alt="Профессиональный уход ЖеДерм: средства для процедур в кабинете" loading="eager">
      <img data-show="home" src="{IMG}home/banner-homecare.webp" alt="Домашний уход ЖеДерм: кремы, эмульсии и сыворотка для волос" loading="eager">
    </div>
  </div>
</section>

<!-- ================= НАПРАВЛЕНИЯ ================= -->
<section style="padding-top:clamp(48px,5vw,80px)">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Уход по задачам</span>
      <h2 data-show="pro">Выберите <em>задачу кожи</em></h2>
      <h2 data-show="home">Подберите <em>уход дома</em></h2>
    </div>
    <div class="tls">
{tiles}
    </div>
  </div>
</section>

<!-- ================= КАК РАБОТАЕМ ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Как это работает</span>
      <h2 data-show="pro">Для <em>косметологов</em> и клиник</h2>
      <h2 data-show="home">Уход <em>между визитами</em></h2>
    </div>
    <div class="steps" data-show="pro">
      <div class="st rv"><h3>Выберите линию</h3><p>Под задачу кожи: возрастной уход, проблемная или чувствительная кожа, обновление, кожа головы — или препараты ПРО.</p></div>
      <div class="st rv"><h3>Получите протоколы</h3><p>Пошаговые процедуры с дозировками и временем каждого шага — от атравматичной чистки до лифтинга 40+.</p></div>
      <div class="st rv"><h3>Пройдите обучение</h3><p>Бесплатные занятия в малых группах и вебинары: механизмы, показания и практика с продуктами ЖеДерм.</p></div>
    </div>
    <div class="steps" data-show="home">
      <div class="st rv"><h3>Процедура в кабинете</h3><p>Косметолог проводит процедуру на профессиональных средствах ЖеДерм.</p></div>
      <div class="st rv"><h3>Подбор домашнего ухода</h3><p>Специалист подбирает средства той же линии — для ежедневного очищения, увлажнения и защиты.</p></div>
      <div class="st rv"><h3>Результат держится дольше</h3><p>Домашний уход поддерживает кожу между визитами и продлевает эффект процедуры.</p></div>
    </div>
  </div>
</section>

<!-- ================= CTA ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="cta cta-img rv">
      <div>
        <h2 data-show="pro">Подберём средства для вашего кабинета</h2>
        <h2 data-show="home">Не знаете, с чего начать?</h2>
        <p data-show="pro">Пришлём прайс и протоколы, расскажем о бесплатном обучении. Новым клиентам — −15% на первый заказ.</p>
        <p data-show="home">Оставьте заявку — специалист подберёт домашний уход под задачу вашей кожи.</p>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="#getprice_main">Запросить цены</a>
        <a class="btn btn-o" href="#getconsult">Консультация</a>
      </div>
    </div>
  </div>
</section>

</div>'''

    script = '''<script>
(function(){
  var root=document.getElementById('jdh'); if(!root) return;
  var q=(location.search.match(/[?&]care=(pro|home)/)||[])[1];
  var page=location.pathname.replace(/\\/+$/,'').split('/').pop();
  var mode=q||(/home/.test(page)?'home':'pro');
  root.setAttribute('data-mode',mode);
  [].forEach.call(root.querySelectorAll('[data-sw]'),function(a){ if(a.dataset.sw===mode) a.setAttribute('aria-current','page'); });
  [].forEach.call(root.querySelectorAll('.tl'),function(t){
    if(t.dataset.care.split(' ').indexOf(mode)<0){ t.hidden=true; return; }
    t.href=t.getAttribute('data-'+mode+'-href');
    var img=t.querySelector('img'); img.src=t.getAttribute('data-'+mode+'-img');
    t.querySelector('.tl-n').textContent=t.getAttribute('data-'+mode+'-n');
  });
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''

    head = '''<!-- ЖеДерм · общая страница «Профессиональный уход / Домашний уход» · блок T123 «HTML-код».
     Один и тот же код ставится на /pro-jeuderm и /homecare-jeuderm: режим выбирается сам по адресу
     (или ?care=pro / ?care=home). Собрано tools/build_hub.py — правки текстов вносите там. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + css + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'care.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'care.txt').write_text(out, encoding='utf-8')
    print('care.html', len(out))
