#!/usr/bin/env python3
"""Страница 404 JeuDérm для Tilda, блок T123 (Настройки сайта → Ещё → Страница 404).

Запуск:  python3 tools/build_404.py  →  tilda/404.html и tilda-txt/404.txt
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, IMG, ARROW  # noqa: E402
from build_promo import CONTACTS, COLORS  # noqa: E402

import sys as _sys
_sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from localize import ru  # noqa: E402
ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'

DIRS = [
    ('#cd555b', 'Возрастной уход', 'Reform Age', 'reformage-pro'),
    ('#ab0a3d', 'Проблемная кожа', 'Acno Active', 'acnopro-jeuderm'),
    ('#76bc21', 'Чувствительная кожа', 'Ato Care', 'atocare-pro'),
    ('#65666b', 'ПРО-уход', 'ПРО', 'pro'),
    ('#2b2a2c', 'Обновление кожи', 'Nova · Zymo', 'novazymo-exfoliation'),
    ('#ae57b9', 'Кожа головы', 'Hair Genesis', 'hairgenesis'),
]

CSS = f'''
/* ===== 404 ===== */
#jds .e404{{padding:clamp(48px,7vw,110px) 0 clamp(56px,7vw,100px)}}
#jds .eg{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,5vw,80px);align-items:center}}
#jds .num{{position:relative;font-family:var(--hf);font-size:clamp(120px,17vw,240px);line-height:.9;letter-spacing:-.06em;color:var(--ink)}}
#jds .num em{{font-style:normal;color:var(--c)}}
#jds .e404 h1{{font-size:clamp(28px,3vw,42px);margin:22px 0 14px}}
#jds .e404 .lead{{font-size:16.5px;max-width:480px;margin-bottom:28px}}
#jds .eph{{position:relative;border-radius:6px;overflow:hidden;aspect-ratio:4/3.2;background:var(--soft)}}
#jds .eph img{{width:100%;height:100%;object-fit:cover}}
#jds .eph span{{position:absolute;left:14px;bottom:14px;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.92);font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}}
#jds .go{{margin-top:clamp(40px,5vw,64px)}}
#jds .go h2{{font-size:clamp(22px,2.2vw,30px);margin:14px 0 22px}}
#jds .dl{{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}}
#jds .di{{--k:var(--gray);display:flex;flex-direction:column;gap:6px;padding:18px 16px;border:1px solid var(--line);border-radius:4px;background:#fff;transition:transform .4s,border-color .3s}}
#jds .di:before{{content:"";width:28px;height:3px;background:var(--k);margin-bottom:8px}}
#jds .di:hover{{transform:translateY(-3px);border-color:var(--k)}}
#jds .di b{{font-weight:600;font-size:14.5px;color:var(--ink)}}
#jds .di span{{font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--k)}}
#jds .links{{display:flex;flex-wrap:wrap;gap:8px 22px;margin-top:22px}}
#jds .links a{{font-size:12.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink);border-bottom:1px solid var(--line);padding-bottom:3px;transition:color .3s,border-color .3s}}
#jds .links a:hover{{color:var(--c);border-color:var(--c)}}
#jds .msg{{display:flex;flex-wrap:wrap;gap:8px;margin-top:28px;align-items:center}}
#jds .msg p{{font-size:14px;margin-right:6px}}
#jds .msg a{{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid var(--line);border-radius:999px;font-size:12.5px;font-weight:600;color:var(--ink);transition:background .3s,color .3s,border-color .3s}}
#jds .msg a:hover{{background:var(--k);border-color:var(--k);color:#fff}}
#jds .msg svg{{width:16px;height:16px;fill:var(--k)}}
#jds .msg a:hover svg{{fill:#fff}}
@media (max-width:1000px){{#jds .eg{{grid-template-columns:1fr}}#jds .dl{{grid-template-columns:repeat(3,1fr)}}}}
@media (max-width:640px){{#jds .dl{{grid-template-columns:1fr 1fr}}}}
'''


def build():
    dl = '\n'.join(f'      <a class="di rv" style="--k:{c}" href="{SITE}{u}"><span>{line}</span><b>{t}</b></a>' for c, t, line, u in DIRS)
    msg = ''.join(f'<a href="{url}" style="--k:{COLORS[k]}"{"" if url.startswith(("tel:", "mailto:")) else " target=\"_blank\" rel=\"noopener\""}><svg viewBox="0 0 24 24" aria-hidden="true">{svg}</svg>{t}</a>'
                  for k, t, sub, url, svg in CONTACTS if k in ('wa', 'tg', 'tel'))
    body = f'''<div id="jds">
<section class="e404">
  <div class="w">
    <div class="eg">
      <div>
        <div class="num rv" aria-hidden="true">4<em>0</em>4</div>
        <h1 class="rv">Страница не найдена</h1>
        <p class="lead rv">Возможно, она переехала после обновления сайта или в адресе опечатка. Всё о профессиональной космецевтике JeuDérm — на главной и в разделах ухода.</p>
        <div class="btns rv">
          <a class="btn btn-a" href="{SITE}">На главную {ARROW}</a>
          <a class="btn btn-o" href="{SITE}pro-jeuderm">Профессиональный уход</a>
        </div>
      </div>
      <div class="eph rv">
        <img src="{IMG}home/skin-renewal.webp" alt="JeuDérm — обновление кожи" loading="eager">
        <span>JeuDérm · Южная Корея</span>
      </div>
    </div>

    <div class="go">
      <span class="lab rv"><i></i>Куда перейти</span>
      <h2 class="rv">Выберите <em>задачу кожи</em></h2>
      <div class="dl">
{dl}
      </div>
      <div class="links rv">
        <a href="{SITE}homecare-jeuderm">Домашний уход</a>
        <a href="{SITE}study">Обучение</a>
        <a href="{SITE}partners-distributors-jeuderm">Дистрибьюторам</a>
        <a href="{SITE}cosmeticru">Дом Русской Косметики</a>
      </div>
      <div class="msg rv"><p>Не нашли нужное? Напишите нам:</p>{msg}</div>
    </div>
  </div>
</section>
</div>'''
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.1});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''
    head = '''<!-- JeuDérm · страница 404 · блок T123. Собрано tools/build_404.py. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / '404.html').write_text(ru(out), encoding='utf-8')
    (ROOT / 'tilda-txt' / '404.txt').write_text(ru(out), encoding='utf-8')
    print('404.html', len(out))
