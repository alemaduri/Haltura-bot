import telebot

main = telebot.types.ReplyKeyboardMarkup(True, True)
main.row('18+ Заработок', '18- Заработок')
main.row('Активный заработок', 'Пассивный заработок')
main.row('Онлайн заработок', 'Оффлайн заработок')
main.row('Белый заработок', 'Серый заработок')
main.row('Каталог товаров', 'Связь с админом')

go_back = telebot.types.ReplyKeyboardMarkup(True, True)
go_back.row('Назад')

buying = telebot.types.ReplyKeyboardMarkup(True, True)
buying.row('Купить', 'Назад')

paying = telebot.types.ReplyKeyboardMarkup(True, True)
paying.row('Я оплатил', 'Назад')