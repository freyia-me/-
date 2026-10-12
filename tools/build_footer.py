#!/usr/bin/env python3
"""Общий подвал ЖеДерм для Tilda — отдельный блок T123, один код на все страницы.

Запуск:  python3 tools/build_footer.py  →  tilda/footer.html и tilda-txt/footer.txt
Ставится последним блоком страницы (вместо стандартного подвала Tilda) или в «Подвал» в настройках сайта.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_promo import CONTACTS, COLORS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'

COLS = [
    ('Уход', [('Профессиональный уход', 'pro-jeuderm'), ('Домашний уход', 'homecare-jeuderm'),
              ('Возрастной уход · Reform Age', 'reformage-pro'), ('Проблемная кожа · Acno', 'acnopro-jeuderm'),
              ('Чувствительная кожа · Ato Care', 'atocare-pro')]),
    ('Ещё', [('ПРО-препараты', 'pro'), ('Обновление · Nova · Zymo', 'novazymo-exfoliation'),
             ('Кожа головы · Hair Genesis', 'hairgenesis')]),
    ('Компания', [('Обучение', 'study'), ('Дистрибьюторам', 'partners-distributors-jeuderm'),
                  ('Дом Русской Косметики', 'cosmeticru')]),
]

CSS = '''
#jdf{--ink:#201f20;--acc:#cd555b;font-family:'Montserrat',Arial,sans-serif;background:#1d1c1e;color:rgba(255,255,255,.66);-webkit-font-smoothing:antialiased;font-size:14px;line-height:1.6;position:relative;overflow:hidden}
#jdf *{box-sizing:border-box;margin:0;padding:0}
#jdf a{color:inherit;text-decoration:none;transition:color .3s}
#jdf a:hover{color:#fff}
#jdf .w{max-width:1320px;margin:0 auto;padding:0 clamp(20px,4vw,58px)}
#jdf .sp{display:grid;grid-template-columns:repeat(6,1fr);height:3px}
#jdf .sp i:nth-child(1){background:#ab0a3d}#jdf .sp i:nth-child(2){background:#76bc21}#jdf .sp i:nth-child(3){background:#cd555b}
#jdf .sp i:nth-child(4){background:#ae57b9}#jdf .sp i:nth-child(5){background:#4a494c}#jdf .sp i:nth-child(6){background:#65666b}
#jdf .top{display:grid;grid-template-columns:1.25fr repeat(3,1fr) 1.2fr;gap:clamp(24px,3vw,48px);padding:clamp(48px,6vw,80px) 0 clamp(36px,4vw,56px)}
#jdf .logo{font-family:'Tenor Sans',Georgia,serif;font-size:34px;letter-spacing:-.02em;color:#fff;line-height:1}
#jdf .tagl{margin-top:14px;max-width:280px;font-size:13.5px}
#jdf .dist{display:inline-flex;align-items:center;gap:8px;margin-top:20px;padding:7px 12px;border:1px solid rgba(255,255,255,.18);border-radius:999px;font-size:10.5px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.8)}
#jdf .dist:before{content:"";width:6px;height:6px;border-radius:50%;background:var(--acc)}
#jdf h4{font-size:10.5px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#fff;margin-bottom:16px}
#jdf ul{list-style:none}
#jdf li+li{margin-top:9px}
#jdf .ct a{display:flex;align-items:center;gap:10px}
#jdf .ct a+a{margin-top:10px}
#jdf .ct b{font-weight:500;color:#fff}
#jdf .msg{display:flex;gap:8px;margin-top:18px}
#jdf .msg a{display:grid;place-items:center;width:40px;height:40px;border-radius:50%;background:rgba(255,255,255,.08);transition:background .3s}
#jdf .msg a:hover{background:var(--k)}
#jdf .msg svg{width:18px;height:18px;fill:#fff}
#jdf .bot{display:grid;grid-template-columns:1fr auto;gap:20px 40px;align-items:end;padding:26px 0 30px;border-top:1px solid rgba(255,255,255,.1);font-size:12px;color:rgba(255,255,255,.5)}
#jdf .bot p+p{margin-top:6px}
#jdf .req span{white-space:nowrap}
#jdf .req span+span:before{content:"·";margin:0 8px;color:rgba(255,255,255,.3)}
#jdf .up{display:inline-flex;align-items:center;gap:8px;font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:rgba(255,255,255,.7)}
#jdf .up:after{content:"↑";color:var(--acc)}
#jdf .wm{position:absolute;right:-1%;bottom:54px;font-family:'Tenor Sans',Georgia,serif;font-size:clamp(90px,14vw,220px);line-height:1;color:rgba(255,255,255,.03);pointer-events:none;white-space:nowrap}
@media (max-width:1000px){#jdf .top{grid-template-columns:1fr 1fr 1fr}#jdf .brand,#jdf .ct{grid-column:span 3}#jdf .ct{order:-1;display:none}}
@media (max-width:640px){
  #jdf .top{grid-template-columns:1fr 1fr;gap:28px 20px}
  #jdf .brand{grid-column:1/-1}
  #jdf .bot{grid-template-columns:1fr}
  #jdf .req span{white-space:normal}
  #jdf .req span+span:before{display:none}
  #jdf .req span{display:block}
}
'''


def build():
    cols = '\n'.join('''    <div>
      <h4>%s</h4>
      <ul>%s</ul>
    </div>''' % (t, ''.join('<li><a href="%s%s">%s</a></li>' % (SITE, u, n) for n, u in items)) for t, items in COLS)
    msg = ''.join(f'<a href="{url}" style="--k:{COLORS[k]}" aria-label="{t}"{"" if url.startswith(("tel:","mailto:")) else " target=\"_blank\" rel=\"noopener\""}><svg viewBox="0 0 24 24" aria-hidden="true">{svg}</svg></a>'
                  for k, t, sub, url, svg in CONTACTS if k in ('wa', 'tg', 'max'))
    contacts = f'''    <div class="cc">
      <h4>Связаться</h4>
      <div class="ct2">
        <a href="tel:+79253428202"><b>+7 925 342-82-02</b></a><br>
        <a href="mailto:info@revolution.bio">info@revolution.bio</a>
      </div>
      <div class="msg">{msg}</div>
    </div>'''
    body = f'''<footer id="jdf">
  <div class="sp" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
  <span class="wm" aria-hidden="true">JeuDérm</span>
  <div class="w">
    <div class="top">
      <div class="brand">
        <a class="logo" href="{SITE}">JeuDérm</a>
        <p class="tagl">Южнокорейская профессиональная космецевтика на основе пептидов и биотехнологий.</p>
        <span class="dist">Официальный дистрибьютор в России</span>
      </div>
{cols}
{contacts}
    </div>
    <div class="bot">
      <div>
        <p>© 2026 ООО «Революшн Био» — инновационные решения для профессиональной косметологии. Все права защищены.</p>
        <p>105064, Москва, улица Земляной Вал, д. 7, кв./оф. помещ. 2/4</p>
        <p class="req"><span>ИНН 9709100594</span><span>КПП 770901001</span><span>ОГРН 1237700714085</span></p>
      </div>
      <a class="up" href="#" onclick="window.scrollTo({{top:0,behavior:'smooth'}});return false;">Наверх</a>
    </div>
  </div>
</footer>'''
    css = CSS.replace("#jdf .ct a{display:flex;align-items:center;gap:10px}\n#jdf .ct a+a{margin-top:10px}\n#jdf .ct b{font-weight:500;color:#fff}",
                      "#jdf .ct2 a{display:inline-block;margin-bottom:8px}\n#jdf .ct2 b{font-weight:500;font-size:16px;color:#fff}")
    css = css.replace("@media (max-width:1000px){#jdf .top{grid-template-columns:1fr 1fr 1fr}#jdf .brand,#jdf .ct{grid-column:span 3}#jdf .ct{order:-1;display:none}}",
                      "@media (max-width:1000px){#jdf .top{grid-template-columns:1fr 1fr 1fr}#jdf .brand,#jdf .cc{grid-column:1/-1}}")
    head = '''<!-- ЖеДерм · общий подвал · блок T123 «HTML-код». Собрано tools/build_footer.py. Один код на все страницы. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + css + '</style>\n\n' + body + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'footer.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'footer.txt').write_text(out, encoding='utf-8')
    print('footer.html', len(out))
