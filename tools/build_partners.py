#!/usr/bin/env python3
"""Страница для дистрибьюторов ЖеДерм (/partners-distributors-jeuderm), блок T123.

Запуск:  python3 tools/build_partners.py  →  tilda/partners.html и tilda-txt/partners.txt
Попапы Tilda: #getprice_partner (прайс для партнёров), #getprotocol_partner (протоколы / материалы).
Карточка октябрьской акции скрывается сама после DISTR_UNTIL (как на странице акций).
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, IMG, ARROW  # noqa: E402
from build_promo import CONTACTS, COLORS, DISTR_UNTIL, DISTR_UNTIL_T  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'
PRICE = '#getprice_partner'
PROTO = '#getprotocol_partner'

DIRS = [
    ('#cd555b', 'Возрастной уход', 'Reform Age', 'reformage-pro', 'products/reform-age-o2-boto-fluid-110ml.webp'),
    ('#ab0a3d', 'Проблемная кожа', 'Acno Active', 'acnopro-jeuderm', 'products/acno-active-emulsion-150ml.webp'),
    ('#76bc21', 'Чувствительная кожа', 'Ato Care', 'atocare-pro', 'products/ato-care-mild-cleanser.webp'),
    ('#65666b', 'ПРО-уход', 'ПРО', 'pro', 'products/lift-intense-viso-contour.webp'),
    ('#2b2a2c', 'Обновление кожи', 'Nova · Zymo', 'novazymo-exfoliation', 'products/nova-complex.webp'),
    ('#ae57b9', 'Кожа головы', 'Hair Genesis', 'hairgenesis', 'products/hair-genesis-stimulator.webp'),
]

CSS = '''
/* ===== Дистрибьюторам ===== */
#jds .head{display:block;margin-bottom:36px}
#jds .head h2{margin-top:16px}
#jds .head .lead{margin-top:14px;font-size:16.5px}
#jds .pt-top{padding-top:clamp(40px,5vw,72px)}
#jds .pt-g{display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:clamp(32px,5vw,80px);align-items:center}
#jds .pt-top h1{font-size:clamp(32px,3.6vw,54px);margin:20px 0 18px}
#jds .pt-top .lead{font-size:16.5px;max-width:540px;margin-bottom:28px}
#jds .pt-ph{position:relative;border-radius:4px;overflow:hidden;aspect-ratio:4/3.4;background:var(--soft)}
#jds .pt-ph img{width:100%;height:100%;object-fit:cover;object-position:50% 70%}
#jds .pt-ph span{position:absolute;left:14px;bottom:14px;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.92);font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
#jds .nums{display:grid;grid-template-columns:repeat(3,1fr);margin-top:34px;border-top:1px solid var(--line)}
#jds .nums div{padding:18px 14px 0 0}
#jds .nums div+div{padding-left:18px;border-left:1px solid var(--line)}
#jds .nums b{display:block;font-family:var(--hf);font-weight:400;font-size:clamp(30px,3vw,42px);line-height:1;color:var(--ink)}
#jds .nums b sup{font-size:.45em;color:var(--c);vertical-align:top}
#jds .nums span{display:block;margin-top:8px;font-size:12.5px;line-height:1.4;color:var(--gray)}
/* октябрьская акция */
#jds .deal{display:grid;grid-template-columns:1fr auto;gap:30px;align-items:center;padding:clamp(28px,4vw,44px) clamp(24px,4vw,52px);border-radius:6px;background:#29282a;color:rgba(255,255,255,.82);position:relative;overflow:hidden;isolation:isolate}
#jds .deal:after{content:"";position:absolute;right:-70px;top:-90px;width:280px;height:280px;border-radius:50%;border:1px solid rgba(255,255,255,.16);box-shadow:0 0 0 34px rgba(255,255,255,.04);z-index:-1}
#jds .deal[hidden]{display:none}
#jds .deal .tag{display:inline-block;padding:7px 13px;border-radius:999px;background:rgba(255,255,255,.12);color:#fff;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase}
#jds .deal h2{color:#fff;margin:16px 0 10px;font-size:clamp(24px,2.6vw,36px)}
#jds .deal p{font-size:15px;max-width:620px}
#jds .deal .left{display:inline-flex;align-items:center;gap:8px;margin-top:14px;font-size:12.5px;color:rgba(255,255,255,.7)}
#jds .deal .left b{font-family:var(--hf);font-weight:400;font-size:22px;color:#fff}
#jds .deal .btn-a{background:var(--c)}
#jds .deal .btn-a:hover{background:#fff;color:var(--ink)}
#jds .deal .btn-o{border-color:rgba(255,255,255,.45);color:#fff}
#jds .deal .btn-o:hover{background:#fff;color:var(--ink)}
/* выгоды */
#jds .bn{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
#jds .bi{padding:28px 26px;border:1px solid var(--line);border-radius:4px;background:#fff}
#jds .bi:before{content:"";display:block;width:36px;height:3px;background:var(--c);margin-bottom:20px}
#jds .bi h3{font-size:18px;margin-bottom:8px}
#jds .bi p{font-size:14px}
/* портфель */
#jds .pf{display:grid;grid-template-columns:repeat(6,1fr);gap:12px}
#jds .pfi{--k:var(--gray);display:flex;flex-direction:column;border:1px solid var(--line);border-radius:4px;overflow:hidden;background:#fff;transition:transform .45s}
#jds .pfi:hover{transform:translateY(-3px)}
#jds .pfi:before{content:"";height:3px;background:var(--k)}
#jds .pfi img{width:100%;aspect-ratio:1/1;object-fit:cover}
#jds .pfi span{padding:12px 14px 14px;font-size:13.5px;line-height:1.35;color:var(--ink)}
#jds .pfi small{display:block;margin-top:3px;font-size:10.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--k)}
/* шаги */
#jds .steps-s{background:var(--soft)}
#jds .sg{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;counter-reset:s}
#jds .si{counter-increment:s;padding:26px 22px;background:#fff;border:1px solid var(--line);border-radius:4px}
#jds .si:before{content:counter(s,decimal-leading-zero);display:block;font-family:var(--hf);font-size:30px;color:var(--c);margin-bottom:12px}
#jds .si h3{font-size:18px;margin-bottom:8px}
#jds .si p{font-size:14px}
/* связь */
#jds .cn{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
#jds .ci{display:flex;flex-direction:column;align-items:flex-start;gap:14px;padding:22px 20px;border:1px solid var(--line);border-radius:4px;background:#fff;transition:transform .4s,border-color .3s}
#jds .ci:hover{transform:translateY(-3px);border-color:var(--k)}
#jds .ci i{display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--k);color:#fff}
#jds .ci svg{width:22px;height:22px;fill:currentColor}
#jds .ci b{font-weight:600;font-size:15px;color:var(--ink)}
#jds .ci span{font-size:13px;color:var(--gray);word-break:break-word}
#jds .cta-img{background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.95) 40%,rgba(255,255,255,.2) 78%,rgba(255,255,255,0) 100%),url('IMGhome/skin-renewal.webp') right center/cover;color:var(--text);border:1px solid var(--line)}
#jds .cta-img h2{color:var(--ink)}
#jds .cta-img .btn-a{background:var(--ink);color:#fff}
#jds .cta-img .btn-a:hover{background:var(--c)}
#jds .cta-img .btn-o{border-color:#c8c1bf;color:var(--ink)}
#jds .cta-img .btn-o:hover{background:var(--ink);color:#fff}
@media (max-width:1000px){
  #jds .pt-g,#jds .deal,#jds .cta{grid-template-columns:1fr}
  #jds .bn{grid-template-columns:1fr 1fr}
  #jds .pf{grid-template-columns:repeat(3,1fr)}
  #jds .sg{grid-template-columns:1fr 1fr}
  #jds .cn{grid-template-columns:repeat(3,1fr)}
  #jds .cta-img{background:linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.9) 60%,rgba(255,255,255,.6) 100%),url('IMGhome/skin-renewal.webp') center/cover}
}
@media (max-width:640px){
  #jds .nums{grid-template-columns:1fr}
  #jds .nums div,#jds .nums div+div{padding:14px 0;border-left:0;border-bottom:1px solid var(--line)}
  #jds .bn,#jds .sg{grid-template-columns:1fr}
  #jds .pf{grid-template-columns:1fr 1fr;gap:10px}
  #jds .cn{grid-template-columns:1fr 1fr;gap:10px}
  #jds .ci{padding:16px 14px}
}
'''.replace('IMG', IMG)


def build():
    pf = '\n'.join(f'      <a class="pfi rv" style="--k:{c}" href="{SITE}{url}"><img src="{IMG}{img}" alt="{t} — ЖеДерм {line}" loading="lazy"><span>{t}<small>{line}</small></span></a>'
                   for c, t, line, url, img in DIRS)
    cn = '\n'.join(f'''      <a class="ci rv" style="--k:{COLORS[k]}" href="{url}"{'' if url.startswith(('tel:', 'mailto:')) else ' target="_blank" rel="noopener"'}><i><svg viewBox="0 0 24 24" aria-hidden="true">{svg}</svg></i><b>{t}</b><span>{sub}</span></a>'''
                   for k, t, sub, url, svg in CONTACTS)
    body = f'''<div id="jds">

<!-- ================= ПЕРВЫЙ ЭКРАН ================= -->
<section class="pt-top">
  <div class="w pt-g">
    <div>
      <span class="lab rv"><i></i>Дистрибьюторам и партнёрам</span>
      <h1 class="rv">Станьте партнёром <em>ЖеДерм</em> в вашем регионе</h1>
      <p class="lead rv">Южнокорейская профессиональная космецевтика на основе пептидов и биотехнологий. Работаем с дистрибьюторами, клиниками эстетической медицины и косметологическими центрами — напрямую от официального дистрибьютора в России, ООО «Революшн Био».</p>
      <div class="btns rv">
        <a class="btn btn-a" href="{PRICE}">Получить прайс для партнёров {ARROW}</a>
        <a class="btn btn-o" href="{PROTO}">Протоколы и материалы</a>
      </div>
      <div class="nums rv">
        <div><b>50 000<sup>+</sup></b><span>процедур в клиниках и центрах</span></div>
        <div><b>20<sup>+</sup></b><span>стран, где работают с ЖеДерм</span></div>
        <div><b>6</b><span>направлений ухода — ПРО и домашний</span></div>
      </div>
    </div>
    <div class="pt-ph rv">
      <img src="{IMG}study/symposium-group-dubrovnik.webp" alt="Партнёры и специалисты ЖеДерм на международном симпозиуме в Дубровнике" loading="eager">
      <span>International Aesthetic Symposium · 2026</span>
    </div>
  </div>
</section>

<!-- ================= АКЦИЯ ОКТЯБРЯ ================= -->
<section style="padding-top:0;padding-bottom:0" data-until-wrap>
  <div class="w">
    <div class="deal rv" data-until="{DISTR_UNTIL}">
      <div>
        <span class="tag">До {DISTR_UNTIL_T}</span>
        <h2>Специальные условия для новых дистрибьюторов</h2>
        <p>До конца октября — особые условия старта для новых партнёров. Оставьте заявку: менеджер расскажет подробности и подготовит предложение для вашего региона.</p>
        <span class="left" data-left hidden>Осталось <b></b></span>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="{PRICE}">Узнать условия {ARROW}</a>
        <a class="btn btn-o" href="https://wa.me/79253428202" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<!-- ================= ВЫГОДЫ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Что получает партнёр</span>
      <h2>Почему <em>ЖеДерм</em></h2>
    </div>
    <div class="bn">
      <div class="bi rv"><h3>Оригинальная продукция</h3><p>Прямые поставки от официального дистрибьютора в России — без посредников, с документами на всю продукцию.</p></div>
      <div class="bi rv"><h3>Полный портфель</h3><p>Шесть направлений ухода: препараты для кабинета и домашний уход. Клиенты возвращаются за средствами между процедурами.</p></div>
      <div class="bi rv"><h3>Доказанная эффективность</h3><p>Формулы протестированы в Дерматологическом центре Национального университета Чунгнам и в Университете Ханнам.</p></div>
      <div class="bi rv"><h3>Обучение вашей команды</h3><p>Бесплатное обучение специалистов, протоколы процедур, вебинары и участие в международных симпозиумах ЖеДерм.</p></div>
      <div class="bi rv"><h3>Маркетинговая поддержка</h3><p>Фото продуктов, описания, материалы для соцсетей и презентации для работы с клиниками и косметологами.</p></div>
      <div class="bi rv"><h3>Персональный менеджер</h3><p>Помогаем с запуском, ассортиментом и первыми продажами в регионе. Условия растут вместе с объёмом закупок.</p></div>
    </div>
  </div>
</section>

<!-- ================= ПОРТФЕЛЬ ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Портфель</span>
      <h2>Шесть направлений <em>ухода</em></h2>
    </div>
    <div class="pf">
{pf}
    </div>
  </div>
</section>

<!-- ================= ШАГИ ================= -->
<section class="steps-s">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Как начать</span>
      <h2>Четыре шага до <em>партнёрства</em></h2>
    </div>
    <div class="sg">
      <div class="si rv"><h3>Заявка</h3><p>Оставьте заявку или напишите в мессенджер — расскажите о регионе и вашей компании.</p></div>
      <div class="si rv"><h3>Предложение</h3><p>Менеджер пришлёт прайс для партнёров и условия сотрудничества.</p></div>
      <div class="si rv"><h3>Договор и первая поставка</h3><p>Подбираем стартовый ассортимент под рынок региона и оформляем поставку.</p></div>
      <div class="si rv"><h3>Обучение и запуск</h3><p>Обучаем команду, передаём протоколы и материалы, сопровождаем первые продажи.</p></div>
    </div>
  </div>
</section>

<!-- ================= СВЯЗЬ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Прямая связь</span>
      <h2>Обсудим <em>партнёрство</em></h2>
    </div>
    <div class="cn">
{cn}
    </div>
  </div>
</section>

<!-- ================= CTA ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="cta cta-img rv">
      <div>
        <h2>Получите прайс для партнёров</h2>
        <p>Пришлём условия сотрудничества, прайс и материалы о брендe — и подберём стартовый ассортимент для вашего региона.</p>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="{PRICE}">Получить прайс {ARROW}</a>
        <a class="btn btn-o" href="{PROTO}">Протоколы</a>
      </div>
    </div>
  </div>
</section>

</div>'''.replace('брендe', 'бренде')
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  var d=root.querySelector('[data-until]');
  if(d){
    var end=new Date(d.getAttribute('data-until')+'T23:59:59+03:00'), now=new Date();
    if(now>end){ root.querySelector('[data-until-wrap]').hidden=true; }
    else{
      var days=Math.ceil((end-now)/864e5), el=d.querySelector('[data-left]');
      var w=(days%10===1&&days%100!==11)?'день':((days%10>=2&&days%10<=4&&(days%100<10||days%100>=20))?'дня':'дней');
      el.querySelector('b').textContent=days+' '+w; el.hidden=false;
    }
  }
  var items=root.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){[].forEach.call(items,function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.12,rootMargin:'0px 0px -30px 0px'});
  [].forEach.call(items,function(el){io.observe(el);});
})();
</script>'''
    head = '''<!-- ЖеДерм · страница для дистрибьюторов (/partners-distributors-jeuderm) · блок T123. Собрано tools/build_partners.py.
     Попапы: #getprice_partner, #getprotocol_partner. Блок октябрьской акции скрывается сам после срока. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'partners.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'partners.txt').write_text(out, encoding='utf-8')
    print('partners.html', len(out))
