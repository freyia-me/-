#!/usr/bin/env python3
"""Страница «Контакты» ЖеДерм для Tilda, блок T123.

Запуск:  python3 tools/build_contacts.py  →  tilda/contacts.html и tilda-txt/contacts.txt
"""
import pathlib
import sys
import urllib.parse

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, ARROW  # noqa: E402
from build_promo import CONTACTS, COLORS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'
ADDR = '105064, Москва, улица Земляной Вал, д. 7, кв./оф. помещ. 2/4'
MAP_Q = 'Москва, улица Земляной Вал, 7'
MAP = 'https://yandex.ru/map-widget/v1/?text=' + urllib.parse.quote(MAP_Q) + '&z=16'
MAP_LINK = 'https://yandex.ru/maps/?text=' + urllib.parse.quote(MAP_Q)

CSS = '''
/* ===== Контакты ===== */
#jds .head{display:block;margin-bottom:32px}
#jds .head h2{margin-top:16px}
#jds .ct-top{padding-top:clamp(40px,5vw,72px)}
#jds .ct-top h1{font-size:clamp(32px,3.6vw,54px);margin:20px 0 16px;max-width:720px}
#jds .ct-top .lead{font-size:16.5px;max-width:600px}
#jds .main{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:20px;margin-top:clamp(32px,4vw,48px)}
#jds .card{padding:clamp(28px,3.5vw,44px);border:1px solid var(--line);border-radius:6px;background:#fff}
#jds .card .code{display:block;margin-bottom:14px}
#jds .ph{display:block;font-family:var(--hf);font-size:clamp(30px,3.2vw,44px);line-height:1.1;color:var(--ink);transition:color .3s}
#jds .ph:hover{color:var(--c)}
#jds .ml{display:inline-block;margin-top:12px;font-size:18px;color:var(--ink);border-bottom:1px solid var(--line);transition:color .3s,border-color .3s}
#jds .ml:hover{color:var(--c);border-color:var(--c)}
#jds .msg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:28px}
#jds .msg a{display:flex;align-items:center;gap:10px;padding:13px 14px;border:1px solid var(--line);border-radius:999px;font-size:13px;font-weight:600;color:var(--ink);transition:background .3s,color .3s,border-color .3s}
#jds .msg a:hover{background:var(--k);border-color:var(--k);color:#fff}
#jds .msg i{display:grid;place-items:center;flex:none;width:30px;height:30px;border-radius:50%;background:var(--k);color:#fff}
#jds .msg a:hover i{background:rgba(255,255,255,.2)}
#jds .msg svg{width:16px;height:16px;fill:currentColor}
#jds .card .btns{margin-top:28px}
#jds .req{background:var(--soft)}
#jds .req dl{display:grid;grid-template-columns:auto 1fr;gap:12px 22px;margin-top:6px}
#jds .req dt{font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);padding-top:3px}
#jds .req dd{font-size:15px;color:var(--ink)}
#jds .req h3{margin-bottom:18px}
#jds .copy{display:inline-flex;align-items:center;gap:8px;margin-top:22px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);cursor:pointer;background:none;border:0}
#jds .copy:after{content:"⧉";color:var(--c)}
#jds .map{position:relative;border-radius:6px;overflow:hidden;border:1px solid var(--line);aspect-ratio:21/8;background:var(--soft)}
#jds .map iframe{position:absolute;inset:0;width:100%;height:100%;border:0;filter:grayscale(.35)}
#jds .map-f{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-top:16px;font-size:14.5px;color:var(--ink)}
#jds .who{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
#jds .wi{display:flex;flex-direction:column;padding:26px 24px;border:1px solid var(--line);border-radius:4px;background:#fff}
#jds .wi:before{content:"";width:34px;height:3px;background:var(--k,var(--c));margin-bottom:18px}
#jds .wi h3{font-size:18px;margin-bottom:8px}
#jds .wi p{font-size:14px;flex:1}
#jds .wi .more{margin-top:18px;display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
#jds .wi .more:after{content:"→";color:var(--k,var(--c))}
@media (max-width:1000px){#jds .main{grid-template-columns:1fr}#jds .who{grid-template-columns:1fr}#jds .map{aspect-ratio:4/3}}
@media (max-width:640px){#jds .msg{grid-template-columns:1fr}#jds .req dl{grid-template-columns:1fr;gap:2px}#jds .req dd{margin-bottom:10px}}
'''


