import asyncio

from aiogram import Router, F
from aiogram.filters import CommandStart, Filter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile, CallbackQuery

from config import bot
from src.keyboard import keyboard_maker, slovar, keyboard_start, keyboard_faq, answers, keyboard_stars, keyboard_review
from src.states import UserStates

user_router = Router()

@user_router.message(CommandStart())
async def f1(message: Message, state: FSMContext):
    await bot.send_document(
        chat_id=message.chat.id,
        caption="Привет! 👋"
                "\nРады приветствовать вас в сервисе цифровой больницы! 🏥💙"
                "\n\nЯ — ваш помощник в получении медицинских справок и других документов. Со мной всё просто и быстро! ✨"
                "\n\nЧтобы начать, мне нужно знать ваш номер телефона 📱"
                "\nЭто нужно для безопасности и быстрого доступа к вашим данным."
                "\n\nТакже нам потребуется ваше согласие на обработку персональных данных."
                "\nЭто стандартная процедура, чтобы всё было по закону и ваши данные были под защитой 🔒"
                "\n\nНажмите на кнопку ниже, чтобы продолжить 👇"
                "\n\nЕсли что-то пойдёт не так — просто введите /start, и я всё перезапущу! 🔄",
        reply_markup=keyboard_start(),
        document=FSInputFile("./Политика конфиденциальности.docx.pdf")
    )
    await state.set_state(UserStates.pologenie1)


@user_router.message(UserStates.pologenie1, F.content_type == "contact")
async def f2(message: Message, state: FSMContext):
    contact = message.contact
    chat_id = message.chat.id

    if contact.user_id != message.from_user.id:
        await bot.send_message(
            chat_id=chat_id,
            text="Для продолжения работы нажмите на кнопку «Я согласен на обработку персональных данных»"
        )
        return
    await state.set_state(UserStates.menu)
    await bot.send_message(
        chat_id=chat_id,
        text="Отлично! Вы успешно зарегистрированы! ✅"
             "\nТеперь вам доступны все возможности бота 🏥💙"
             "\n\nЧто бы вы хотели сделать?",
        reply_markup=keyboard_maker()
    )
    await asyncio.sleep(120)
    await bot.send_message(
        chat_id=message.chat.id,
        text="Спасибо, что выбрали нашу клинику! 💙"
             "\nПомогите нам стать лучше — оцените, пожалуйста, ваше посещение от 1 до 5 🌟"
             "\n\nВаше мнение очень важно для нас!",
        reply_markup=keyboard_stars()
    )


@user_router.message(UserStates.menu, F.text == slovar["buttonkey1"])
async def f3(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="🏥 Наша больница – это современный медицинский центр, где мы заботимся о вашем здоровье с теплотой и профессионализмом."
             "\n\n✨ Что мы предлагаем:"
             "\n• Консультации врачей разных специальностей"
             "\n• Диагностику и анализы"
             "\n• Помощь в оформлении медицинских документов"
             "\n• Комфортное и внимательное обслуживание"
             "\n\n💙 Мы работаем, чтобы вы оставались здоровыми и чувствовали нашу поддержку!"
    )


@user_router.message(UserStates.menu, F.text == slovar["buttonkey3"])
async def f4(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="❓ Частые вопросы (FAQ)",
        reply_markup=keyboard_faq()
    )


@user_router.message(UserStates.menu, F.text == slovar["buttonkey4"])
async def f5(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Обрабатываем запрос... ⏳"
             "\nСкоро всё будет готово!"
    )
    await asyncio.sleep(10)
    await bot.send_message(
        chat_id=message.chat.id,
        text="🎉 Ваша справка готова!"
             "\nМожете забирать её в регистратуре 📄✨"
             "\n\nСпасибо, что пользуетесь нашим сервисом! Если нужна ещё помощь — я всегда тут 😊"
    )


@user_router.message(UserStates.menu, F.text == slovar["buttonkey5"])
async def f6(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Опишите, пожалуйста, вашу проблему или вопрос. Мы постараемся помочь как можно скорее! 🤗",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.tech_wait)


@user_router.message(UserStates.tech_wait)
async def f7(message: Message, state: FSMContext):
    await bot.send_message(
        chat_id=1000060754,
        text=message.text
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text="✅ Ваше обращение принято!"
             "\nНаша команда уже занимается вашим вопросом и свяжется с вами в ближайшее время. Обычно это занимает до 15 минут в рабочее время. ⏳💙",
        reply_markup=keyboard_maker()
    )
    await state.set_state(UserStates.menu)


@user_router.callback_query(F.data.contains("⭐"))
async def f0(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data in ("1⭐", "2⭐", "3⭐"):
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text="🛎️ Нажмите «⚙️ Техподдержка» и опишите вашу проблему."
                 "\nМы поможем вам в ближайшее время!"
        )
    if callback_query.data in ("4⭐", "5⭐"):
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text="Мы будем очень благодарны, если вы поделитесь впечатлениями о работе нашего сервиса! Это поможет нам стать лучше. 💙",
            reply_markup=keyboard_review()
        )


@user_router.callback_query(UserStates.menu)
async def f7(callback_query: CallbackQuery, state: FSMContext):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=answers[callback_query.data]
    )

