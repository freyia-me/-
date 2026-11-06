#!/usr/bin/env python3
"""Страница-шпаргалка «Коды для Tilda»: все коды страниц с кнопкой «Скопировать».

Запуск: python3 tools/build_codes_page.py  → /tmp/.../codes.html (путь передаётся аргументом)
"""
import hashlib, json, pathlib, sys, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / 'codes.html'

GROUPS = [
  ('Основные страницы', [
    ('home', 'Главная', ['/']),
    ('care', 'Профессиональный и домашний уход', ['/pro-jeuderm', '/homecare-jeuderm']),
  ]),
  ('Линейки', [
    ('reformage', 'Реформэйдж · возрастной уход', ['/reformage-pro', '/reformage-homecare']),
    ('acno', 'Акно Актив · проблемная кожа', ['/acnopro-jeuderm', '/acnohome']),
    ('atocare', 'Ато Кэр · чувствительная кожа', ['/atocare-pro', '/atocare-home']),
    ('pro', 'ПРО · препараты для кабинета', ['/pro']),
    ('renew', 'Нова · Зимо · обновление кожи', ['/novazymo-exfoliation']),
    ('hairgenesis', 'Хэйр Генезис · кожа головы', ['/hairgenesis']),
  ]),
  ('Компания и обучение', [
    ('study', 'Обучение', ['/study']),
    ('partners', 'Дистрибьюторам', ['/partners-distributors-jeuderm']),
    ('cosmeticru', 'Дом Русской Косметики', ['/cosmeticru']),
    ('about', 'О компании', ['/about']),
    ('promo', 'Акции', ['/promo']),
    ('contacts', 'Контакты', ['/contacts']),
  ]),
  ('Общие блоки', [
    ('footer', 'Подвал', ['последним блоком на всех страницах']),
    ('404', 'Страница 404', ['/oops — и выбрать её в Настройках сайта → Ещё → Страница 404']),
  ]),
]

items = []
for g, rows in GROUPS:
    for slug, name, where in rows:
        code = (ROOT / 'tilda-txt' / f'{slug}.txt').read_text(encoding='utf-8')
        items.append(dict(group=g, slug=slug, name=name, where=where, code=code,
                          kb=round(len(code.encode()) / 1024), sum=hashlib.sha1(code.encode()).hexdigest()[:7]))

data = json.dumps({i['slug']: i['code'] for i in items}, ensure_ascii=False).replace('</', '<\\/')
today = datetime.date.today().strftime('%d.%m.%Y')

rows_html = []
cur = None
for i in items:
    if i['group'] != cur:
        if cur is not None:
            rows_html.append('</div></section>')
        cur = i['group']
        rows_html.append(f'<section class="grp"><h2>{cur}</h2><div class="list">')
    where = ''.join(f'<span class="url">{w}</span>' for w in i['where'])
    rows_html.append(f'''<article class="row" id="r-{i['slug']}">
  <div class="meta"><h3>{i['name']}</h3><div class="where">{where}</div>
    <div class="file"><span>tilda-txt/{i['slug']}.txt</span><span>{i['kb']} КБ</span><span title="Контрольная сумма версии">версия {i['sum']}</span></div></div>
  <div class="act"><button class="copy" type="button" data-slug="{i['slug']}" id="b-{i['slug']}">Скопировать код</button>
    <button class="show" type="button" data-slug="{i['slug']}" aria-expanded="false">Показать</button></div>
  <textarea class="code" id="t-{i['slug']}" readonly hidden spellcheck="false"></textarea>
</article>''')
rows_html.append('</div></section>')

