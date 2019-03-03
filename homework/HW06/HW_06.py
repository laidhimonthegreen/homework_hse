#этот код неряшлив и неэффективен не из-за неуважения, а из-за неопытности

#импорт нужных библиотек
import pandas as pd
import os
import re
from urllib.request import urlretrieve
import urllib
from nltk import word_tokenize
import bs4
from transliterate import slugify


#базовые значения некоторых переменных
mystem_path = "/home/laidhimonthegreen/mystem/mystem"
interval = [(7, 2015), (12, 2018)]
months_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
reg_html = '<[^<]+>'

#Работа с HTML

#функция, которая загружает отдельную страницу
def page_download(url):
    destination = "".join(url.split('/'))[-4:]
    urlretrieve(url, destination)
    return destination


#функция, которая переводит html в текст и удаляет первичный html (попутно достаёт заголовок)
def to_txt(path):
    with open(path, "r") as file:
        soup_page = bs4.BeautifulSoup(file, "lxml")
        page_title = soup_page.title.getText().replace(" ", "_")
        article_list = [str(x) for x in (soup_page.findAll('p'))]
        article_text = " ".join(article_list)
        not_clean_text = str(soup_page)
        kinda_clean_text = "\n" + article_text.replace("<p>", "\n")
    return page_title, not_clean_text, kinda_clean_text


#функция возвращает достаточно чистый текст статьи
def get_clean_text(path):
    cleaner_text = [line for line in to_txt(path)[2].split("\n") if "href" not in line]
    cleaner_text = " ".join(cleaner_text)
    clean_text = (("".join(cleaner_text.split("</p>")[1:]).split("<p class"))[0])
    return clean_text

#функция возвращает автора статьи из текста с тегами
def get_author(text):
    for line in text.split("{"):
        if r'"@type": "Person"' in line:
            return (" ".join([word for word in line.split(' ') if word.strip()][3:5]))

#Собираем сами ссылки

#вспомогательные функции для дней формата "01"
def get_days():
    days = []
    for i in range(1, 32):
        if i > 9:
            days.append(str(i))
        else:
            days.append("0" + str(i))
    return days

#и месяцев формата "01"
def get_months():
    months = []
    for i in range(1, 13):
        if i > 9:
            months.append(str(i))
        else:
            months.append("0" + str(i))
    return months

#конструируем возможные ссылки по дням при известной теме "theme"
def main_links(theme):
    links_to_search = []
    for year in range(2016, 2019):
        for month in get_months():
            for day in get_days():
                link_name = "https://www.mk.ru/" + theme + "/" + str(year) + "/" + month + "/" + day + "/"
                links_to_search.append(link_name)
    return links_to_search

#функция, которая на одной странице ищет все ссылки на новости за определенную дату и собирает их
def get_urls_from_date(date_url):
    date_urls = to_txt(page_download(date_url))[1]
    link_pattern = re.compile('href="(.*?)"')
    urls_from_date = [url for url in re.findall(link_pattern, date_urls) if date_url in url]
    os.remove(page_download(date_url))
    return urls_from_date

#собираем ссылки вида сайт.ру/тема/дата по всем датам при известной теме "theme"
def get_all_dates(theme):
    all_dates = []
    for link in main_links(theme):
            try:
                all_dates += get_urls_from_date(link)
            except urllib.error.HTTPError:
                pass
    return set(all_dates)

#собираем ссылки, из которых в будущем будем собирать информацию
def getting_links_for_parse():
    links_for_parse = get_all_dates("economics") | get_all_dates("politics")
    return links_for_parse

#Готовим таблицу с информацией

#создаем пустой список со списками, которые будут потом заполненными строками таблицы
def empty_lists(link_list): 
    metalinks = [["path", "date", "author", "title", "text", "wordcount"] for link in link_list]
    return metalinks

