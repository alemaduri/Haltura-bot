import telebot
import setup

bot = telebot.TeleBot(setup.haltura_reg_team)

@bot.message_handler(commands = ['start'])
def send(message):
    bot.send_message(message.chat.id, 'Приветствую, халтурщик!\nДобро пожаловать в нашего скромного бота)\nДля входа в команду заполни форму.')
    bot.send_message(message.chat.id, '1. Кто тебя привёл?(ник знакомого, реклама и тд.)\n2. Какие у тебя цели( заработать денег, обучиться СИ и заработать денег, срочно заработать много денег и тд.)?\n3. Предпосылки к цели( получить фин.независимость, заработать на покупку и тд.)?\n4. Опиши свой опыт работы в данной сфере( команды, свои темы и тд.), как долго в сфере?( от этого будет зависеть твой процент)\n ПИШИ ВСЕ ОДНИМ СООБЩЕНИЕМ!')

@bot.message_handler(content_types = ['text'])
def second(message):
    if message.chat.id == setup.admin:
        text = message.text.lower()
        splitted = text.split(' ')
        if splitted[0] == 'добавить':
            bot.send_message(splitted[1], 'https://t.me/joinchat/GevzRJuAkyWZqFKC')
    bot.send_message(message.chat.id, 'После заполнения формы мы обработаем заявку и примем тебя в течение часа-дня.')
    bot.send_message(setup.admin, message.text + '\n' + str(message.chat.id))


bot.infinity_polling()