page = f'''<title>Коды страниц JeuDérm</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<style>
/* Список кодов в духе сайта: светлый лист, цвета линеек как метки. */
:root{{--bg:#faf9f7;--card:#fff;--fg:#201f20;--muted:#6b6467;--line:#e8e3e1;--acc:#cd555b;--ok:#3f8f3a;--hf:'Tenor Sans',Georgia,serif;--tf:'Montserrat',Arial,sans-serif;--mf:'JetBrains Mono',ui-monospace,Menlo,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#181618;--card:#221f22;--fg:#efeae8;--muted:#a59da0;--line:#3a3437;--acc:#e07a7f;--ok:#7cc274;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#181618;--card:#221f22;--fg:#efeae8;--muted:#a59da0;--line:#3a3437;--acc:#e07a7f;--ok:#7cc274;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--tf);font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}}
.w{{max-width:980px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:40px 64px}}
header h1{{font-family:var(--hf);font-weight:400;font-size:clamp(28px,4vw,40px);letter-spacing:-.02em;margin:0 0 10px;text-wrap:balance}}
header p{{margin:0;color:var(--muted);max-width:62ch}}
.steps{{display:flex;flex-wrap:wrap;gap:8px 18px;margin:18px 0 0;padding:0;list-style:none;font-size:13.5px;color:var(--muted)}}
.steps li{{counter-increment:s}}
.steps li::before{{content:counter(s) ". ";color:var(--acc);font-weight:600}}
.grp{{margin-top:36px}}
.grp h2{{font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}}
.list{{display:grid;gap:10px}}
.row{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:10px 20px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:8px;padding:16px 18px}}
.meta{{min-width:0}}
.row h3{{font-family:var(--hf);font-weight:400;font-size:19px;margin:0 0 6px}}
.where{{display:flex;flex-wrap:wrap;gap:6px}}
.url{{font-family:var(--mf);font-size:12.5px;padding:2px 8px;border-radius:999px;background:color-mix(in srgb,var(--acc) 10%,transparent);color:var(--fg)}}
.file{{display:flex;flex-wrap:wrap;gap:4px 14px;margin-top:8px;font-size:12px;color:var(--muted);font-variant-numeric:tabular-nums}}
.act{{display:flex;gap:8px}}
button{{font:inherit;cursor:pointer;border-radius:6px;padding:11px 16px;font-size:12.5px;font-weight:600;letter-spacing:.04em;transition:background .2s,color .2s,border-color .2s}}
.copy{{background:var(--fg);color:var(--bg);border:1px solid var(--fg);min-width:178px}}
.copy:hover{{background:var(--acc);border-color:var(--acc);color:#fff}}
.copy.done{{background:var(--ok);border-color:var(--ok);color:#fff}}
.show{{background:transparent;color:var(--fg);border:1px solid var(--line)}}
.show:hover{{border-color:var(--fg)}}
button:focus-visible,textarea:focus-visible{{outline:2px solid var(--acc);outline-offset:2px}}
.code{{grid-column:1/-1;width:100%;box-sizing:border-box;height:260px;font-family:var(--mf);font-size:12px;line-height:1.5;color:var(--fg);background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:12px;resize:vertical;white-space:pre;overflow:auto}}
.hint{{grid-column:1/-1;font-size:12.5px;color:var(--acc);margin:0}}
footer{{margin-top:36px;font-size:12.5px;color:var(--muted)}}
@media (max-width:640px){{.row{{grid-template-columns:1fr}}.act{{flex-wrap:wrap}}.copy{{flex:1}}}}
@media (prefers-reduced-motion:reduce){{button{{transition:none}}}}
</style>
<div class="w">
<header>
  <h1>Коды страниц JeuDérm</h1>
  <p>Актуальные коды всех страниц сайта для вставки в Tilda. Один код — один блок «HTML-код» (T123). Обновлено {today}.</p>
  <ol class="steps"><li>Нажмите «Скопировать код»</li><li>В Tilda откройте блок T123 → «Контент»</li><li>Выделите старый код, вставьте новый, сохраните</li><li>Опубликуйте страницу</li></ol>
</header>
{''.join(rows_html)}
<footer>Код страниц линеек ставится на оба адреса — режим «профессиональный / домашний» страница выбирает сама. Контрольная сумма «версия» меняется при каждом обновлении кода: так видно, какая версия у вас в Tilda.</footer>
</div>
<script type="application/json" id="codes">{data}</script>
<script>
(function(){{
  var CODES = JSON.parse(document.getElementById('codes').textContent);
  function area(slug){{ var t=document.getElementById('t-'+slug); if(!t.value) t.value=CODES[slug]; return t; }}
  function hint(row,msg){{ var h=row.querySelector('.hint'); if(!h){{h=document.createElement('p');h.className='hint';row.appendChild(h);}} h.textContent=msg; }}
  document.addEventListener('click', function(e){{
    var b=e.target.closest('button'); if(!b) return; var slug=b.dataset.slug, row=b.closest('.row');
    if(b.classList.contains('show')){{ var t=area(slug); t.hidden=!t.hidden; b.textContent=t.hidden?'Показать':'Скрыть'; b.setAttribute('aria-expanded',String(!t.hidden)); return; }}
    if(b.classList.contains('copy')){{
      var ok=function(){{ b.classList.add('done'); b.textContent='Скопировано ✓'; setTimeout(function(){{b.classList.remove('done');b.textContent='Скопировать код';}},2200); }};
      var fallback=function(){{ var t=area(slug); t.hidden=false; row.querySelector('.show').textContent='Скрыть'; t.focus(); t.select();
        var done=false; try{{ done=document.execCommand('copy'); }}catch(_){{}}
        if(done) ok(); else hint(row,'Код выделен — нажмите Ctrl+C (на Mac — Cmd+C).'); }};
      if(navigator.clipboard && navigator.clipboard.writeText){{ navigator.clipboard.writeText(CODES[slug]).then(ok, fallback); }} else fallback();
    }}
  }});
}})();
</script>
'''
OUT.write_text(page, encoding='utf-8')
print(OUT, round(len(page.encode()) / 1024), 'KB')