def build():
    msg = ''.join(f'<a href="{url}" style="--k:{COLORS[k]}" target="_blank" rel="noopener"><i><svg viewBox="0 0 24 24" aria-hidden="true">{svg}</svg></i>{t}</a>'
                  for k, t, sub, url, svg in CONTACTS if k in ('wa', 'tg', 'max'))
    body = f'''<div id="jds">

<!-- ================= ШАПКА ================= -->
<section class="ct-top">
  <div class="w">
    <span class="lab rv"><i></i>Контакты</span>
    <h1 class="rv">Свяжитесь с <em>ЖеДерм</em></h1>
    <p class="lead rv">ООО «Революшн Био» — официальный дистрибьютор ЖеДерм (JeuDérm) в России. Подберём средства, пришлём прайс и протоколы, запишем на обучение.</p>

    <div class="main">
      <div class="card rv">
        <span class="code">Телефон и почта</span>
        <a class="ph" href="tel:+79253428202">+7 925 342-82-02</a>
        <a class="ml" href="mailto:info@revolution.bio">info@revolution.bio</a>
        <div class="msg">{msg}</div>
        <div class="btns">
          <a class="btn btn-a" href="#popup:ask">Задать вопрос {ARROW}</a>
          <a class="btn btn-o" href="#getprice_main">Запросить цены</a>
        </div>
      </div>
      <div class="card req rv">
        <h3>Реквизиты</h3>
        <dl>
          <dt>Компания</dt><dd>ООО «Революшн Био»</dd>
          <dt>Адрес</dt><dd>{ADDR}</dd>
          <dt>ИНН</dt><dd>9709100594</dd>
          <dt>КПП</dt><dd>770901001</dd>
          <dt>ОГРН</dt><dd>1237700714085</dd>
        </dl>
        <button type="button" class="copy" data-copy="ООО «Революшн Био»&#10;{ADDR}&#10;ИНН 9709100594, КПП 770901001, ОГРН 1237700714085">Скопировать реквизиты</button>
      </div>
    </div>
  </div>
</section>

<!-- ================= КАРТА ================= -->
<section style="padding-top:clamp(40px,5vw,72px)">
  <div class="w">
    <div class="map rv"><iframe src="{MAP}" title="ЖеДерм на карте: {MAP_Q}" loading="lazy" allowfullscreen></iframe></div>
    <div class="map-f rv"><span>{ADDR}</span><a class="btn btn-o" href="{MAP_LINK}" target="_blank" rel="noopener">Открыть в Яндекс Картах</a></div>
  </div>
</section>

<!-- ================= ПО ВОПРОСАМ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>По вопросам</span>
      <h2>Куда <em>обратиться</em></h2>
    </div>
    <div class="who">
      <div class="wi rv" style="--k:#cd555b"><h3>Косметологам и клиникам</h3><p>Прайс, подбор средств под задачу кожи, протоколы процедур и скидка −15% на первый заказ.</p><a class="more" href="#getprice_main">Запросить цены</a></div>
      <div class="wi rv" style="--k:#76bc21"><h3>Обучение</h3><p>График семинаров в малых группах, обучение в клинике и записи вебинаров — по запросу.</p><a class="more" href="#popup:registerstudy">Узнать график</a></div>
      <div class="wi rv" style="--k:#29282a"><h3>Дистрибьюторам</h3><p>Условия партнёрства, прайс для партнёров и материалы для запуска в вашем регионе.</p><a class="more" href="{SITE}partners-distributors-jeuderm">Стать партнёром</a></div>
    </div>
  </div>
</section>

</div>'''
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  [].forEach.call(root.querySelectorAll('[data-copy]'),function(b){
    b.addEventListener('click',function(){
      var t=b.getAttribute('data-copy'), done=function(){var o=b.textContent;b.textContent='Скопировано';setTimeout(function(){b.textContent=o;},1800);};
      if(navigator.clipboard) navigator.clipboard.writeText(t).then(done,function(){});
    });
  });
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''
    head = '''<!-- ЖеДерм · страница «Контакты» · блок T123. Собрано tools/build_contacts.py. Попапы: #popup:ask, #getprice_main, #popup:registerstudy. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'contacts.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'contacts.txt').write_text(out, encoding='utf-8')
    print('contacts.html', len(out))
