from clarifai.rest import ClarifaiApp
from emoji import emojize
from random import choice, randint
from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, вы выиграли"
    elif user_number == bot_number:
        message = f"Ваше число {user_number}, мое {bot_number}, ничья"
    else:
        message = f"Ваше число {user_number}, мое {bot_number}, вы проиграли"
    return message

def main_keyboard():
    return ReplyKeyboardMarkup([
        ['Прислать котика', KeyboardButton('Мои координаты', request_location=True), 'Заполнить анкету']
    ])

def is_cat(file_name):
    app = ClarifaiApp(api_key=settings.CLARIFAI_API_KEY)
    model = app.public_models.general_model
    responce = model.predict_by_filename(file_name, max_concepts=5)
    if responce['status']['code'] == 10000:
        for concept in responce['outputs'][0]['data']['concepts']:
            if concept['name'] == 'cat':
                return True
    return False

if __name__ == "__main__":
    print(is_cat("images/cat1.jpg"))
    print(is_cat("images/not_cat.jpg"))
