import random

import telebot
from telebot import types  # для указание типов

bot = telebot.TeleBot("6014682117:AAFfAdFLn8i62aQq8DYREr_q0S2Z2hJ1-P0")

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
il1Lo0O = 'il1Lo0O'

chars = []


@bot.message_handler(commands=['start'])  # первое приветственное сообщение
def start(message):
    chars.clear()
    bot.send_message(message.chat.id, text="Добро пожаловать в Генератор паролей".format(message.from_user))
    bot.send_message(message.chat.id, text="Сколько паролей нужно сгенерировать?".format(message.from_user))
    bot.register_next_step_handler(message, pas_is_quantity)  # следующий шаг – функция pas_is_quantity


def pas_is_quantity(message):  # Сколько паролей нужно сгенерировать?
    global is_quantity
    is_quantity = message.text
    if is_quantity.isdigit() != True:
        bot.send_message(message.chat.id, text="Попробуйте еще раз ...".format(message.from_user))
    elif is_quantity.isdigit() == True:
        bot.send_message(message.chat.id, text="Генерирую " + is_quantity + '. Договорились.'.format(message.from_user))
        bot.send_message(message.chat.id, text="Какая длинна у пароля(-ей)?".format(message.from_user))
        bot.register_next_step_handler(message, pass_is_lenght)  # следующий шаг – функция pass_is_lenght


def pass_is_lenght(message):  # Какая длинна у пароля(-ей)?
    global is_lenght
    is_lenght = message.text
    if is_lenght.isdigit() != True:
        bot.send_message(message.chat.id, text="Попробуйте еще раз ...".format(message.from_user))
    elif is_lenght.isdigit() == True:
        bot.send_message(message.chat.id, text="Длинна у пароля(-ей) " + is_lenght + ' символов. Договорились.'.format(
            message.from_user))
        bot.send_message(message.chat.id, text='Включать-ли цифры ' + digits + "? (да, нет)".format(message.from_user))
        bot.register_next_step_handler(message, pas_is_digits)  # следующий шаг – функция pas_is_digits


def pas_is_digits(message):  # Включать-ли цифры
    global is_digits
    is_digits = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)

    if message.text == "Да" or message.text == "да":
        chars.append(1)
        bot.send_message(message.chat.id, text="Цифры " + digits + ' будут в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Включать ли прописные буквы ' + uppercase_letters + "? (да, нет)".format(
                             message.from_user))
        bot.register_next_step_handler(message, pas_is_uppers)  # следующий шаг – функция pas_is_uppers
    elif message.text == "Нет" or message.text == "нет":
        chars.append(0)
        bot.send_message(message.chat.id, text="Цифр " + digits + 'не будет в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Включать ли прописные буквы ' + uppercase_letters + "? (да, нет)".format(
                             message.from_user))
        bot.register_next_step_handler(message, pas_is_uppers)  # следующий шаг – функция pas_is_uppers


def pas_is_uppers(message):  # Включать ли прописные буквы
    global is_uppers
    is_uppers = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    if message.text == "Да" or message.text == "да":
        chars.append(1)
        bot.send_message(message.chat.id,
                         text="Прописные буквы " + uppercase_letters + ' будут в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id, text='Включать ли строчные буквы ' + lowercase_letters + "? (да, нет)".format(
            message.from_user))
        bot.register_next_step_handler(message, pas_is_lowers)  # следующий шаг – функция pas_is_lowers
    elif message.text == "Нет" or message.text == "нет":
        chars.append(0)
        bot.send_message(message.chat.id,
                         text="Прописных букв " + uppercase_letters + ' не будет в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id, text='Включать ли строчные буквы ' + lowercase_letters + "? (да, нет)".format(
            message.from_user))
        bot.register_next_step_handler(message, pas_is_lowers)  # следующий шаг – функция pas_is_lowers


