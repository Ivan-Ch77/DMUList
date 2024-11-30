Переходим в командной строке в папку DMUList:
cd .\DMUList\ 

В папке DMUList пишем:
python -m venv venv

Активируем виртуальное окружение:
.\venv\Scripts\activate 

Устанавливаем либы:
pip install -r requirements.txt   

Запускаем сервер
python manage.py runserver 

Там будут url, на которые можно перейти
