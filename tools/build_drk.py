#!/usr/bin/env python3
"""Страница партнёра «Дом Русской Косметики» (/cosmeticru) для Tilda, блок T123.

Запуск:  python3 tools/build_drk.py  →  tilda/cosmeticru.html и tilda-txt/cosmeticru.txt
Факты — только с текущей страницы /cosmeticru и из открытого каталога учебных заведений;
программы и цены не дублируем, ведём на сайт института.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, IMG, ARROW  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DRK = 'https://cosmeticru.com/kursy-kosmetologii'
ASK = '#popup:ask'
ACC = '#2b35d6'   # фирменный синий «Дома Русской Косметики»

AUD = [
    ('Для врачей-дерматологов', 'Программы профессиональной переподготовки и повышения квалификации по косметологии для врачей.'),
    ('Для практикующих косметологов', 'Повышение квалификации, новые методики и аппаратные технологии для тех, кто уже работает в профессии.'),
    ('Для специалистов с медицинским образованием', 'Программы для медсестёр и специалистов со средним медицинским образованием.'),
    ('Для слушателей без медицинского образования', 'Курсы эстетической косметологии и beauty-сферы для старта в профессии.'),
]

CSS = f'''
/* ===== Дом Русской Косметики ===== */
#jds{{--c:{ACC};--c-soft:#eef0ff}}
#jds .head{{display:block;margin-bottom:36px}}
#jds .head h2{{margin-top:16px}}
#jds .dk-top{{padding-top:clamp(40px,5vw,72px)}}
#jds .dk-g{{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(32px,5vw,80px);align-items:center}}
#jds .dk-top h1{{font-size:clamp(30px,3.4vw,50px);margin:20px 0 18px}}
#jds .dk-top .lead{{font-size:16.5px;max-width:560px;margin-bottom:28px}}
#jds .dk-card{{position:relative;overflow:hidden;border-radius:6px;padding:clamp(32px,4vw,52px);background:linear-gradient(135deg,{ACC} 0%,#4652ea 100%);color:#fff;isolation:isolate}}
#jds .dk-card:after{{content:"Курсы косметологии";position:absolute;left:-4%;bottom:-8%;z-index:-1;font-family:var(--hf);font-size:clamp(48px,6vw,92px);line-height:1;white-space:nowrap;color:rgba(255,255,255,.1)}}
#jds .dk-card .code{{color:rgba(255,255,255,.7)}}
#jds .dk-card b{{display:block;font-family:var(--hf);font-weight:400;font-size:clamp(56px,6vw,88px);line-height:1;margin:14px 0 6px}}
#jds .dk-card p{{color:rgba(255,255,255,.85);font-size:15px;max-width:360px}}
#jds .dk-card ul{{list-style:none;margin-top:26px;border-top:1px solid rgba(255,255,255,.25)}}
#jds .dk-card li{{padding:11px 0;border-bottom:1px solid rgba(255,255,255,.25);font-size:14px}}
#jds .aud{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;counter-reset:a}}
#jds .au{{counter-increment:a;padding:26px 24px;border:1px solid var(--line);border-radius:4px;background:#fff}}
#jds .au:before{{content:counter(a);display:grid;place-items:center;width:42px;height:42px;border-radius:50%;background:var(--c-soft);color:var(--c);font-weight:600;margin-bottom:18px}}
#jds .au h3{{font-size:18px;margin-bottom:10px;color:var(--c)}}
#jds .au p{{font-size:14px}}
#jds .why{{background:var(--soft)}}
#jds .wg{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
#jds .wi{{padding:28px 26px;background:#fff;border:1px solid var(--line);border-radius:4px}}
#jds .wi .k{{font-family:var(--hf);font-size:30px;color:var(--c);line-height:1.1}}
#jds .wi h3{{margin:12px 0 8px;font-size:18px}}
#jds .wi p{{font-size:14px}}
#jds .duo{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
#jds .duo>div{{padding:clamp(28px,3.5vw,44px);border:1px solid var(--line);border-radius:4px;background:#fff}}
#jds .duo h3{{margin:12px 0 12px}}
#jds .duo p{{font-size:14.5px;margin-bottom:20px}}
#jds .dk-cta{{border-radius:6px;padding:clamp(40px,5vw,72px) clamp(24px,5vw,64px);background:linear-gradient(135deg,{ACC} 0%,#4652ea 100%);color:rgba(255,255,255,.88);display:grid;grid-template-columns:1fr auto;gap:30px;align-items:center}}
#jds .dk-cta h2{{color:#fff;margin-bottom:12px}}
#jds .dk-cta .btn-a{{background:#fff;color:{ACC}}}
#jds .dk-cta .btn-a:hover{{background:#201f20;color:#fff}}
#jds .dk-cta .btn-o{{border-color:rgba(255,255,255,.55);color:#fff}}
#jds .dk-cta .btn-o:hover{{background:#fff;color:{ACC}}}
#jds .src{{margin-top:18px;font-size:12px;color:var(--gray)}}
@media (max-width:1000px){{
  #jds .dk-g,#jds .duo,#jds .dk-cta{{grid-template-columns:1fr}}
  #jds .aud{{grid-template-columns:repeat(2,1fr)}}
  #jds .wg{{grid-template-columns:1fr}}
}}
@media (max-width:640px){{#jds .aud{{grid-template-columns:1fr}}}}
'''


def build():
    aud = '\n'.join(f'      <div class="au rv"><h3>{t}</h3><p>{p}</p></div>' for t, p in AUD)
    body = f'''<div id="jds">

<!-- ================= ПЕРВЫЙ ЭКРАН ================= -->
<section class="dk-top">
  <div class="w dk-g">
    <div>
      <span class="lab rv"><i></i>Партнёр ЖеДерм по обучению</span>
      <h1 class="rv">Институт косметологии <em>«Дом Русской Косметики»</em></h1>
      <p class="lead rv">Обучение специалистов косметологии и сферы красоты. Программы для любого уровня подготовки — от базового до профессионального совершенствования. Курсы зарегистрированы в системе НМО Минздрава, а документы об окончании вносятся в ФИС ФРДО.</p>
      <div class="btns rv">
        <a class="btn btn-a" href="{DRK}" target="_blank" rel="noopener">Курсы и стоимость {ARROW}</a>
        <a class="btn btn-o" href="{ASK}">Задать вопрос</a>
      </div>
    </div>
    <div class="dk-card rv">
      <span class="code">Учебный центр в Москве</span>
      <b>с 1989</b>
      <p>Более 35 лет готовит врачей, косметологов и специалистов beauty-сферы.</p>
      <ul>
        <li>Документы государственного образца</li>
        <li>Внесение в ФИС ФРДО</li>
        <li>Регистрация программ в НМО Минздрава</li>
      </ul>
    </div>
  </div>
</section>

<!-- ================= ДЛЯ КОГО ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Для кого</span>
      <h2>Программы для <em>любого уровня</em> подготовки</h2>
    </div>
    <div class="aud">
{aud}
    </div>
  </div>
</section>

<!-- ================= ПОЧЕМУ ================= -->
<section class="why">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Почему «Дом Русской Косметики»</span>
      <h2>Обучение с <em>официальными документами</em></h2>
    </div>
    <div class="wg">
      <div class="wi rv"><span class="k">НМО</span><h3>Баллы непрерывного образования</h3><p>Курсы зарегистрированы в системе непрерывного медицинского образования Минздрава — для врачей и специалистов с медицинским образованием.</p></div>
      <div class="wi rv"><span class="k">ФИС ФРДО</span><h3>Документы в федеральном реестре</h3><p>Сведения о выданных документах вносятся в Федеральный реестр документов об образовании — их легко проверить.</p></div>
      <div class="wi rv"><span class="k">Очно и онлайн</span><h3>Удобный формат</h3><p>Очные занятия в учебных классах и дистанционные программы повышения квалификации и вебинары.</p></div>
    </div>
  </div>
</section>

<!-- ================= ЖЕДЕРМ + ДРК ================= -->
<section>
  <div class="w duo">
    <div class="rv">
      <span class="code">Обучение ЖеДерм</span>
      <h3>Работа с препаратами ЖеДерм</h3>
      <p>Бесплатные занятия по продукции ЖеДерм в малых группах, обучение в клиниках при запуске линии и вебинары по протоколам — от тренеров Революшн Био.</p>
      <a class="btn btn-o" href="https://jeuderm-russia.ru/study">Обучение ЖеДерм</a>
    </div>
    <div class="rv">
      <span class="code">Дом Русской Косметики</span>
      <h3>Базовое и дополнительное образование</h3>
      <p>Профессия косметолога с нуля, переподготовка и повышение квалификации с документами государственного образца — на программах института.</p>
      <a class="btn btn-o" href="{DRK}" target="_blank" rel="noopener">Все программы института</a>
    </div>
  </div>
</section>

<!-- ================= CTA ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="dk-cta rv">
      <div>
        <h2>Курсы косметологии</h2>
        <p>Посмотрите актуальные программы и их стоимость на сайте института «Дом Русской Косметики».</p>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="{DRK}" target="_blank" rel="noopener">Перейти на сайт {ARROW}</a>
        <a class="btn btn-o" href="{ASK}">Задать вопрос</a>
      </div>
    </div>
  </div>
</section>

</div>'''
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''
    head = '''<!-- ЖеДерм · страница партнёра «Дом Русской Косметики» (/cosmeticru) · блок T123. Собрано tools/build_drk.py. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'cosmeticru.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'cosmeticru.txt').write_text(out, encoding='utf-8')
    print('cosmeticru.html', len(out))