def pas_is_lowers(message):  # Включать ли строчные буквы
    global is_lowers
    is_lowers = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    if message.text == "Да" or message.text == "да":
        chars.append(1)
        bot.send_message(message.chat.id,
                         text="Строчные буквы " + lowercase_letters + ' будут в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Вкючать ли специальные символы ' + punctuation + "? (да, нет)".format(message.from_user))
        bot.register_next_step_handler(message, pas_is_punctuation)  # следующий шаг – функция pas_is_uppers
    elif message.text == "Нет" or message.text == "нет":
        chars.append(0)
        bot.send_message(message.chat.id,
                         text="Строчных букв " + lowercase_letters + ' не будет в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Вкючать ли специальные символы ' + punctuation + "? (да, нет)".format(message.from_user))
        bot.register_next_step_handler(message, pas_is_punctuation)  # следующий шаг – функция pas_is_punctuation


def pas_is_punctuation(message):  # Вкючать ли специальные символы
    global is_punctuation
    is_punctuation = message.text

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    if message.text == "Да" or message.text == "да":
        chars.append(1)
        bot.send_message(message.chat.id,
                         text="Специальные символы " + punctuation + ' будут в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Вкючать ли однозначные символы ' + il1Lo0O + "? (да, нет)".format(message.from_user))
        bot.register_next_step_handler(message, pas_is_il1Lo0O)  # следующий шаг – функция pas_is_il1Lo0O
    elif message.text == "Нет" or message.text == "нет":
        chars.append(0)
        bot.send_message(message.chat.id,
                         text="Специальных символов " + punctuation + ' не будет в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id,
                         text='Вкючать ли однозначные символы ' + il1Lo0O + "? (да, нет)".format(message.from_user))
        bot.register_next_step_handler(message, pas_is_il1Lo0O)  # следующий шаг – функция pas_is_il1Lo0O


def pas_is_il1Lo0O(message):
    global is_il1Lo0O
    is_il1Lo0O = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Да")
    btn2 = types.KeyboardButton("Нет")
    markup.add(btn1, btn2)
    if message.text == "Да" or message.text == "да":
        chars.append(1)
        bot.send_message(message.chat.id,
                         text="Однозначные символы " + il1Lo0O + ' будут в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id, text="Генерирую пароль...введите Ок".format(message.from_user))
        bot.register_next_step_handler(message, password)  # следующий шаг – функция password
    elif message.text == "Нет" or message.text == "нет":
        chars.append(0)
        bot.send_message(message.chat.id,
                         text="Однозначных символов " + il1Lo0O + ' не будет в пароле.'.format(message.from_user))
        bot.send_message(message.chat.id, text="Генерирую пароль...введите Ок".format(message.from_user))
        bot.register_next_step_handler(message, password)  # следующий шаг – функция password


def password(message):
    pas_chars = []
    pas_chars2 = []

    if chars[0] == 1:
        pas_chars.extend(digits)
    if chars[1] == 1:
        pas_chars.extend(uppercase_letters)
    if chars[2] == 1:
        pas_chars.extend(lowercase_letters)
    if chars[3] == 1:
        pas_chars.extend(punctuation)
    if chars[4] == 0:
        for i in pas_chars:
            if i not in il1Lo0O:
                pas_chars2.append(i)
            else:
                continue
        pas_chars = pas_chars2
    if int(is_lenght) > len(pas_chars):
        pas_chars = pas_chars * int(is_lenght)
    # list_string = ''.join(pas_chars)
    # list_string2 = ''.join(str(chars))
    if message.text == "Ок":
        for i in range(int(is_quantity)):
            # bot.send_message(message.chat.id, text=len(int(pas_chars)).format(message.from_user))
            bot.send_message(message.chat.id,
                             text=''.join(random.sample(pas_chars, int(is_lenght))).format(message.from_user))
            # bot.send_message(message.chat.id, text=list_string.format(message.from_user))
            # bot.send_message(message.chat.id, text=list_string2.format(message.from_user))


bot.polling(none_stop=True)
