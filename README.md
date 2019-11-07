# django-task

https://docs.google.com/forms/d/e/1FAIpQLSdOjZb6U4gq5yuMnS00DtofLbG2TVVH8EyhcYIsAab-UfJucw/viewform

python 3.6.6

django 2.2.4

mysqlclient 1.4.4


Мы предлагаем вам создать службу рекрутинга для ордена Ситхов.

* — Нужно создать веб приложение на Django (версию можно выбрать самому), Python 2/3.
* — Верстка и внешний вид системы абсолютно не важны, фокус внимания на backend части.
* — Исходники нужно обязательно выложить на github/bitbucket.

Описание службы рекрутинга (далее - системы)

Система осуществляет:
*  поиск и учет рекрутов на всех планетах:

* отбор рекрутов по средствам вступительных испытаний;

* оповещение рекрутов о результатах испытаний и зачисление их в орден ситхов.

Система содержит сущности:

* Рекрут (Имя, Планета обитания, Возраст. Email);

* Ситх (Имя, планета на которой он обучает);
* Планета (Наименование);
* Тестовое испытание для Руки Тени (уникальный код ордена, список вопросов).

Такие сущности как Ситх / Планета / Тестовое испытание Руки Тени заводится в систему через
админку.
