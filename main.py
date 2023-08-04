# -*- coding: utf-8 -*-
import json
import telebot
from telebot import types
import custom
import setup
import keyboards

bot = telebot.TeleBot(setup.bot1)
admin = telebot.TeleBot(setup.admin_bot)
me = telebot.TeleBot(setup.me)
db = json.load(open('db.json', 'r'))

def save_db(db, file_name = 'db.json'):
    dbjob = open(file_name, 'w')
    dbjob.write(json.dumps(db, ensure_ascii = False, indent = 4))
    dbjob.close()

menu = 'Выберите интересующую вас схему \n1. Заработок на продаже плюшевых медведей\n2. Заработок на продаже картинок\n3. Заработок на кошельке Payeer\n4. Заработок на смс\n5. Заработок на документах в ВК\n6. Заработок на халяве со всего Telegram\n7. Заработок на продаже готовых шаблонов ()\n8. Заработок на просмотре фотографий\n9. Заработок на монетизации статей на Яндекс Дзен\n10. Получаем халявные 3500р и рубим деньги на пассиве!\n11. Заработок на выполнении заданий в приложении\n12. Заработок на загрузочно трафике за счет инстаграма\n13. Заработок на чатах в телеграме\n14. Пассивный доход на играх с помощью YouTube и Twitch\n15. Монетизация на яндекс эфире\n16. Пассивный заработок на уведомлениях\n17. Фарм Биг Маков \n18. Стать частью команды(t.me/Haltura_Join_Team_Bot) \n 19. АльфаБанк 1.0 \n 20. АльфаБанк 2.0 \n21. Схема с кровью\n22.Продажа верифицированных киви аккаунтов'
welcome_msg = '💰Халтура- Подработка; побочный заработок; работа, выполняемая помимо или за счёт основной.💰\n\n💸В детстве мне казалось, что нормальные деньги невозможно заработать в интернете, особенно если тебе нет 18. Казино, ставки, пирамиды, работа кладменом, инфоцыганство, бинарные опционы( не путать с акциями и инвертированием, это тема здравая) и прочее говно убеждали меня в этом. Но я не сдавался и продолжал искать. Так вот, я нашёл. Спустя годы, я рос и пробовал разные способы. Некоторые потребовали от меня активности и выходов на улицу. Я работал фрилансером курьером, открыл с напарниками дропшиппинг бизнес, искал, искал и искал. И вот, перед вами результат многолетнего мозгового штурма, проект всей моей жизни- экосистема «Халтура». в этой экосистеме ты найдёшь абсолютно всё, что можно, для того, чтобы заработать деньги. Канал с предложениями реальной работы на фрилансе и без Найма, бот со схемами для заработка, приём в мою команду и работа по моим авторским схемам. Такого ты не найдёшь нигде, ведь проект реализовала команда энтузиастов( шат аут своим, вы самые лучшие), которые также как и автор текста искали способы заработка в интернете. Добро пожаловать в Халтуру, чувствуй себя как дома. Тебе тут точно понравится. 💸'
welcome_msg_2 = '😏Приветствую тебя, схемщик. В этом боте тебя ждёт множество интересной информации касательно заработка в интернете и не только. Здесь не будет казино, пирамид, ставок, предложений о работе кладменом и прочей дряни. Тут тебя научат грамотно подходить к процессу заработка и как и в любом другом месте понадобиться труд и желание. Без этого никуда, ты сам это прекрасно понимаешь. 😏\n\n❗Смотри, здесь будут представлены белые и серые схемы заработка, возможность заработать на дропшиппинге, получение пассивного дохода от соответствующих проектов( рукапча, everve), благодаря автоматизации процесса, официальное фриланс трудоустройство с соответствующими привилегиями и т.д. ❗\n\n🤓Проект был создан компанией энтузиастов, желающих облегчить жизнь таким же как и они. Наверное, это можно считать старт-апом. Поскольку это старт-ап, мы решили поставить на некоторые схемы довольно условный ценник, который можно окупить сразу же после начала работы по схеме, а многие схемы и вовсе сделали бесплатными, дабы привлечь должное количество клиентов в наш проект. 🤓\n\n🧐В этом сообщении наша команда была максимально честной с тобой. Каждый проект создатель курирует самостоятельно и в цену покупки входит четкое проведение от начала и до конца пути. По бесплатным схемам такой поддержки не будет. Также в платные схемы мы впихнули скрипты и подробнейшие гайды по работе. Так что, по большому счёту ничего кроме c\n\nctrl-c ctrl-v делать не прийдется. 🧐\n\n‼В случае не удовлетворённости и не работе все деньги будут возвращены или будет проведена аналитическая работа. ‼\n\n❕❗❕❗Также у нас есть канал, где в онлайн формате выкладываются обновления по боту и добавляются новые схемы- https://t.me/joinchat/VFFvmdWjvTmryfWq ❗❕❗❕\n\n🔥🔥🔥Еще есть чат офферов с предложениями сотрудничества в офлайн формате( доставить Документы, привлечь людей в заведение, продать кроссовки и прочие товары за процент)- для входа туда выбери соответствующую кнопку в боте или напиши администратору. 🔥🔥🔥\n\n🔞А еще, ты можешь стать частью нашей команды, продавая схемы вместе с нами и зарабатывая неплохие деньги, заполнив форму в этом боте- 🔞\n\n😏Для выбора схемы выберу категорию, которая тебя интересует и нажми на цифру схемы. Ты получишь файл с описанием😏'
tegs = ['18+ Заработок', '18- Заработок', 'Активный заработок', 'Пассивный заработок', 'Онлайн заработок', 'Оффлайн заработок', 'Белый заработок', 'Серый заработок']


