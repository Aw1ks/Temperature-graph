# Temperature-graph
## Используемые API и библиотеки
**opendatasoft:** Для получения координат города по названию и коду страны.
[Документация](https://public.opendatasoft.com/explore/)
**open-meteo:** Для получения данных о погоде.
[Документация](https://open-meteo.com/en/docs)
    
This project uses libraries such as: [requests](https://python-scripts.com/requests?ysclid=lyr2i4f3us982315000), [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/)
## Использование
1.  Запустите скрипт `python main.py`.
2.  Введите название города (на английском, с большой буквы), код страны (в формате ISO 3166-1 alpha-2, например, "US"), начальную и конечную дату периода (в формате YYYY-MM-DD).
3.  Скрипт отобразит график изменения температуры для указанного города в заданный период времени.
