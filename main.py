import telebot
import openai

openai.api_key = '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'

bot = telebot.TeleBot('6515433115:AAGTjoOkO24oDMof_lvVk2quk19Hn86E-2U')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    response = openai.Completion.create(
        engine='davinci',
        prompt=user_input,
        max_tokens=100
    )

    bot.reply_to(message, response.choices[0].text)

bot.polling()
