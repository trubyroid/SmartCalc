SMART CALC
=====================
![Main window](./images/main_screen.png)  
Больше калькуляторов богу калькуляторов!   
Базовые и инженерные функции, понятный интерфейс и удобные фичи:
- История
- Графики функций
- Польские нотации

## Подготовка (в директории `smartcalc`)

**Poetry**
1. Для запуска виртуального окружения `poetry shell`
2. Для установки зависимостей `poetry install`

**Pip**
1. Для создания виртуального окружения `python3 -m venv venv`
2. Для запуска виртуального окружения `source venv/bin/activate`
3. Для установки зависимостей `pip install -r requirements.txt`

## Cтарт
Для установки (MacOS) - `python3 install_script.py` / Для запуска без установки - `python3 main.py`.  
Перед установкой будет запрошен путь (по умолчанию /Applications) и нужно ли создать ярлык на рабочем столе.

# Меню
- `H` - переведёт вас в окно с историей запросов. В нём будет скроллбар с историей, а так же возможность добавить запрос в поле ввода калькулятора, удалить его из истории, или же вовсе _очистить всю историю_.
![History window](./images/history_screen.png)  
- `F(x)` - запустит построение графика (необходимое условие - в поле ввода калькулятора должен быть x). После нажатия будут запрошены области значений и определений.
![History window](./images/graph_screen.png)  
- `?` - откроет окно с краткой инструкцией по работе с калькулятором.
### Режимы
>[!IMPORTANT]
>Переход между режимами очищает поле ввода калькулятора.
- `Default` - возвращает в стандартный режим работы калькулятора.
- `PN` (Polish Notation) - режим работы с выражениями в Польской нотации. Сначала пишутся операторы, потом операнды.
Пример: "+ 4 5"
- `RPN` (Reverse Polish Notation) - режим работы с выражениями в Обратной Польской нотации. Сначала пишутся операнды, потом операторы.
Пример: "48 6 -"
- `  ` - ставит в поле ввода пробел. Доступна только если нажаты PN или RPN. Его нужно ставить между каждым оператором и операндом в выражениях в Польских нотациях. 

>[!NOTE]
> Пробел необходим для того, чтобы калькулятор различал использование унарных знаков и вычисление выражений в Польских нотациях.  
Пример: "+32" может значить как унарный плюс к тридцати двум, так и три плюс два.

## Завершение
Благодарю читателя за интерес к моему проекту, буду рад вашему фидбеку.
