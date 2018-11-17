#все пункты задания рассматривались как независимые (эти папки = папки всего дерева)
import os
import re

#функция, которая возвращает названия всех папок дерева
def folder_names():
    folders = [os.getcwd().split("/")[-1]] #записываем в список название текущей папки
    for i in os.walk("."):
        folders += i[1]
    return folders


#списки отдельно названий (без расширений) и расширений всех файлов в папках
def extension_and_name():
    files = []
    for i in os.walk("."):
        files += i[2]
    extensions = []
    names = []
    for file in files:
        name, extension = os.path.splitext(file)
        names.append(name)
        extensions.append(extension)
    return extensions, names


#функция, которая определяет самый частый элемент списка
def most_common(lst):
    max = lst[0]
    max_count = lst.count(max)
    for el in lst:
        if lst.count(el) > max_count:
            max = el
            max_count = lst.count(el)
    return max


#функция, которая удаляет из списка повторяющиеся элементы
def uniq_list(lst):
    uniq_lst = []
    for i in lst:
        if i not in uniq_lst:
            uniq_lst.append(i)

    return uniq_lst


#1 глубина папки
def deep_folder():
    return (max([len(i[0].split("/")) for i in os.walk(".")])-1)

#2 количество папок с кириллическими названиями
def is_cyrillic():
    folders = folder_names()
    #шаблон для поиска кириллических слов (пробелы не включены)
    r = re.compile("^[а-яА-ЯёЁ]+$")
    #список с кириллическими названиями
    russian = [w for w in filter(r.match, folders)]
    return len(russian)

#3 самое частое расширение для всех файлов
def file_extensions():
    return (most_common(extension_and_name()[0]))


#4 самая частая первая буква
def first_letter():
    letters = []
    for folder in folder_names():
        letters.append(folder[0])
    return (most_common(letters))


#5 количество различных названий файлов (не считая расширений)
def different_names():
    names = extension_and_name()[1]
    uniq_names = uniq_list(names)
    return (len(uniq_names))

#6 количество папок, в которых есть файлы с повторяющимися расширениями
def repeat_extensions():
    a = os.walk(".")
    n = 0
    for i in a:
        extensions = []
        for b in i[2]:
            extensions.append(os.path.splitext(b)[1])
        uniq_extensions = uniq_list(extensions)
        if len(uniq_extensions) < len(extensions):
            n += 1
    return n

#7 папка с наибольшим количеством файлов внутри
def file_counter():
    d = {}
    #ключ -- количество файлов в папке, значение -- название папки
    #если несколько папок содержат одинаковое количество файлов, то выводится только одна
    for i in os.walk("."):
        d[len(i[2])] = i[0]
    max_folder = d.get(max(d.keys())).split("/")[-1]
    #исключение для папки с программой
    if max_folder == ".":
        return os.getcwd().split("/")[-1]
    else:
        return max_folder


def write_results():
    q1 = "Максимальная глубина папки: "+str(deep_folder())
    q2 = "Количество кириллических папок: "+str(is_cyrillic())
    q3 = "Самое частое расширение для всех файлов: "+file_extensions()
    q4 = "Самая популярная первая буква в названиях папок: "+first_letter()
    q5 = "Общее количество уникальных названий файлов: "+str(different_names())
    q6 = "Количество папок, в которых есть файлы с одинаковым расширением: "+str(repeat_extensions())
    q7 = "Папка с наибольшим количеством файлов: "+file_counter()

    with open("results.txt", "w", encoding="utf-8") as result:
        result.write(q1 + '\n' + q2 + '\n' + q3 + '\n' + q4 + '\n' + q5 + '\n' + q6 + '\n' + q7)

write_results()