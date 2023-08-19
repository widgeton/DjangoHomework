from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Главная</title>
    </head>
    <body>
        <h1>Главная</h1>
        <p>Здесь должна быть информация главной страницы сайта.</p>
    </body>
    </html>
    """
    logger.info('Посещение Главной страницы.')
    return HttpResponse(html)


def about(request):
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>О себе</title>
    </head>
    <body>
        <h1>О себе</h1>
        <p>Здесь должна быть информация страницы "О себе".</p>
    </body>
    </html>
    """
    logger.info('Посещение страницы О нас.')
    return HttpResponse(html)
