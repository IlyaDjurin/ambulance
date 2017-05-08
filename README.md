# ambulance
Веб-страница с формой записи к врачу в поликлинике.
Пользователь  имеет возможность выбрать в форме время, дату и врача,
указать свои ФИО,описать кратко проблему и отправить данные. Прием длится один час, нет возможности
выбрать у врача время, на которое кто-либо уже записался. Так же нет возможности
записаться в нерабочее время. Время работы поликлиники: пн - пт с 9:00 до 18:00.
Администратор может зайти через админку и посмотреть запись у любого врача.

Для создания локального репозитория небоходимо:
1.Клонировать этот git-репозиторий в локальную папку и перейти в эту директорию.
2.Скачать докер-контейнер docker pull ilyadjurin/djangoapp.
3.Перейти в дирректорию regitratura и запустить конструктор (docker build -t ilyadjurin/djangoapp . )
4.Возвращаемся в главную директорию,и собираем контейнер docker-compose build. Если он не установлен,предварительно устанавливаем docker-compose.
5.Делаем мигграцию для БД (docker-compose run --rm web  python ./manage.py migrate)
6.Создаём нового суперпользователя, для доступа к админке (docker-compose run --rm web python ./manage.py createsuperuser)  
7.Запускаем приложение docker-compose up
8.Для запуска теста используем команду (docker-compose run --rm web python ./manage.py test).




Примечание:
По умолчанию БД пуста и вы можете через админку доватить любое количество врачей,после чего уже на главной странице появится форма записи на прием.
