#!/usr/bin/env python3
"""Страница «О компании» — ООО «Революшн Био», официальный дистрибьютор ЖеДерм. Блок T123.

Запуск:  python3 tools/build_about.py  →  tilda/about.html и tilda-txt/about.txt
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, IMG, ARROW  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'
LETTER = 'https://cdn.jsdelivr.net/gh/freyia-me/-@16606b2/images/home/distributor-letter.webp'

CSS = '''
/* ===== О компании ===== */
#jds .head{display:block;margin-bottom:34px}
#jds .head h2{margin-top:16px}
#jds .ab-top{padding-top:clamp(40px,5vw,72px)}
#jds .ab-g{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:clamp(32px,5vw,80px);align-items:center}
#jds .ab-top h1{font-size:clamp(32px,3.6vw,54px);margin:20px 0 18px}
#jds .ab-top .lead{font-size:16.5px;max-width:560px;margin-bottom:28px}
#jds .ab-ph{position:relative;border-radius:4px;overflow:hidden;aspect-ratio:4/3.3;background:var(--soft)}
#jds .ab-ph img{width:100%;height:100%;object-fit:cover}
#jds .ab-ph span{position:absolute;left:14px;bottom:14px;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.92);font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
#jds .nums{display:grid;grid-template-columns:repeat(3,1fr);margin-top:34px;border-top:1px solid var(--line)}
#jds .nums div{padding:18px 14px 0 0}
#jds .nums div+div{padding-left:18px;border-left:1px solid var(--line)}
#jds .nums b{display:block;font-family:var(--hf);font-weight:400;font-size:clamp(30px,3vw,42px);line-height:1;color:var(--ink)}
#jds .nums b sup{font-size:.45em;color:var(--c);vertical-align:top}
#jds .nums span{display:block;margin-top:8px;font-size:12.5px;line-height:1.4;color:var(--gray)}
/* письмо */
#jds .cert{background:var(--soft)}
#jds .cert-g{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:clamp(32px,5vw,80px);align-items:center}
#jds .doc{display:block;position:relative;max-width:420px;margin:0 auto;border-radius:3px;overflow:hidden;background:#fff;box-shadow:0 30px 70px -40px rgba(40,30,30,.45),0 0 0 1px var(--line);transform:rotate(-1.5deg);transition:transform .5s cubic-bezier(.2,.7,.2,1)}
#jds .doc:hover{transform:rotate(0) scale(1.02)}
#jds .doc img{width:100%}
#jds .doc span{position:absolute;right:12px;bottom:12px;padding:7px 12px;border-radius:999px;background:var(--ink);color:#fff;font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}
#jds .cert h2{margin:16px 0 18px}
#jds .cert blockquote{margin:0 0 22px;padding-left:18px;border-left:3px solid var(--c);font-family:var(--hf);font-size:clamp(18px,1.7vw,22px);line-height:1.5;color:var(--ink)}
#jds .cert dl{display:grid;grid-template-columns:auto 1fr;gap:10px 20px;margin-bottom:26px;font-size:14.5px}
#jds .cert dt{font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);padding-top:3px}
#jds .cert dd{color:var(--ink)}
/* что делаем */
#jds .do{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
#jds .di{padding:26px 22px;border:1px solid var(--line);border-radius:4px;background:#fff}
#jds .di:before{content:"";display:block;width:34px;height:3px;background:var(--k,var(--c));margin-bottom:18px}
#jds .di h3{font-size:18px;margin-bottom:8px}
#jds .di p{font-size:14px}
/* эксперт */
#jds .exp{display:grid;grid-template-columns:1.1fr .9fr;gap:20px}
#jds .quote{background:#4b343b;color:#fff;border-radius:4px;padding:clamp(32px,4vw,52px);display:flex;flex-direction:column;justify-content:space-between}
#jds .quote .code{color:rgba(255,255,255,.65)}
#jds .quote blockquote{font-family:var(--hf);font-size:clamp(19px,1.8vw,24px);line-height:1.5;margin:24px 0 32px}
#jds .quote .who{padding-top:20px;border-top:1px solid rgba(255,255,255,.25)}
#jds .quote .who b{display:block;font-weight:600;font-size:15px}
#jds .quote .who span{font-size:13px;color:rgba(255,255,255,.7)}
#jds .side{display:flex;flex-direction:column;gap:20px}
#jds .side>a,#jds .side>div{flex:1;padding:clamp(24px,3vw,36px);border:1px solid var(--line);border-radius:4px;background:#fff}
#jds .side h3{margin:10px 0 8px}
#jds .side p{font-size:14px}
#jds .side .more{display:inline-flex;margin-top:14px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
#jds .side .more:after{content:" →";color:var(--c);margin-left:6px}
/* реквизиты */
#jds .rq{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border:1px solid var(--line);border-radius:4px;background:#fff}
#jds .rq div{padding:22px 22px}
#jds .rq div+div{border-left:1px solid var(--line)}
#jds .rq dt{font-size:10.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--gray);margin-bottom:6px}
#jds .rq dd{font-size:14.5px;color:var(--ink)}
/* окно с письмом */
#jds .lb{position:fixed;inset:0;z-index:9999;display:none;align-items:center;justify-content:center;padding:24px;background:rgba(25,22,23,.8)}
#jds .lb.on{display:flex}
#jds .lb img{max-width:min(720px,100%);max-height:100%;background:#fff;border-radius:3px;box-shadow:0 30px 80px rgba(0,0,0,.5)}
#jds .lb button{position:absolute;right:18px;top:18px;width:44px;height:44px;border-radius:50%;border:0;background:#fff;font-size:22px;line-height:1;cursor:pointer}
#jds .cta-img{background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.95) 40%,rgba(255,255,255,.2) 78%,rgba(255,255,255,0) 100%),url('IMGhome/skin-renewal.webp') right center/cover;color:var(--text);border:1px solid var(--line)}
#jds .cta-img h2{color:var(--ink)}
#jds .cta-img .btn-a{background:var(--ink);color:#fff}
#jds .cta-img .btn-a:hover{background:var(--c)}
#jds .cta-img .btn-o{border-color:#c8c1bf;color:var(--ink)}
#jds .cta-img .btn-o:hover{background:var(--ink);color:#fff}
@media (max-width:1000px){
  #jds .ab-g,#jds .cert-g,#jds .exp,#jds .cta{grid-template-columns:1fr}
  #jds .do{grid-template-columns:1fr 1fr}
  #jds .rq{grid-template-columns:1fr 1fr}
  #jds .rq div:nth-child(3){border-left:0}
  #jds .rq div:nth-child(n+3){border-top:1px solid var(--line)}
  #jds .cta-img{background:linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.9) 60%,rgba(255,255,255,.6) 100%),url('IMGhome/skin-renewal.webp') center/cover}
}
@media (max-width:640px){
  #jds .nums{grid-template-columns:1fr}
  #jds .nums div,#jds .nums div+div{padding:14px 0;border-left:0;border-bottom:1px solid var(--line)}
  #jds .do,#jds .rq{grid-template-columns:1fr}
  #jds .rq div+div{border-left:0;border-top:1px solid var(--line)}
  #jds .cert dl{grid-template-columns:1fr;gap:2px}
  #jds .cert dd{margin-bottom:8px}
}
'''.replace('IMG', IMG)


def build():
    body = f'''<div id="jds">

<!-- ================= ПЕРВЫЙ ЭКРАН ================= -->
<section class="ab-top">
  <div class="w ab-g">
    <div>
      <span class="lab rv"><i></i>О компании</span>
      <h1 class="rv">«Революшн Био» — официальный дистрибьютор <em>ЖеДерм</em> в России</h1>
      <p class="lead rv">ООО «Революшн Био» представляет южнокорейский бренд профессиональной космецевтики JeuDérm на территории Российской Федерации: поставки, маркетинговая поддержка, логистика и обучение специалистов — напрямую от производителя, без посредников.</p>
      <div class="btns rv">
        <a class="btn btn-a" href="#getprice_main">Запросить цены {ARROW}</a>
        <a class="btn btn-o" href="#letter">Письмо производителя</a>
      </div>
      <div class="nums rv">
        <div><b>50 000<sup>+</sup></b><span>процедур на ЖеДерм в клиниках</span></div>
        <div><b>20<sup>+</sup></b><span>стран, где работают с брендом</span></div>
        <div><b>6</b><span>направлений ухода — ПРО и домашний</span></div>
      </div>
    </div>
    <div class="ab-ph rv">
      <img src="{IMG}study/symposium-hall-bags.webp" alt="Специалисты на международном симпозиуме JeuDérm" loading="eager">
      <span>JeuDérm · Южная Корея</span>
    </div>
  </div>
</section>

<!-- ================= ПИСЬМО ================= -->
<section class="cert" id="letter">
  <div class="w cert-g">
    <a class="doc rv" href="{LETTER}" data-lb><img src="{LETTER}" alt="Официальное подтверждение дистрибьютора JeuDérm в Российской Федерации от VIRTA-MED KOREA Co., LTD" loading="lazy"><span>Открыть</span></a>
    <div class="rv">
      <span class="lab"><i></i>Официальное подтверждение</span>
      <h2>Производитель подтверждает: <em>Revolution bio</em> — официальный дистрибьютор</h2>
      <blockquote>«Компания Revolution bio уполномочена представлять бренд JeuDérm, осуществлять продажи, маркетинговую поддержку и логистику на всей территории РФ».</blockquote>
      <dl>
        <dt>Производитель</dt><dd>VIRTA-MED KOREA Co., LTD · Тэджон, Южная Корея</dd>
        <dt>Подписано</dt><dd>CEO Tatyana Jeon</dd>
        <dt>Дата</dt><dd>01.11.2025</dd>
      </dl>
      <div class="btns">
        <a class="btn btn-o" href="{LETTER}" data-lb>Посмотреть письмо</a>
      </div>
    </div>
  </div>
</section>

<!-- ================= ЧТО ДЕЛАЕМ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Что мы делаем</span>
      <h2>Больше, чем <em>поставка</em> косметики</h2>
    </div>
    <div class="do">
      <div class="di rv" style="--k:#cd555b"><h3>Прямые поставки</h3><p>Оригинальная продукция JeuDérm напрямую от производителя — с документами, без посредников и подделок.</p></div>
      <div class="di rv" style="--k:#76bc21"><h3>Логистика по России</h3><p>Доставляем профессиональные и домашние средства клиникам, косметологам и партнёрам во всех регионах.</p></div>
      <div class="di rv" style="--k:#2a7de1"><h3>Обучение</h3><p>Бесплатные занятия в малых группах, обучение в клиниках, вебинары и международные симпозиумы JeuDérm.</p></div>
      <div class="di rv" style="--k:#ae57b9"><h3>Маркетинговая поддержка</h3><p>Протоколы, материалы и сопровождение для специалистов и дистрибьюторов в регионах.</p></div>
    </div>
  </div>
</section>

<!-- ================= ЭКСПЕРТ ================= -->
<section style="padding-top:0">
  <div class="w exp">
    <div class="quote rv">
      <div>
        <span class="code">Научный руководитель</span>
        <blockquote>«Работая в эстетической медицине более 20 лет, я перепробовала множество брендов, но именно ЖеДерм стал для меня настоящим открытием. Это не просто качественная косметика — это инструмент, который помогает достигать видимых и устойчивых результатов у клиентов».</blockquote>
      </div>
      <div class="who"><b>Лилия Мукарамова</b><span>Научный руководитель Revolution Bio, международный тренер</span></div>
    </div>
    <div class="side">
      <div class="rv">
        <span class="code">Наука</span>
        <h3>Клинически протестированные формулы</h3>
        <p>Эффективность средств JeuDérm подтверждена исследованиями в Дерматологическом центре Национального университета Чунгнам и в Университете Ханнам.</p>
      </div>
      <a class="rv" href="{SITE}cosmeticru">
        <span class="code">Партнёр по обучению</span>
        <h3>«Дом Русской Косметики»</h3>
        <p>Институт косметологии с 1989 года: программы с документами государственного образца, НМО и ФИС ФРДО.</p>
        <span class="more">Подробнее</span>
      </a>
    </div>
  </div>
</section>

<!-- ================= РЕКВИЗИТЫ ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Реквизиты</span>
      <h2>ООО «Революшн Био»</h2>
    </div>
    <dl class="rq rv">
      <div><dt>Адрес</dt><dd>105064, Москва, улица Земляной Вал, д. 7, кв./оф. помещ. 2/4</dd></div>
      <div><dt>ИНН</dt><dd>9709100594</dd></div>
      <div><dt>КПП</dt><dd>770901001</dd></div>
      <div><dt>ОГРН</dt><dd>1237700714085</dd></div>
    </dl>
  </div>
</section>

<!-- ================= CTA ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="cta cta-img rv">
      <div>
        <h2>Работайте с официальным дистрибьютором</h2>
        <p>Оригинальная продукция, обучение и поддержка. Новым клиентам — −15% на первый заказ.</p>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="#getprice_main">Запросить цены</a>
        <a class="btn btn-o" href="{SITE}partners-distributors-jeuderm">Стать партнёром</a>
      </div>
    </div>
  </div>
</section>

<div class="lb" role="dialog" aria-label="Письмо производителя"><button type="button" aria-label="Закрыть">×</button><img alt="Официальное подтверждение дистрибьютора JeuDérm" src="data:image/gif;base64,R0lGODlhAQABAAAAACw="></div>

</div>'''
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  var lb=root.querySelector('.lb'), im=lb.querySelector('img');
  function close(){lb.classList.remove('on');document.documentElement.style.overflow='';}
  [].forEach.call(root.querySelectorAll('[data-lb]'),function(a){a.addEventListener('click',function(e){
    e.preventDefault(); im.src=a.getAttribute('href'); lb.classList.add('on'); document.documentElement.style.overflow='hidden';});});
  lb.addEventListener('click',function(e){ if(e.target!==im) close(); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape') close(); });
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''
    head = '''<!-- ЖеДерм · страница «О компании» (Революшн Био) · блок T123. Собрано tools/build_about.py. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'about.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'about.txt').write_text(out, encoding='utf-8')
    print('about.html', len(out))
