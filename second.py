import telebot


TOKEN = "6860802226:AAG-XIz69_TxQjV1JDYrpeKiTbdvENWtEnI"

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hello")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()

#
# km_in_mil = 1.61
# mil = int(input("введите кол-во миль: "))
# print(mil*km_in_mil)




# def main():
#     print(int(input("Введите кол-во миль: ")) * 1.61)
#
# if __name__ == '__main__': main()







