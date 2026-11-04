#!/usr/bin/env python3
"""Переводит все ссылки на картинки сайта с jsDelivr (GitHub) на Яндекс Object Storage.

Запуск:  python3 tools/switch_media.py           — заменить в tools/*.py, tilda/*.html, tilda-txt/*.txt
         python3 tools/switch_media.py --check   — проверить, что каждый файл открывается в Яндексе
"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
YANDEX = 'https://storage.yandexcloud.net/revolution-bio/jeuderm_site/images/'
OLD = re.compile(r'https://cdn\.jsdelivr\.net/gh/freyia-me/-@[0-9a-f]+/images/')
DRK_OLD = 'https://static.tildacdn.com/tild6539-3739-4963-b264-393861653362/1.jpg'
DRK_NEW = YANDEX + 'partners/drk-logo.jpg'
FILES = [*ROOT.glob('tools/*.py'), *ROOT.glob('tilda/*.html'), *ROOT.glob('tilda-txt/*.txt')]


def switch():
    for f in FILES:
        if f.name == 'switch_media.py':
            continue
        s = f.read_text(encoding='utf-8')
        n = OLD.sub(YANDEX, s).replace(DRK_OLD, DRK_NEW)
        if n != s:
            f.write_text(n, encoding='utf-8')
            print('updated', f.relative_to(ROOT))


def check():
    urls = sorted({u for f in ROOT.glob('tilda/*.html')
                   for u in re.findall(r'https://storage\.yandexcloud\.net/[^"\'\s)]+', f.read_text(encoding='utf-8'))})
    bad = 0
    for u in urls:
        out = subprocess.run(['curl', '-sS', '-o', '/dev/null', '-w', '%{http_code} %{content_type}', u],
                             capture_output=True, text=True).stdout
        ok = out.startswith('200') and out.split()[-1].startswith('image/')
        bad += not ok
        print('OK ' if ok else 'BAD', out, u)
    print(len(urls), 'urls,', bad, 'problems')
    return bad


if __name__ == '__main__':
    sys.exit(check() if '--check' in sys.argv else switch())
