import time
import telebot
from telebot import types
import psutil
from threading import Thread

token = 'Сюда нужно вставить токен'
bot = telebot.TeleBot(token)

print(bot)
print(bot.get_me())

@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
  bot.answer_callback_query(call.id)                # Отправка ответа, что запрос обработан
  if call.data == 'button_1':
    bot.send_message(call.message.chat.id, str(psutil.cpu_freq()))
  elif call.data == 'button_2':
    bot.send_message(call.message.chat.id, str(psutil.sensors_battery()))
@bot.message_handler(commands=['start'])
def start_message(message):
  Buttons = types.InlineKeyboardMarkup(row_width=2)
  button_1 = types.InlineKeyboardButton(text='Кнопка 1', callback_data='button_1')
  button_2 = types.InlineKeyboardButton(text='Кнопка 2', callback_data='button_2')
  Buttons.add(button_1, button_2)

  bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=Buttons)

@bot.message_handler(commands=['info'])
def info_message(message):
  bot.send_message(message.chat.id, f'ID этого чата: {message.chat.id}')
@bot.message_handler(commands=['help'])
def help_message(message):
  bot.send_message(message.chat.id, 'Здесь будет наша подсказка')
@bot.message_handler(regexp=r'\d{4}')
def parse_message(message):
  bot.send_message(message.chat.id, "Сообщение содержит число из четырех цифр")

def parallel_task():
    while True:
        print('I am here')
        time.sleep(2)

thread1 = Thread(target = bot.infinity_polling)
thread2 = Thread(target = parallel_task)

thread1.start() # запускает ранее созданный поток
thread2.start()
thread1.join() # останавливает поток, когда тот выполнит свои задачи
thread2.join()
