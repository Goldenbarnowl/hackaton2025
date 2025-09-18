from aiogram.types import KeyboardButton, WebAppInfo, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

slovar = {"buttonkey1": "🏥 О нас",
          "buttonkey2": "📍 Наш адрес на карте",
          "buttonkey3": "💬 FAQ",
          "buttonkey4": "📝 Получить справку",
          "buttonkey5": "⚙️ Техподдержка",
          "buttonkey_st": "✅ Я согласен на обработку персональных данных"}


faqs = {"faq1": "Как узнать больше о больнице?",
        "faq2": "Где находится больница?",
        "faq3": "Как оформить медицинскую справку?",
        "faq4": "Куда написать, если есть проблема или вопрос?",
        "faq5": "Как оставить отзыв о работе больницы?"}


answers = {"faq1": "Всё просто! Нажмите кнопку «🏥 О нас» — там есть информация о наших отделениях, врачах и услугах.",
           "faq2": "Нажмите кнопку «📍 Наш адрес на карте» — я покажу вам местоположение и схему проезда.",
           "faq3": "Выберите пункт «📝 Получить справку». Всё займет меньше 5 минут! 📄✨"
                   "\n\nСправки оформляются в течение 1–2 рабочих дней.",
           "faq4": "Нажмите «⚙️ Техподдержка» → опишите проблему → мы ответим в течение 15 минут в рабочее время! 🛎️⏳",
           "faq5": "Нажмите «Оставить отзыв» ваше мнение очень важно для нас! 💙🌟"
                   "Мы читаем все отзывы и становимся лучше благодаря вам!"}


def keyboard_maker():
    builder = ReplyKeyboardBuilder()
    button1 = KeyboardButton(text=slovar["buttonkey1"])
    builder.row(button1)
    button2 = KeyboardButton(text=slovar["buttonkey2"], web_app=WebAppInfo(url="https://yandex.ru/maps/-/CLeeAC2p"))
    builder.row(button2)
    button3 = KeyboardButton(text=slovar["buttonkey3"])
    builder.row(button3)
    button4 = KeyboardButton(text=slovar["buttonkey4"])
    builder.row(button4)
    button5 = KeyboardButton(text=slovar["buttonkey5"])
    builder.row(button5)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def keyboard_start():
    builder = ReplyKeyboardBuilder()
    button_st = KeyboardButton(text=slovar["buttonkey_st"], request_contact=True)
    builder.row(button_st)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def keyboard_faq():
    builder = InlineKeyboardBuilder()

    for faq in faqs.keys():
        button = InlineKeyboardButton(text=faqs[faq], callback_data=faq)
        builder.row(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def keyboard_stars():
    builder = InlineKeyboardBuilder()

    for star in range(1,6):
        button = InlineKeyboardButton(text=str(star)+"⭐️", callback_data=str(star)+"⭐")
        builder.add(button)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


def keyboard_review():
    builder = InlineKeyboardBuilder()
    button1 = InlineKeyboardButton(text="Оставить отзыв", url="https://yandex.ru/maps/-/CLeeAC2p")
    builder.row(button1)
    return builder.as_markup(resize_keyboard=True, is_persistent=True)


