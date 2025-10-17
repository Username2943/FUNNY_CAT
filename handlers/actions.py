import os

history = []

def handle_action(bot, message):
    '''Нажал кнопку погладить кота'''
    text = message.text

    if 'Погладить' in text:
        history.append('Погладить кота')
        photo_path = os.path.join("media", "koska.jpg")
        if os.path.exists(photo_path):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption='Кот доволен, он счастлив')
    elif 'Обнять' in text:
        history.append('Обнять кота')
        photo_path2 = os.path.join("media", "kosecki.jpg")
        if os.path.exists(photo_path2):
            with open(photo_path2, 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption='Кот доволен, он счастлив')