import re
import pymorphy2
morph = pymorphy2.MorphAnalyzer()



# Чтение текста из файла, перевод в строку

txt = open('text.txt', 'r', encoding='utf-8')
text = txt.read()
txt.close()
print(type(text),text)

# Замена знаков припинания на пробелы №1 Недостаток слова через дефис разделяются по-своему = по своему
print()
print('Замена знаков припинания ')


# reg = re.compile('[\W]')
# text = reg.sub(' ', text)
# print(len(text), text)

# Метод удаления припинания знаков №2 Недостаток француженкою-гувернанткой остается одним словом

text=text.replace('—','').replace(',','').replace('.','').replace('«','').replace('»','').replace('!','').replace('?','').replace('\t',' ').replace('\n',' ').replace(';',' ')
print(len(text), text)

 # Убрать лишние пробелы
print()
print('Убираем лишние пробелы')

a = 0
b = 1
while b != a:
    b = len(text)
    text_1 = text.replace('  ',' ')
    a = len(text_1)
    text = text_1
print(len(text), text)

#  Все буквы строчные
print()
print('Все буквы строчные')
text = text.lower()
print(len(text), text)

# Преобразуем текст в список
print()
print('Переводим в список')
text_list = text.split(' ')
print(type(text_list), text_list)

# Нормализация слов
print()
print('Нормализация слов в списке')

text_list_norm=[]
for el in text_list:
    el = morph.parse(el)[0].normal_form
    text_list_norm.append(el)
print(len(text_list_norm),text_list_norm)

# Составление словаря: слово:частота применения
print()
print('Подсчет частоты применения слов')
text_dic={}
text_value = []

for el in text_list_norm:
    text_value.append(text_list_norm.count(el))

print(type(text_value),len(text_value),text_value)

# Составление словаря слов. Метод сборки через zip удивил тем, что сразу отбросил повторяющиеся значения
print()
print('Словарь частоты применения слов')
text_dic = dict(zip(text_list_norm,text_value))
print(len(text_dic), text_dic)

# Сортировка словаря
print()
print('Топ 5 слов текста по применению')
# Проблема в том, что сортировка идет по ключам, а нужно отсортировать по частоте, поэтому переделал словарь в вид частота:слово
text_dic_rev = dict(zip(text_value,text_list_norm))
text_dict_tuples = list(text_dic_rev.items())
text_dict_tuples.sort(reverse=True)
for i in range(5):
    print(text_dict_tuples[i])

# Перевод списка в множество')
text_set = set(text_list_norm)

print()

print('Количество применяемых слов', len(text_set))




