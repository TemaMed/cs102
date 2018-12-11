import datetime as dt
import requests
import config
import telebot
from bs4 import BeautifulSoup
from datetime import datetime
import calendar


bot = telebot.TeleBot(config.telebot_CONFIG['access_token'])


def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.telebot_CONFIG['domain'],
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_day(web_page, number_day: str):
    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием на понедельник
    schedule_table = soup.find("table", attrs={"id": number_day + "day"})

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text+room.dd.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.replace('\n', '').replace('\t', '') for lesson in lessons_list]

    return times_list, locations_list, lessons_list


def parse_schedule_for_a_near_lesson(web_page, number_day: str):
    soup = BeautifulSoup(web_page, "html5lib")
    status = True
    # Получаем таблицу с расписанием на день
    schedule_table = soup.find("table", attrs={"id": number_day + "day"})
    if schedule_table is None:
        status = False
        return status, None

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text + ", №:" + room.dd.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.replace('\n', '').replace('\t', '') for lesson in lessons_list]

    return status, (times_list, locations_list, lessons_list)


@bot.message_handler(commands=['monday'])
def get_monday(message):
    """ Получить расписание на понедельник """
    day, group = message.text.split()
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_day(web_page, '1')
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '{},<b>{}</b>,{}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    number_day = '0'
    day, group = message.text.split()
    web_page = get_page(group)
    if day == "/monday":
        number_day = "1"
    elif day == "/tuesday":
        number_day = "2"
    elif day == "/wednesday":
        number_day = "3"
    elif day == "/thursday":
        number_day = "4"
    elif day == "/friday":
        number_day = "5"
    elif day == "/saturday":
        number_day = "6"
    elif day == "/sunday":
        number_day = "7"
    times_lst, locations_lst, lessons_lst = \
        parse_schedule_for_day(web_page, number_day)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>, <b>{}</b>, {}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    day, group = message.text.split()
    week_number = dt.date.today().isocalendar()[1]
    if week_number % 2 == 1:
        week_number = "2"
    else:
        week_number = "1"
    time = dt.datetime.now().time()
    ltime = str(time).split(":")
    time = float(ltime[0] + "." + ltime[1])
    day = dt.datetime.isoweekday(dt.datetime.today())
    web_page = get_page(group, week_number)
    skip_day = False
    resp = ''
    while True:
        status, lists = parse_schedule_for_a_near_lesson(web_page, str(day))
        if not status:
            skip_day = True
            day += 1
            if day > 7:
                day = 1
                if week_number == 2:
                    week_number = 1
                else:
                    week_number = 2
                web_page = get_page(group, str(week_number))
            continue
        times = lists[0]
        if skip_day:
            resp += '<b>{}</b>, {}, {}\n'.format(lists[0][0], lists[1][0], lists[2][0])
            break
        i = -1
        for lessons in times:
            i += 1
            lessons = float(str(lessons).split("-")[0].replace(":", "."))
            if time < lessons:
                resp += '<b>{}</b>, {}, {}\n'.format(lists[0][i], lists[1][i], lists[2][i])
                break
            elif i == len(times) - 1:
                day += 1
                if day > 7:
                    day = 1
                    if week_number == 2:
                        week_number = 1
                    else:
                        week_number = 2
                continue

        break
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['tommorow'])
def get_tommorow(message):
    """ Получить расписание на следующий день """
    number_day = datetime.isoweekday(datetime.today()) + 1
    if number_day == 8:
        number_day = 1
    day, group = message.text.split()
    web_page = get_page(group)
    number_day = str(number_day)
    try:
        times_lst, locations_lst, lessons_lst = parse_schedule_for_day(web_page, number_day)
        resp = ''
        for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
            resp += '<b>{}</b>, {}, {}\n'.format(time, location, lession)
        bot.send_message(message.chat.id, resp, parse_mode='HTML')
    except AttributeError:
        resp = "<b>Нет пар</b>"
        bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    day, group = message.text.split()
    week_number = dt.date.today().isocalendar()[1]
    if week_number % 2 == 1:
        week_number = "2"
    else:
        week_number = "1"
    web_page = get_page(group, week_number)
    resp = ''
    days = ("1", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресение")
    for i in range(1, 8):
        resp += '<b>{}</b>\n'.format(days[i])
        try:
                times_lst, locations_lst, lessons_lst = \
                    parse_schedule_for_day(web_page, str(i))
                for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
                    resp += '{},<b>{}</b>,{}\n'.format(time, location, lession)
        except AttributeError:
            resp += '{}\n'.format('Нет Пар')
        if i == 7:
            bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
