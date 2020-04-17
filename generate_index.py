# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body):
    page = f'<html>{head}{body}</html>'
    return page

def generate_head(title):
    head = f'<meta charset="UTF-8"><title>{title}</title>'
    return f'<head>{head}</head>'

def generate_body_(header, paragraphs):
    body = f'<h1>{header}</h1>'
    for p in paragraphs:
        body += f'<p>{p}</p>'
    return f'<body>{body}</body>'

def save_page(title, header, paragraphs, output='index.html'):
    fp = open(output, 'w', encoding='utf8')
    today = dt.now().date()
    page = generate_page(generate_head(title),
                         generate_body_(header=header, paragraphs=paragraphs))
    print(page, file=fp)
    fp.close()

today = dt.now().date()
save_page(
    title="Гороскоп на сегодня",
    header=f"Что день {today} готовит",
    paragraphs=generate_prophecies()
)