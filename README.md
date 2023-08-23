SMARTCALC
==========
Больше калькуляторов богу калькуляторов!   
Базовые и инженерные функции, понятный интерфейс и удобные фичи:
- История
- Графики функций
- Польские нотации

## Быстрый старт
1. Для установки зависимостей используйте `poetry install` или `pip install -r requirements.txt`
2. Зайдите в директорию smartcalc и используйте `python install_script.py`

Скрипт запросит путь для установки, по умолчанию она будет произведена в директорию `/Applications`.   
Так же будет будет представлена возможность создать ярлык на рабочем столее, по умолчанию ярлык не создаётся.

## Основное окно
Здесь вы найдете все самые необходимые для калькулятора, базовые и не очень, функции, а так же:
- `?` - откроет окно с помощью. В нём вы сможете найти нюансы использования этого калькулятора.
- `H` - переведёт вас в окно с историей запросов. В нём будет скроллбар с историей, а так же возможность добавлять запрос в окно калькулятора, удалять запрос и очищать всю историю.
- `F(x)` - запустит производство графика (необходимое условие - в поле ввода калькулятора должен быть x). После нажатия будут запрошены области значений и определений.
- `Default` - возвращает в режим работы обычного калькулятора. Доступна только если нажаты PN или RPN.
- `PN` (Polish Notation) - режим работы с выражениями в Польской нотации. Сначала пишутся операторы, потом операнды.
> Пример: "+ 4 5"
- `RPN` (Reverse Polish Notation) - режим работы с выражениями в Обратной Польской нотации. Сначала пишутся операнды, потом операторы.
>Пример: "48 6 -"
- ` ` - ставить в поле ввода пробел. Доступна только если нажаты PN или RPN. Его нужно ставить между каждым оператором и операндом в выражениях в Польских нотациях. Необходимо для того, чтобы разграничить использование унарных знаков и выражений в Польских нотациях.
> Пример: "+32" может значить как унарный плюс к тридцати двум, так и три плюс два.