@bot.message_handler(commands = ['start'])
def welcome_message(message):
    if message.chat.id in db['id_list']:
        bot.send_message(message.chat.id, 'Вы уже начали общение с ботом', reply_markup = keyboards.main)
        custom.position_set(message.chat.id, db, 'sub_main')
        custom.looking_set(message.chat.id, db, 0)
    else:
        bot.send_message(message.chat.id, welcome_msg)
        bot.send_message(message.chat.id, welcome_msg_2, reply_markup = keyboards.main)
        db['users'].append({'id': message.chat.id, 'position': 'sub_main', 'looking': 0})
        db['id_list'].append(message.chat.id)
        save_db(db)

@bot.message_handler(func = lambda message: custom.position(message.chat.id, db) == 'sub_main')
def sub_main(message):
    if message.text in tegs:
        text_send = custom.generate_text(message.text)
        bot.send_message(message.chat.id, text_send, reply_markup = keyboards.go_back)
        custom.position_set(message.chat.id, db, 'main')
        save_db(db)
    elif message.text == 'Каталог товаров':
        bot.send_message(message.chat.id, 'Покупка Qiwi кошельков, фейков ВК, сим-карт\nQiwi: 500, VK: 90, SIM: 110\nДля покупки написать: @dasolnce', reply_markup = keyboards.main)
    elif message.text == 'Связь с админом':
        bot.send_message(message.chat.id, '@dasolnce', reply_markup = keyboards.main)
    else:
        bot.send_message(message.chat.id, 'Бот не распознал вашу команду', reply_markup = keyboards.main)
    

