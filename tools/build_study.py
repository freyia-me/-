#!/usr/bin/env python3
"""Страница «Обучение» ЖеДерм (/study) для Tilda, блок T123.

Запуск:  python3 tools/build_study.py  →  tilda/study.html и tilda-txt/study.txt
Общие стили (шрифты, кнопки, метки, анимация) берутся из tools/line_template.html.
График семинаров не публикуется — только «по запросу» через форму #stadyjeuderm.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMG = 'https://cdn.jsdelivr.net/gh/freyia-me/-@a886d1a/images/'
SITE = 'https://jeuderm-russia.ru/'
FORM = '#popup:registerstudy'      # запись в малые группы / график семинаров
CLINIC = '#popup:studyclinic'     # обучение в клинике
ASK = '#popup:ask'                # задать вопрос
ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M1 8h13M9 3l5 5-5 5"/></svg>'
PLAY = '<svg viewBox="0 0 14 14" fill="currentColor"><path d="M2 1l11 6-11 6z"/></svg>'

WEBINARS = [
    ('#623a2c', 'products/nova-complex.webp', 'Обновляющая система Нова Комплекс',
     'Механизм действия, показания и ограничения, выбор пациента и ключевые этапы процедуры.',
     'https://rutube.ru/video/d7302347806e412731e8452d92509b13/'),
    ('#ab0a3d', 'products/zymo-complex.webp', 'Обновляющая система Зимо Комплекс',
     'Действие Zymo, протокол и нюансы для разного возраста и типа кожи, включая чувствительную и реактивную.',
     'https://rutube.ru/video/c266156ecd63023ff5dcac2c25901baf/'),
    ('#cd555b', 'products/reform-age-o2-boto-fluid-110ml.webp', 'Пептидные решения для здоровья и молодости кожи',
     'Для специалистов, которые хотят расширить арсенал проверенными и безопасными препаратами.',
     'https://rutube.ru/video/be7dc7a49613fefc73a1bb21cc9b99ec/'),
    ('#7f2346', 'products/molecular-twin-oil.webp', 'Ангельское совершенство кожи',
     'Система мягкого молекулярного обновления: гладкость, ровный тон и сияние без раздражения и реабилитации.',
     'https://rutube.ru/video/ecc180120e27f8f7743990dc621770f4/'),
]


def base_css():
    tpl = (ROOT / 'tools' / 'line_template.html').read_text(encoding='utf-8')
    css = re.search(r'<style>(.*?)</style>', tpl, re.S).group(1)
    keep = [l for l in css.split('\n')
            if not (re.match(r'\s*#jdl \.(card|grid|pr|procs|pd|tags|tag|seg|keys|dlg|x|meta|top|note|bar|res)\b', l)
                    or 'dialog' in l or '@keyframes' in l)]
    css = '\n'.join(keep).replace('#jdl', '#jds')
    return re.sub(r'@media \(max-width:\d+px\)\{\s*\}', '', css)


PAGE_CSS = f'''
/* ===== Обучение ===== */
#jds .head{{display:block;margin-bottom:36px}}
#jds .head h2{{margin-top:16px}}
#jds .head .lead{{margin-top:14px;font-size:16.5px}}
/* первый экран */
#jds .st-top{{padding-top:clamp(40px,5vw,72px)}}
#jds .st-g{{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(32px,5vw,80px);align-items:center}}
#jds .st-top h1{{font-size:clamp(32px,3.6vw,54px);margin:20px 0 18px}}
#jds .st-top .lead{{font-size:16.5px;max-width:520px;margin-bottom:28px}}
#jds .st-ph{{position:relative;border-radius:4px;overflow:hidden;aspect-ratio:16/10;background:var(--soft)}}
#jds .st-ph img{{width:100%;height:100%;object-fit:cover}}
#jds .st-badge{{position:absolute;left:14px;bottom:14px;padding:9px 14px;border-radius:999px;background:rgba(255,255,255,.92);font-size:11px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}}
#jds .facts{{list-style:none;display:grid;grid-template-columns:repeat(3,1fr);margin-top:34px;border-top:1px solid var(--line)}}
#jds .facts li{{padding:16px 14px 0 0;font-size:12.5px;line-height:1.45;color:var(--gray)}}
#jds .facts li+li{{padding-left:14px;border-left:1px solid var(--line)}}
#jds .facts b{{display:block;margin-bottom:3px;font-weight:600;font-size:13px;color:var(--ink)}}
/* форматы */
#jds .fm{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
#jds .fc{{display:flex;flex-direction:column;padding:30px 28px;border:1px solid var(--line);border-radius:4px;background:#fff}}
#jds .fc:before{{content:"";width:40px;height:3px;background:var(--c);margin-bottom:22px}}
#jds .fc h3{{margin:10px 0 12px}}
#jds .fc p{{font-size:14.5px;flex:1}}
#jds .fc ul{{list-style:none;margin-top:18px;border-top:1px solid var(--line)}}
#jds .fc li{{padding:9px 0 9px 18px;border-bottom:1px solid var(--line);font-size:13.5px;color:var(--ink);position:relative}}
#jds .fc li:before{{content:"";position:absolute;left:0;top:16px;width:6px;height:6px;background:var(--c)}}
#jds .fc .more{{margin-top:20px;display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}}
#jds .fc .more:after{{content:"→";color:var(--c);transition:transform .3s}}
#jds .fc .more:hover:after{{transform:translateX(4px)}}
/* программа */
#jds .prog{{background:var(--soft)}}
#jds .pg{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;counter-reset:s}}
#jds .pi{{counter-increment:s;padding:24px 22px;background:#fff;border:1px solid var(--line);border-radius:4px}}
#jds .pi:before{{content:counter(s,decimal-leading-zero);display:block;font-family:var(--hf);font-size:28px;color:var(--c);margin-bottom:12px}}
#jds .pi h3{{font-size:18px;margin-bottom:8px}}
#jds .pi p{{font-size:14px}}
/* симпозиум */
#jds .sym{{display:grid;grid-template-columns:1.2fr 1fr 1fr;grid-template-rows:repeat(2,minmax(0,1fr));gap:12px;aspect-ratio:2.1/1}}
#jds .sym figure{{margin:0;position:relative;overflow:hidden;border-radius:4px;background:var(--soft)}}
#jds .sym figure:first-child{{grid-row:1/3}}
#jds .sym img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform 1.4s cubic-bezier(.2,.7,.2,1)}}
#jds .sym figure:hover img{{transform:scale(1.04)}}
#jds .sym figcaption{{position:absolute;left:10px;bottom:10px;padding:6px 11px;border-radius:999px;background:rgba(255,255,255,.9);font-size:10.5px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:var(--ink)}}
#jds .sym-t{{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:end;margin-bottom:28px}}
#jds .sym-t .lead{{font-size:16px}}
/* эксперт */
#jds .exp{{display:grid;grid-template-columns:1.1fr .9fr;gap:20px}}
#jds .quote{{background:#4b343b;color:#fff;border-radius:4px;padding:clamp(32px,4vw,52px);display:flex;flex-direction:column;justify-content:space-between}}
#jds .quote .code{{color:rgba(255,255,255,.65)}}
#jds .quote blockquote{{font-family:var(--hf);font-size:clamp(19px,1.8vw,24px);line-height:1.5;margin:24px 0 32px}}
#jds .quote .who{{padding-top:20px;border-top:1px solid rgba(255,255,255,.25)}}
#jds .quote .who b{{display:block;font-weight:600;font-size:15px}}
#jds .quote .who span{{font-size:13px;color:rgba(255,255,255,.7)}}
#jds .partner{{display:flex;flex-direction:column;justify-content:space-between;padding:clamp(28px,3.5vw,44px);border:1px solid var(--line);border-radius:4px;background:#fff}}
#jds .partner h3{{margin:12px 0 12px}}
#jds .partner p{{font-size:14.5px;margin-bottom:22px}}
/* вебинары */
#jds .web{{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}}
#jds .wc{{--c:var(--gray);display:flex;flex-direction:column;border:1px solid var(--line);border-radius:4px;overflow:hidden;background:#fff;transition:transform .5s cubic-bezier(.2,.7,.2,1)}}
#jds .wc:hover{{transform:translateY(-4px)}}
#jds .wc .band{{position:relative;height:170px;display:flex;justify-content:space-between;align-items:flex-end;padding:16px 18px;background:#eee center/cover no-repeat;background-image:var(--img);isolation:isolate}}
#jds .wc .band:after{{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,transparent 35%,color-mix(in srgb,var(--c) 70%,transparent) 100%)}}
#jds .wc .band .code{{color:#fff}}
#jds .play{{width:44px;height:44px;border-radius:50%;background:#fff;display:grid;place-items:center;color:var(--c)}}
#jds .play svg{{width:12px;height:12px;margin-left:2px}}
#jds .wc .bd{{padding:20px 20px 22px;display:flex;flex-direction:column;flex:1}}
#jds .wc h3{{font-size:17px;margin-bottom:10px}}
#jds .wc p{{font-size:13.5px;line-height:1.5;flex:1}}
#jds .web-f{{margin-top:22px;display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap}}
#jds .web-f p{{font-size:15px;max-width:640px}}
/* CTA */
#jds .cta-img{{background:linear-gradient(90deg,#fff 0%,rgba(255,255,255,.95) 40%,rgba(255,255,255,.2) 78%,rgba(255,255,255,0) 100%),url('{IMG}home/skin-renewal.webp') right center/cover;color:var(--text);border:1px solid var(--line)}}
#jds .cta-img h2{{color:var(--ink)}}
#jds .cta-img .btn-a{{background:var(--ink);color:#fff}}
#jds .cta-img .btn-a:hover{{background:var(--c)}}
#jds .cta-img .btn-o{{border-color:#c8c1bf;color:var(--ink)}}
#jds .cta-img .btn-o:hover{{background:var(--ink);color:#fff}}
@media (max-width:1000px){{
  #jds .st-g,#jds .exp,#jds .cta,#jds .sym-t{{grid-template-columns:1fr}}
  #jds .fm{{grid-template-columns:1fr}}
  #jds .pg,#jds .web{{grid-template-columns:repeat(2,1fr)}}
  #jds .sym{{grid-template-columns:1fr 1fr;grid-template-rows:auto;aspect-ratio:auto}}
  #jds .sym figure{{aspect-ratio:4/3}}
  #jds .sym figure:first-child{{grid-row:auto;grid-column:1/3;aspect-ratio:16/9}}
  #jds .cta-img{{background:linear-gradient(180deg,rgba(255,255,255,.96) 0%,rgba(255,255,255,.9) 60%,rgba(255,255,255,.6) 100%),url('{IMG}home/skin-renewal.webp') center/cover}}
}}
@media (max-width:640px){{
  #jds .facts{{grid-template-columns:1fr}}
  #jds .facts li,#jds .facts li+li{{padding:12px 0;border-left:0;border-bottom:1px solid var(--line)}}
  #jds .pg{{grid-template-columns:1fr}}
  #jds .web{{grid-template-columns:1fr}}
  #jds .sym{{gap:8px}}
  #jds .sym figcaption{{left:6px;bottom:6px;font-size:8.5px;letter-spacing:.04em;padding:4px 7px}}
}}
'''


def build():
    webs = '\n'.join(f'''      <a class="wc rv" style="--c:{c}" href="{url}" target="_blank" rel="noopener">
        <div class="band" style="--img:url('{IMG}{img}')"><span class="code">Вебинар {i:02d}</span><span class="play">{PLAY}</span></div>
        <div class="bd"><h3>{t}</h3><p>{p}</p><span class="more" style="margin-top:16px;font-size:12px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)">Смотреть →</span></div>
      </a>''' for i, (c, img, t, p, url) in enumerate(WEBINARS, 1))

    body = f'''<div id="jds">

<!-- ================= ПЕРВЫЙ ЭКРАН ================= -->
<section class="st-top">
  <div class="w st-g">
    <div>
      <span class="lab rv"><i></i>Обучение · Революшн Био — ЖеДерм</span>
      <h1 class="rv">Обучение для <em>косметологов</em> и клиник</h1>
      <p class="lead rv">Многоуровневая система профессионального обучения для косметологов, трихологов и специалистов эстетической медицины: от первого знакомства с препаратами ЖеДерм до уверенной работы по протоколам.</p>
      <div class="btns rv">
        <a class="btn btn-a" href="{FORM}">Узнать график семинаров {ARROW}</a>
        <a class="btn btn-o" href="#webinars">Смотреть вебинары</a>
      </div>
      <ul class="facts rv">
        <li><b>Бесплатно</b>для специалистов, работающих с ЖеДерм</li>
        <li><b>Малые группы</b>практика и вопросы тренеру</li>
        <li><b>Протоколы</b>которые можно применить сразу</li>
      </ul>
    </div>
    <div class="st-ph rv">
      <img src="{IMG}study/symposium-hall-bags.webp" alt="Обучение ЖеДерм: зал международного симпозиума" loading="eager">
      <span class="st-badge">International Aesthetic Symposium · 2026</span>
    </div>
  </div>
</section>

<!-- ================= ФОРМАТЫ ================= -->
<section>
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Форматы обучения</span>
      <h2>Выберите <em>удобный формат</em></h2>
    </div>
    <div class="fm">
      <div class="fc rv" style="--c:#cd555b">
        <span class="code">В клинике</span>
        <h3>Обучение в клиниках</h3>
        <p>При запуске препаратов ЖеДерм проводим бесплатное обучение и сопровождение на базе партнёрских клиник. Практические занятия под руководством опытных тренеров.</p>
        <ul><li>Запуск линии в кабинете</li><li>Отработка протоколов на практике</li><li>Сопровождение после старта</li></ul>
        <a class="more" href="{CLINIC}">Заявка на обучение в клинике</a>
      </div>
      <div class="fc rv" style="--c:#76bc21">
        <span class="code">Очно</span>
        <h3>Обучение в малых группах</h3>
        <p>Очные занятия в учебном центре ЖеДерм. В небольшой группе тренер уделяет внимание каждому, а вы отрабатываете навыки в комфортной обстановке.</p>
        <ul><li>Практика с продуктами ЖеДерм</li><li>Вопросы напрямую экспертам</li><li>Участие по предварительной записи</li></ul>
        <a class="more" href="{FORM}">Узнать график</a>
      </div>
      <div class="fc rv" style="--c:#2a7de1">
        <span class="code">Онлайн</span>
        <h3>Вебинары и онлайн-тренинги</h3>
        <p>Для специалистов, которые не могут присутствовать очно: вебинары и онлайн-тренинги по линиям и протоколам. Записи прошедших вебинаров — по запросу у менеджера.</p>
        <ul><li>Механизмы действия и показания</li><li>Разбор протоколов</li><li>Записи для повторного просмотра</li></ul>
        <a class="more" href="#webinars">Смотреть вебинары</a>
      </div>
    </div>
  </div>
</section>

<!-- ================= ПРОГРАММА ================= -->
<section class="prog">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Что вы получите</span>
      <h2>Программа <em>обучения</em></h2>
    </div>
    <div class="pg">
      <div class="pi rv"><h3>Наука формул</h3><p>Пептиды, пробиотики и биотехнологии: как работают средства ЖеДерм и почему.</p></div>
      <div class="pi rv"><h3>Подбор под задачу</h3><p>Возрастная, проблемная, чувствительная кожа, обновление и кожа головы — какую линию выбрать.</p></div>
      <div class="pi rv"><h3>Протоколы процедур</h3><p>Пошаговые процедуры с дозировками и временем каждого шага — от чистки до лифтинга 40+.</p></div>
      <div class="pi rv"><h3>Домашний уход</h3><p>Как подобрать клиенту уход между визитами, чтобы результат держался дольше.</p></div>
    </div>
  </div>
</section>

<!-- ================= СИМПОЗИУМ ================= -->
<section>
  <div class="w">
    <div class="sym-t">
      <div class="head" style="margin-bottom:0">
        <span class="lab"><i></i>Международные мероприятия</span>
        <h2>JeuDérm International <em>Aesthetic Symposium</em></h2>
        <p class="lead">Дубровник, Хорватия · 19–21 мая 2026. Доклады экспертов, разборы клинических случаев и новые протоколы — вместе с косметологами из разных стран.</p>
      </div>
      <a class="btn btn-o" href="{FORM}">Узнать о ближайших событиях</a>
    </div>
    <div class="sym">
      <figure class="rv"><img src="{IMG}study/symposium-group-dubrovnik.webp" alt="Участники симпозиума JeuDérm в Дубровнике" loading="lazy"><figcaption>Дубровник · 2026</figcaption></figure>
      <figure class="rv"><img src="{IMG}study/symposium-lecture-hall.webp" alt="Доклад на симпозиуме JeuDérm" loading="lazy" style="object-position:50% 30%"><figcaption>Доклады экспертов</figcaption></figure>
      <figure class="rv"><img src="{IMG}study/symposium-terrace.webp" alt="Стенд JeuDérm на террасе симпозиума" loading="lazy" style="object-position:50% 52%"><figcaption>JeuDérm Symposium</figcaption></figure>
      <figure class="rv"><img src="{IMG}study/symposium-exosome-lecture.webp" alt="Научный доклад о механизмах действия на коже" loading="lazy"><figcaption>Научная программа</figcaption></figure>
      <figure class="rv"><img src="{IMG}study/symposium-hall-bags.webp" alt="Зал симпозиума с участниками" loading="lazy"><figcaption>Участники</figcaption></figure>
    </div>
  </div>
</section>

<!-- ================= ЭКСПЕРТ + ПАРТНЁР ================= -->
<section style="padding-top:0">
  <div class="w exp">
    <div class="quote rv">
      <div>
        <span class="code">Тренер ЖеДерм</span>
        <blockquote>«Работая в эстетической медицине более 20 лет, я перепробовала множество брендов, но именно ЖеДерм стал для меня настоящим открытием. Это не просто качественная косметика — это инструмент, который помогает достигать видимых и устойчивых результатов у клиентов».</blockquote>
      </div>
      <div class="who"><b>Лилия Мукарамова</b><span>Научный руководитель Revolution Bio, сертифицированный тренер по продукции ЖеДерм</span></div>
    </div>
    <div class="partner rv">
      <div>
        <span class="code">Наш партнёр · с 1989 года</span>
        <h3>Институт косметологии «Дом Русской Косметики»</h3>
        <p>Обучение специалистов косметологии и beauty-сферы: программы для врачей, косметологов и новичков, документы государственного образца, внесение в ФИС ФРДО, регистрация в НМО Минздрава.</p>
      </div>
      <a class="btn btn-o" href="{SITE}cosmeticru">Подробнее</a>
    </div>
  </div>
</section>

<!-- ================= ВЕБИНАРЫ ================= -->
<section id="webinars" style="padding-top:0">
  <div class="w">
    <div class="head">
      <span class="lab"><i></i>Вебинары для профи</span>
      <h2>Смотрите <em>бесплатно</em> на Рутуб</h2>
    </div>
    <div class="web">
{webs}
    </div>
    <div class="web-f rv">
      <p>Записи других вебинаров и онлайн-тренингов — по запросу у менеджера.</p>
      <a class="btn btn-o" href="https://rutube.ru/channel/42947212/" target="_blank" rel="noopener">Все вебинары</a>
    </div>
  </div>
</section>

<!-- ================= CTA ================= -->
<section style="padding-top:0">
  <div class="w">
    <div class="cta cta-img rv">
      <div>
        <h2>Узнайте график ближайших семинаров</h2>
        <p>Расписание обучения формируется по запросу. Оставьте заявку — менеджер пришлёт даты, программу и подтвердит участие. Количество мест в группе ограничено.</p>
      </div>
      <div class="btns">
        <a class="btn btn-a" href="{FORM}">Узнать график {ARROW}</a>
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

    head = '''<!-- ЖеДерм · страница «Обучение» (/study) · блок T123 «HTML-код». Собрано tools/build_study.py.
     Кнопки ведут на попапы Tilda: #popup:registerstudy (график / запись), #popup:studyclinic (обучение в клинике), #popup:ask (вопрос). -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Tenor+Sans&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">

'''
    return head + '<style>' + base_css() + PAGE_CSS + '</style>\n\n' + body + '\n\n' + script + '\n'


if __name__ == '__main__':
    out = build()
    (ROOT / 'tilda' / 'study.html').write_text(out, encoding='utf-8')
    (ROOT / 'tilda-txt' / 'study.txt').write_text(out, encoding='utf-8')
    print('study.html', len(out))
