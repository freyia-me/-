#!/usr/bin/env python3
"""Страница «Акции» ЖеДерм для Tilda, блок T123.

Запуск:  python3 tools/build_promo.py  →  tilda/promo.html и tilda-txt/promo.txt
Срок акции для дистрибьюторов задаётся в DISTR_UNTIL; после этой даты карточка сама скрывается.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_study import base_css, IMG, ARROW  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = 'https://jeuderm-russia.ru/'
DISTR_UNTIL = '2026-10-31'          # последний день акции для дистрибьюторов
DISTR_UNTIL_T = '31 октября'

CONTACTS = [
    ('wa', 'WhatsApp', '+7 925 342-82-02', 'https://wa.me/79253428202',
     '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1 .2-3.3-.7-2.8-1.1-4.6-4-4.7-4.2-.1-.2-1.1-1.5-1.1-2.9s.7-2 1-2.3c.2-.3.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 2c.1.2.1.4 0 .5l-.4.6-.4.4c-.1.1-.3.3-.1.6.2.3.8 1.3 1.7 2.1 1.2 1 2.1 1.3 2.4 1.5.3.1.5.1.6-.1l.9-1c.2-.3.4-.2.6-.1l1.9.9c.3.1.5.2.5.3.1.2.1.7-.1 1.3z"/>'),
    ('tg', 'Telegram', '+7 925 084-30-90', 'https://t.me/+79250843090',
     '<path d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.3-5 9.1-8.2c.4-.4-.1-.6-.6-.2L6.2 13.1l-4.8-1.5c-1-.3-1.1-1 .2-1.5L20.5 3c.9-.3 1.6.2 1.4 1.3z"/>'),
    ('max', 'MAX', 'Написать в MAX', 'https://max.ru/u/f9LHodD0cOLKBWLODghgiSo7Io7UdoSgD9WyEFyj38AwuRwPD6M5HL3syog',
     '<path d="M12 2C6.5 2 2 6.1 2 11.2c0 2.6 1.2 5 3.1 6.7L4.5 22l4-2.1c1.1.3 2.3.5 3.5.5 5.5 0 10-4.1 10-9.2S17.5 2 12 2zm-4.6 12.4V8.1h1.5l2.1 3 2.1-3h1.5v6.3h-1.6v-3.7l-2 2.8-2-2.8v3.7H7.4z"/>'),
    ('tel', 'Позвонить', '+7 925 342-82-02', 'tel:+79253428202',
     '<path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2z"/>'),
    ('mail', 'E-mail', 'info@revolution.bio', 'mailto:info@revolution.bio',
     '<path d="M3 5h18c.6 0 1 .4 1 1v12c0 .6-.4 1-1 1H3c-.6 0-1-.4-1-1V6c0-.6.4-1 1-1zm9 7.2L4 7.3V17h16V7.3l-8 4.9zM19.1 7H4.9l7.1 4.3L19.1 7z"/>'),
]

CSS = '''
/* ===== Акции ===== */
#jds .head{display:block;margin-bottom:36px}
#jds .head h2{margin-top:16px}
#jds .pr-top{padding-top:clamp(40px,5vw,72px)}
#jds .pr-top h1{font-size:clamp(32px,3.6vw,54px);margin:20px 0 16px;max-width:760px}
#jds .pr-top .lead{font-size:16.5px;max-width:620px}
#jds .offers{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:clamp(32px,4vw,52px)}
#jds .of{position:relative;overflow:hidden;isolation:isolate;display:flex;flex-direction:column;padding:clamp(30px,4vw,48px);border-radius:6px;min-height:420px}
#jds .of-1{background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.94) 46%,rgba(255,255,255,.25) 100%),url('IMGhome/skin-renewal.webp') right center/cover;border:1px solid var(--line)}
#jds .of-2{background:#29282a;color:rgba(255,255,255,.8)}
#jds .of-2:after{content:"";position:absolute;right:-60px;top:-60px;width:260px;height:260px;border-radius:50%;border:1px solid rgba(255,255,255,.18);box-shadow:0 0 0 30px rgba(255,255,255,.04),0 0 0 70px rgba(255,255,255,.03);z-index:-1}
#jds .of .tag{align-self:flex-start;padding:7px 13px;border-radius:999px;font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;background:var(--c-soft);color:var(--c)}
#jds .of-2 .tag{background:rgba(255,255,255,.12);color:#fff}
#jds .of .big{font-family:var(--hf);font-size:clamp(72px,8vw,120px);line-height:1;color:var(--c);margin:26px 0 8px}
#jds .of-2 .big{color:#fff;font-size:clamp(40px,4.4vw,64px);line-height:1.08;margin:26px 0 14px}
#jds .of h2{font-size:clamp(22px,2.2vw,30px);margin-bottom:12px}
#jds .of-2 h2{color:#fff}
#jds .of p{font-size:15px;max-width:440px;flex:1}
#jds .of ul{list-style:none;margin:18px 0 0;max-width:460px}
#jds .of li{position:relative;padding:8px 0 8px 18px;font-size:14px;border-top:1px solid rgba(255,255,255,.15)}
#jds .of li:before{content:"";position:absolute;left:0;top:15px;width:6px;height:6px;background:var(--c)}
#jds .of .btns{margin-top:28px}
#jds .of-2 .btn-a{background:var(--c)}
#jds .of-2 .btn-a:hover{background:#fff;color:var(--ink)}
#jds .of-2 .btn-o{border-color:rgba(255,255,255,.45);color:#fff}
#jds .of-2 .btn-o:hover{background:#fff;color:var(--ink)}
#jds .left{display:inline-flex;align-items:center;gap:8px;margin-top:16px;font-size:12.5px;color:rgba(255,255,255,.7)}
#jds .left b{font-family:var(--hf);font-weight:400;font-size:22px;color:#fff}
#jds .of-2[hidden]{display:none}
#jds .offers.one{grid-template-columns:1fr}
#jds .cn{display:grid;grid-template-columns:repeat(5,1fr);gap:14px}
#jds .ci{display:flex;flex-direction:column;align-items:flex-start;gap:14px;padding:22px 20px;border:1px solid var(--line);border-radius:4px;background:#fff;transition:transform .4s,border-color .3s,box-shadow .4s}
#jds .ci:hover{transform:translateY(-3px);border-color:var(--k);box-shadow:0 18px 40px -32px rgba(0,0,0,.4)}
#jds .ci i{display:grid;place-items:center;width:46px;height:46px;border-radius:50%;background:var(--k);color:#fff}
#jds .ci svg{width:22px;height:22px;fill:currentColor}
#jds .ci b{font-weight:600;font-size:15px;color:var(--ink)}
#jds .ci span{font-size:13px;color:var(--gray);word-break:break-word}
#jds .terms{margin-top:28px;font-size:12.5px;color:var(--gray);max-width:820px}
@media (max-width:1000px){#jds .offers{grid-template-columns:1fr}#jds .cn{grid-template-columns:repeat(3,1fr)}}
@media (max-width:640px){#jds .cn{grid-template-columns:1fr 1fr;gap:10px}#jds .ci{padding:16px 14px}#jds .of{min-height:0}#jds .of .big{font-size:64px}#jds .of-2 .big{font-size:30px}}
'''.replace('IMG', IMG)

COLORS = {'wa': '#25d366', 'tg': '#229ed9', 'max': '#6d43f5', 'tel': '#29282a', 'mail': '#cd555b'}


def build():
    cn = '\n'.join(f'''      <a class="ci rv" style="--k:{COLORS[k]}" href="{url}"{'' if url.startswith(('tel:', 'mailto:')) else ' target="_blank" rel="noopener"'}><i><svg viewBox="0 0 24 24" aria-hidden="true">{svg}</svg></i><b>{t}</b><span>{sub}</span></a>'''
                   for k, t, sub, url, svg in CONTACTS)
    body = f'''<div id="jds">

<!-- ================= ШАПКА ================= -->
<section class="pr-top">
  <div class="w">
    <span class="lab rv"><i></i>Акции ЖеДерм</span>
    <h1 class="rv">Специальные условия для <em>специалистов</em> и партнёров</h1>
    <p class="lead rv">Начните работать с профессиональной космецевтикой ЖеДерм на выгодных условиях — напрямую от официального дистрибьютора в России.</p>

    <div class="offers">
      <div class="of of-1 rv">
        <span class="tag">Постоянная акция</span>
        <div class="big">−15%</div>
        <h2>на первый заказ</h2>
        <p>Скидка для новых клиентов на первую закупку профессиональных и домашних средств ЖеДерм — любых линий.</p>
        <ul style="color:var(--ink)">
          <li style="border-color:var(--line)">Для косметологов, клиник и салонов</li>
          <li style="border-color:var(--line)">На все линии: Reform Age, Acno, Ato Care, ПРО, Nova · Zymo, Hair Genesis</li>
          <li style="border-color:var(--line)">Бесплатное обучение работе с препаратами</li>
        </ul>
        <div class="btns">
          <a class="btn btn-a" href="#get15%discount">Получить скидку {ARROW}</a>
          <a class="btn btn-o" href="https://wa.me/79253428202" target="_blank" rel="noopener">Написать в WhatsApp</a>
        </div>
      </div>

      <div class="of of-2 rv" data-until="{DISTR_UNTIL}">
        <span class="tag">До {DISTR_UNTIL_T}</span>
        <div class="big">Специальные условия для дистрибьюторов</div>
        <p>Станьте партнёром ЖеДерм в своём регионе. До конца октября — особые условия для новых дистрибьюторов: расскажем подробности и подготовим предложение.</p>
        <ul>
          <li>Официальное партнёрство с дистрибьютором ЖеДерм в России</li>
          <li>Обучение команды и маркетинговая поддержка</li>
          <li>Персональный менеджер</li>
        </ul>
        <span class="left" data-left hidden>Осталось <b></b></span>
        <div class="btns">
          <a class="btn btn-a" href="#getconsult">Узнать условия {ARROW}</a>
          <a class="btn btn-o" href="{SITE}partners-distributors-jeuderm">Для дистрибьюторов</a>
        </div>
      </div>
    </div>
    <p class="terms rv">Подробные условия акций, сроки и порядок получения скидки уточняйте у менеджера. Скидка на первый заказ предоставляется один раз новому клиенту и не суммируется с другими предложениями.</p>
  </div>
</section>

<!-- ================= СВЯЗЬ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Прямая связь</span>
      <h2>Свяжитесь с нами <em>удобным способом</em></h2>
    </div>
    <div class="cn">
{cn}
    </div>
  </div>
</section>

</div>'''
    script = '''<script>
(function(){
  var root=document.getElementById('jds'); if(!root) return;
  /* карточка для дистрибьюторов: прячем после даты, показываем, сколько дней осталось */
  var d=root.querySelector('[data-until]');
  if(d){
    var end=new Date(d.getAttribute('data-until')+'T23:59:59+03:00'), now=new Date();
    if(now>end){ d.hidden=true; d.parentNode.classList.add('one'); }
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
    head = '''<!-- ЖеДерм · страница «Акции» · блок T123. Собрано tools/build_promo.py.
     Карточка для дистрибьюторов скрывается сама после DISTR_UNTIL. Кнопки: #get15%discount и #getconsult — попапы Tilda. -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'promo.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'promo.txt').write_text(out, encoding='utf-8')
    print('promo.html', len(out))