@bot.message_handler(func = lambda message: custom.position(message.chat.id, db) == 'main')
def main(message):
    try:
        num = int(message.text)
        if num == 18:
            bot.send_message(message.chat.id, '@haltura_reg_team_bot')
            bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
            custom.position_set(message.chat.id, db, 'sub_main')
        elif num == 23:
            bot.send_message(message.chat.id, 'Напишите админу: @dasolnce')
            bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
            custom.position_set(message.chat.id, db, 'sub_main')
        elif num in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27]:
            custom.looking_set(message.chat.id, db, num)
            file_name = 'sxem' + str(num) + '.docx'
            file_ = open(file_name, 'rb')
            bot.send_document(message.chat.id, file_, reply_markup = keyboards.buying)
            custom.position_set(message.chat.id, db, 'looking')
            save_db(db)
        else:
            bot.send_message(message.chat.id, 'Схемы с таким номером не существует, повторите попытку')
    except ValueError:
        if message.text == 'Назад':
            bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
            custom.position_set(message.chat.id, db, 'sub_main')
            custom.looking_set(message.chat.id, db, 0)
        else:
            bot.send_message(message.chat.id, 'Напишите число')

@bot.message_handler(func = lambda message: custom.position(message.chat.id, db) == 'looking')
def buying(message):
    if message.text == 'Купить':
        bot.send_message(message.chat.id, 'Сбербанк-онлайн(СЧЕТ): 40817810740018011026', reply_markup = keyboards.paying)
        custom.position_set(message.chat.id, db, 'buying')
        save_db(db)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
        custom.position_set(message.chat.id, db, 'sub_main')
        custom.looking_set(message.chat.id, db, 0)
        save_db(db)
    else:
        bot.send_message(message.chat.id, 'Бот не распознал вашу команду', reply_markup = keyboards.buying)


@bot.message_handler(func = lambda message: custom.position(message.chat.id, db) == 'buying')
def paying(message):
    if message.text == 'Я оплатил':
        bot.send_message(message.chat.id, 'Отлично, после подтверждения платежа, вам будет выслана схема')
        try:
            admin.send_message(setup.admin, 'Возможно поступил платеж\n' + str(message.chat.id) + '\nСхема номер: ' + str(custom.looking(message.chat.id, db)) + '\n' + 'Стоимость: ' + setup.sxem[custom.looking(message.chat.id, db)]['price'])
        except Exception:
            admin.send_message(setup.admin2, 'Возможно поступил платеж\n' + str(message.chat.id) + '\nСхема номер: ' + str(custom.looking(message.chat.id, db)) + '\n' + 'Стоимость: ' + setup.sxem[custom.looking(message.chat.id, db)]['price'])
        print('Возможно поступил платеж\n' + str(message.chat.id) + '\nСхема номер: ' + str(custom.looking(message.chat.id, db)) + '\n' + 'Стоимость: ' + setup.sxem[custom.looking(message.chat.id, db)]['price'])
        me.send_message(setup.admin2, 'Возможно поступил платеж\n' + str(message.chat.id) + '\nСхема номер: ' + str(custom.looking(message.chat.id, db)) + '\n' + 'Стоимость: ' + setup.sxem[custom.looking(message.chat.id, db)]['price'])

        bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
        custom.position_set(message.chat.id, db, 'sub_main')
        custom.looking_set(message.chat.id, db, 0)
        save_db(db)
    elif message.text == 'Назад':
        bot.send_message(message.chat.id, 'Выберите интересующий Вас раздел', reply_markup = keyboards.main)
        custom.position_set(message.chat.id, db, 'sub_main')
        custom.looking_set(message.chat.id, db, 0)
        save_db(db)
    else:
        bot.send_message(message.chat.id, 'Бот не распознал Вашу команду', reply_markup = keyboards.paying)

@bot.message_handler(content_types = ['text'])
def send_sxem(message):
    if message.chat.id == setup.admin:
        text = message.text.lower()
        splitted = text.split(' ')
        if splitted[0] == 'отправить':
            bot.send_document(splitted[1], open('full_sxem' + str(splitted[2]) + '.docx'), 'Ваш платеж подтвержден, вот Ваша схема:')
            me.send_message(setup.admin2, 'Подтвержден платеж на сумму ' + str(setup.sxem[int(splitted[2])]['price']))
    save_db(db)
            
bot.infinity_polling(True)
admin.polling()
me.polling()
