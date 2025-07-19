<h1 align="center">Игра "Змейка"<img src="https://cdn-icons-png.flaticon.com/512/616/616487.png" width="35px" height="35px"></h1>
<h2>Оглавление</h2>

1. [Об авторе](#me)

1. [Об игре](#game)

1. [Как установить](#install)


## <a name="me">Об авторе</a>


<h3>Привет! Меня зовут Мария</h3>
<p>Я занимаюсь программированием c 2020 года. В моем арсенале:</p>
<div>
<img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
<img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E">
<img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Django%20REST%20Framework-red?style=for-the-badge&logo=django&logoColor=white">
<img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=Flask&logoColor=white">
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white">
<img src="https://img.shields.io/badge/Scrapy-46A247?style=for-the-badge&logo=scrapy&logoColor=white">
<img src="https://img.shields.io/badge/postgresql-4169e1?style=for-the-badge&logo=postgresql&logoColor=white">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/docker-%231572B6.svg?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/nginx-%231572B6.svg?style=for-the-badge&logo=nginx&logoColor=white">
<img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white">
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white">
<img src="https://github.com/Mhch497/the_snake/assets/55291670/cb8309ba-5a85-40c1-ae28-291713f0609d" width="30px" height="30px">
</div>
<p>Я также являюсь преподавателем программирования в международной школе математики и программирования Алгоритмика</p>
<img src="https://static.tildacdn.com/tild6661-3330-4861-b630-663534303033/Logo1.svg"  height="35px"/>


## <a name="game">Об игре</a>

<p>Вашему вниманию представляется один из базовых проектов для изучения программирования - "Змейка"</p>
<img src="https://pictures.s3.yandex.net/resources/image_1702376899.png">
<p>Игра реализована на языке программирования <b>Python</b> (v3.9.13) с использованием библиотеки для создания игр <b>Pygame</b> и модуля <b>random</b></p>
<p><b>Суть игры:</b> игрок управляет змейкой, которая движется по игровому полю, разделённому на клетки.</p>
<p><b>Цель игры:</b> увеличивать длину змейки, «съедая» появляющиеся на экране яблоки</p>

<p>В моем варианте также имеются:</p>
<ul type='square'>
  <li>"мусор" - вредная для змейки еда, после которой у нее длина уменьшается <img src="https://www.colorabout.com/images/color/rgb/85-107-47.jpg?v=1" width="15px" height="15px"></li>
  <li>"камни" - препятствия на пути змейки. Если змейка сталкивается с камнем, она "погибает" и игра начинается заново <img src="https://www.colorcombos.com/images/colors/696969.png" width="15px" height="15px"></li>
</ul>

<p>Управление в игре осуществляется на кнопки-стрелочки или на кнопки wasd.</p>
<h4>В дальнейшем планируется добавление меню, где можно будет настроить цвета для персонажей и выбрать сложность игры. Следите за обновлениями!</h4>

## <a name="install">Как установить</a>

<p>Клонировать репозиторий</p>

`git clone https://github.com/Mhch497/the_snake.git`

<p>Перейти в папку с игрой</p>

`cd .\the_snake\`

<p>Установить зависимости</p>

`pip install -r requirements.txt`

<p>Запустить игру</p>

`python the_snake.py`
