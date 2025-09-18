from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    pologenie1 = State()
    pologenie2 = State()
    tech_wait = State()
    menu = State()
