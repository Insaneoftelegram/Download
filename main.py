import telebot
import yt_dlp

bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(content_types=['text'])
def handle_message(message):
    if 'youtube.com/watch?v=' in message.text:
        song_url = message.text
        song_name = song_url.split('=')[1]
        song_file = yt_dlp.YoutubeDL().extract_info(song_url, download=True)['filename']
        bot.send_message(message.chat.id, f'Downloading song {song_name}...')
        bot.send_document(message.chat.id, song_file)

bot.polling()
