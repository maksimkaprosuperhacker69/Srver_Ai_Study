TEST_PROMT="""
Cоздай тест из {count} вопросов c вариантами ответа
 на основе текста, и дай ответ в json формате,[
 question,options[],correct_ans_id(int)]"""

SUMMARIZE_PROMT="""
Суммируй информацию из текста и по необходимости добавь что то своё. Разбивай ответ на абзацы, ответ дай на русском языке, верни просто ответ без пояснений. Пример ответа: 'Свет - видимая электромагнитная
волна

Цвет света определяется частотой
его колебаний

При переходе из одной среды в
другую меняется скорость света (по
формуле 2) и длина волны, но частота
остается постоянной

Дисперсия света - зависимость
показателя преломления вещества от
его частоты

Луч красного цвета в призме
преломляется меньше, чем луч
фиолетового цвета, так как у красного
света наибольшая скорость в
веществе, а у фиолетового -
наименьшая

Появление радуги объясняется
дисперсией света и полным
внутренним отражением в каплях
воды после дождя

Благодаря дисперсии света можно
наблюдать цветную игру света на
гранях бриллианта и других
прозрачных граненых предметах или
материалах' 

 Текст:
"""

TERMS_PROMT="""
Из текста выдели основные определения, понятия, формулы(если есть). """