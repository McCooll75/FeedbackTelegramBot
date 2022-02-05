from time import sleep
import telebot
import datetime
token = 'token'
bot = telebot.TeleBot(token)
manager_id = 'reciever_id'
show_stick = 1
date = datetime.datetime.now()

#
# Code is a bit longer than can be
# But it works
#

#/start
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Hello! Send your message.")


def Action(name, id, user, text, photo, video):
    bot.send_message(manager_id, f'Name: <a href="tg://user?id={id}">{name}</a>\nUser: {user}\nTime: {date.day}/{date.month}/{date.year} | {date.hour}:{date.minute}\nText: {text}', parse_mode='html')
    if photo != 0:
        bot.send_photo(manager_id, photo)
    if video != 0:
        bot.send_video(manager_id, video)
    global show_stick
    if show_stick == 1:
        show_stick = 0
        sleep(20)
        bot.send_message(id, 'Thank you!.')
        bot.send_sticker(id, open('sticker/path/sticker.webp', 'rb'))
        show_stick = 1


#текст
@bot.message_handler(content_types=['text'])
def talk(message):
    text = message.text
    user = '@'+str(message.chat.username)
    #Name Check
    if str(message.chat.last_name) == 'None':
        name = str(message.chat.first_name)
    elif message.chat.last_name != 'None':
        name = str(message.chat.first_name) + ' ' + str(message.chat.last_name)
    #Client ID
    id = message.from_user.id

    #Data send
    Action(name, id, user, text, 0, 0)

@bot.message_handler(content_types=['photo'])
def get_Image(message):
    photo = message.photo[-1].file_id

    user = '@'+str(message.chat.username)
    #Name Check
    if str(message.chat.last_name) == 'None':
        name = str(message.chat.first_name)
    elif message.chat.last_name != 'None':
        name = str(message.chat.first_name) + ' ' + str(message.chat.last_name)
    #Client ID
    id = message.from_user.id

    Action(name, id, user, 'photo (see below)', photo, 0)

@bot.message_handler(content_types=['video'])
def get_video(message):
    video = message.video.file_id

    user = '@'+str(message.chat.username)
    #Remove None from surname
    if str(message.chat.last_name) == 'None':
        name = str(message.chat.first_name)
    elif message.chat.last_name != 'None':
        name = str(message.chat.first_name) + ' ' + str(message.chat.last_name)
    #Client ID again
    id = message.from_user.id

    Action(name, id, user, 'video (see below)', 0, video)

bot.polling(none_stop=True)