#главная функция, которая собирает данные для таблицы
def filling_metadf(lists):
    count_words = 0 #счетчик слов
    for metalink in lists:
        metalink[4] = re.sub(reg_html, '', get_clean_text(page_download(metalink[6])))
        #slugify -- транслитерация; 50 символов берем из-за ограничения на длину названия
        metalink[0] = "plain_text/" + "/".join(metalink[6].split("/")[4:6]) + "/" + slugify(to_txt(page_download(metalink[6]))[0].replace("-", "")[0:50]) + ".txt"
        metalink[1] = ".".join(metalink[6].split("/")[4:7])
        metalink[3] = to_txt(page_download(metalink[6]))[0].replace("-", "")
        #подсчет длины
        metalink[5] = len(word_tokenize(metalink[4]))
        #автор указан далеко не всегда
        if get_author(to_txt(page_download(metalink[6]))[1]):
            metalink[2] = get_author(to_txt(page_download(metalink[6]))[1]).replace('"', '').strip()
        else:
            metalink[2] = "Не указан"
        count_words += metalink[5]
        #это изменение в программе (важное для времени её работы) произошло уже после загрузки страниц, поэтому символов в итоге больше
        #его минусы: потом надо чистить датасет от пустых строк; его плюсы: не надо грузить 10 млн токенов
        if count_words > 5500000:
            break
    return lists

#создаем таблицу из наших списков с информацией о статьях
def table_maker(names, lists):
    df = pd.DataFrame(columns=names)
    for i, line in enumerate(lists):
        df.loc[i] = lists[i]
    return df

#финальный вариант таблицы
def final_table():
    mk_df = table_maker(["path", "date", "author", "title", "text", "wordcount", "link"], filling_metadf(empty_lists(getting_links_for_parse())))
    #убираем шаблонные строки (см. примечание к count_word в filling_metadf
    mk_df = mk_df[mk_df["wordcount"] != "wordcount"]
    #источников на другие сайты МК нигде не указывает, поэтому про то, что надо добавить еще один столбец, вспомнить можно не сразу
    mk_df["source"] = "mk.ru"
    #записываем табличку в файл
    mk_df.to_csv(path_or_buf=os.getcwd() + r"/" + "mk_df.csv", sep="\t")
    return mk_df


#Запись текста

# функция, которая создаёт по заданному интервалу список лет
def list_for_years(interval):
    years_list = []
    year = interval[0][1]
    while year <= interval[1][1]:
        years_list.append(year)
        year += 1
    return (years_list)


# функция, которая создаёт каталоги за заданный период
def catalog_maker(interval, head):
    for year in list_for_years(interval):
        if year in list_for_years(interval)[1:-1]:
            for month in months_list:
                try:
                    os.makedirs(os.getcwd() + r"/" + head + r"/" + str(year) + r"/" + month)
                except FileExistsError:
                    pass

        elif year == list_for_years(interval)[0]:
            for month in months_list[interval[0][0] - 1:]:
                try:
                    os.makedirs(os.getcwd() + r"/" + head + r"/" + str(year) + r"/" + month)
                except FileExistsError:
                    pass

        else:
            for month in months_list[:interval[1][0]]:
                try:
                    os.makedirs(os.getcwd() + r"/" + head + r"/" + str(year) + r"/" + month)
                except FileExistsError:
                    pass

#создаем каталоги для простого текста и майстема
def my_and_plain():
    catalog_maker(interval, "plain_text")
    catalog_maker(interval, "my_stem")

#запись всех простых файлов
def plain_write():
    for i, line in enumerate(final_table()["text"]):
        with open(os.getcwd() + "/" + final_table()["path"][i]+"/", "w+") as f:
            f.write(final_table()["text"][i])

#все ссылки на все файлы
def links_to_folders():
    paths = []
    for i, line in enumerate(final_table()["text"]):
        paths.append(os.getcwd() + "/" + final_table()["path"][i])
    return paths

#MyStem

#функция для обработки одного файла в майстеме через командную строку
def mystem_for_file (path_to_file, path_to_new):
    os.system (mystem_path + " -d -i" + " " + path_to_file + " " + path_to_new)

#проходим Майстемом по всем файлам и создаем соответствующие обработанные файлы в каталоге my_stem
def mystem_files(paths):
    for path in paths:
        mystem_for_file (path, path.replace("plain_text", "my_stem"))

#запускаем программу
if __name__ == "__main__":
    my_and_plain()
    final_table()
    plain_write()
    mystem_files(links_to_folders())
