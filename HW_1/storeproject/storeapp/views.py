from django.shortcuts import render
from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def home_page(request):
    logger.info(f'{datetime.now().strftime("%H:%M:%S")} Открыта главная страница')
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
       <title>Мой первый Django-сайт</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #FDF5E6;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
                color: #666;
            }
            footer {
                text-align: center;
                margin-top: 20px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container", width = 100%>
            <h1>Добро пожаловать на мой первый интернет-магазин!</h1>
            <p>В дальнейшем здесь вы найдете уникальные товары и аксессуары, которые нельзя найти нигде еще.</p>
            <p>Мы гордимся тем, что предоставляем экспертное обслуживание и заботу для наших клиентов.</p>
            <p>Наша миссия — следовать модным тенденциям, создавать стильные образы и предоставлять клиентам то, что они хотят.</p>
            <p>Наша цель — изменить взаимодействие общества с индустрией моды, предоставляя клиентам продукты, которые производятся этично и ответственно.</p>
            <footer>© 2024 Мой первый интернет-магазин. Все права защищены.</footer>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)


def about_page(request):
    logger.info(f'{datetime.now().strftime("%H:%M:%S")} Открыта страница "О создателе"')
    html = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <title>О создателе</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #FDF5E6;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333;
            }
            p {
                font-size: 16px;
                line-height: 1.6;
                color: #666;
            }
            footer {
                text-align: center;
                margin-top: 20px;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="container", width = 100%>
            <h1>Добро пожаловать на страницу информация о создателе интернет-магазина!</h1>
            <p>О себе: Здравствуйте! Меня зовут Дмитрий. Мне 32 года, раньше я работал дежурным инженером 
            в сотовой компании, позже подключал домашний интернет для абонентов Билайн. 
            На данный момент я изучаю курс backand-разработчик в GeekBrains и в дальшейшем планирую рабать
            в этой сфере. Это будет первый Django-сайт написанный мною. Мой сайт представляет 
            собой интернет-магазин на котором можно будет найти различные товары, которые пользуются спросом 
            у покупателей.</p>
            <p>Заключение: Жизнь ИТ-специалиста — это непрерывное обучение, поиск решений и стремление 
            к совершенству. Я готов к новым вызовам и всегда открыт для сотрудничества.</p>
            <footer>© 2024 Мой первый интернет-магазин. Все права защищены.</footer>
        </div>
    </body>
    </html>
    """

    return HttpResponse(html)