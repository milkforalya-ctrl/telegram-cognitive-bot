import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command

TOKEN = "8637999190:AAGcu5DJ0Dv8vR9kLFwBGc4DxHsHTCCoy9M»

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ======================
# Хранилище данных
# ======================

user_data = {}

def get_user(user_id):
    if user_id not in user_data:
        user_data[user_id] = {
            "score": 0,
            "games_completed": 0,
            "game1": False,
            "game2": False,
            "game3": False
        }
    return user_data[user_id]

# ======================
# Главное меню
# ======================

def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Обучение", callback_data="menu_learning")
    kb.button(text="Игра", callback_data="menu_games")
    kb.button(text="Результат", callback_data="menu_result")
    kb.adjust(1)
    return kb.as_markup()

@dp.message(Command("start"))
async def start(message: Message):
    get_user(message.from_user.id)
    await message.answer(
        "Главное меню.\nВыберите раздел:",
        reply_markup=main_menu()
    )

# ======================
# ОБУЧЕНИЕ
# ======================

def learning_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Ось 1 — Контекстность", callback_data="axis1")
    kb.button(text="Ось 2 — Скорость", callback_data="axis2")
    kb.button(text="Ось 3 — Сложность", callback_data="axis3")
    kb.button(text="⬅ Назад", callback_data="back_main")
    kb.adjust(1)
    return kb.as_markup()

@dp.callback_query(F.data == "menu_learning")
async def learning(callback: CallbackQuery):
    await callback.message.edit_text(
        "Раздел обучения.\nВыберите ось:",
        reply_markup=learning_menu()
    )

# ===== Ось 1 =====

def axis1_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Поле-зависимый", callback_data="axis1_dep")
    kb.button(text="Поле-независимый", callback_data="axis1_indep")
    kb.button(text="⬅ Назад", callback_data="menu_learning")
    kb.adjust(1)
    return kb.as_markup()

@dp.callback_query(F.data == "axis1")
async def axis1(callback: CallbackQuery):
    await callback.message.edit_text(
        "Ось 1 — Контекстность.\nВыберите тип:",
        reply_markup=axis1_menu()
    )

@dp.callback_query(F.data == "axis1_dep")
async def axis1_dep(callback: CallbackQuery):
    await callback.message.edit_text(
        "Поле-зависимый тип:\n"
        "• Видит ситуацию целостно\n"
        "• Ориентируется на социальные сигналы\n"
        "• Учитывает атмосферу\n\n"
        "В рекламе реагирует на инфлюенсеров и социальное доказательство.",
        reply_markup=axis1_menu()
    )

@dp.callback_query(F.data == "axis1_indep")
async def axis1_indep(callback: CallbackQuery):
    await callback.message.edit_text(
        "Поле-независимый тип:\n"
        "• Анализирует характеристики\n"
        "• Структурирует информацию\n"
        "• Принимает автономные решения\n\n"
        "В рекламе реагирует на аргументы и сравнения.",
        reply_markup=axis1_menu()
    )

# ===== Ось 2 =====

def axis2_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Импульсивный", callback_data="axis2_imp")
    kb.button(text="Рефлексивный", callback_data="axis2_ref")
    kb.button(text="⬅ Назад", callback_data="menu_learning")
    kb.adjust(1)
    return kb.as_markup()

@dp.callback_query(F.data == "axis2")
async def axis2(callback: CallbackQuery):
    await callback.message.edit_text(
        "Ось 2 — Скорость принятия решения.\nВыберите тип:",
        reply_markup=axis2_menu()
    )

@dp.callback_query(F.data == "axis2_imp")
async def axis2_imp(callback: CallbackQuery):
    await callback.message.edit_text(
        "Импульсивный тип:\n"
        "• Принимает решение быстро\n"
        "• Реагирует на эмоции и триггеры\n\n"
        "В рекламе эффективны короткие форматы и акции.",
        reply_markup=axis2_menu()
    )

@dp.callback_query(F.data == "axis2_ref")
async def axis2_ref(callback: CallbackQuery):
    await callback.message.edit_text(
        "Рефлексивный тип:\n"
        "• Сравнивает варианты\n"
        "• Ищет подтверждение\n\n"
        "В рекламе эффективны аргументы и кейсы.",
        reply_markup=axis2_menu()
    )

# ===== Ось 3 =====

def axis3_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Низкая сложность", callback_data="axis3_low")
    kb.button(text="Высокая сложность", callback_data="axis3_high")
    kb.button(text="⬅ Назад", callback_data="menu_learning")
    kb.adjust(1)
    return kb.as_markup()

@dp.callback_query(F.data == "axis3")
async def axis3(callback: CallbackQuery):
    await callback.message.edit_text(
        "Ось 3 — Когнитивная сложность.\nВыберите тип:",
        reply_markup=axis3_menu()
    )

@dp.callback_query(F.data == "axis3_low")
async def axis3_low(callback: CallbackQuery):
    await callback.message.edit_text(
        "Низкая сложность:\n"
        "• Предпочитает простоту\n"
        "• Один основной тезис\n\n"
        "В рекламе эффективно одно четкое обещание.",
        reply_markup=axis3_menu()
    )

@dp.callback_query(F.data == "axis3_high")
async def axis3_high(callback: CallbackQuery):
    await callback.message.edit_text(
        "Высокая сложность:\n"
        "• Учитывает несколько факторов\n"
        "• Анализирует условия\n\n"
        "В рекламе эффективна многоуровневая подача.",
        reply_markup=axis3_menu()
    )

# ======================
# ИГРЫ
# ======================

def games_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="Игра 1", callback_data="game1")
    kb.button(text="Игра 2", callback_data="game2")
    kb.button(text="Игра 3", callback_data="game3")
    kb.button(text="⬅ Назад", callback_data="back_main")
    kb.adjust(1)
    return kb.as_markup()

@dp.callback_query(F.data == "menu_games")
async def games(callback: CallbackQuery):
    await callback.message.edit_text(
        "Раздел игр.\nВыберите игру:",
        reply_markup=games_menu()
    )

# ===== Игра 1 =====

@dp.callback_query(F.data == "game1")
async def game1(callback: CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="Блогер + скидка", callback_data="game1_correct")
    kb.button(text="Разбор составов", callback_data="game1_wrong")
    kb.button(text="Таблица сравнения", callback_data="game1_wrong")
    kb.button(text="Философия индустрии", callback_data="game1_wrong")
    kb.button(text="⬅ Назад", callback_data="menu_games")
    kb.adjust(1)
    await callback.message.edit_text(
        "Игра 1.\nАудитория: поле-зависимая, импульсивная, низкая сложность.\n"
        "Выберите стратегию:",
        reply_markup=kb.as_markup()
    )

@dp.callback_query(F.data.startswith("game1_"))
async def game1_result(callback: CallbackQuery):
    user = get_user(callback.from_user.id)
    if not user["game1"]:
        if callback.data == "game1_correct":
            user["score"] += 3
        user["game1"] = True
        user["games_completed"] += 1

    await callback.message.edit_text(
        "Игра 1 завершена.\n"
        "Вы можете перейти к следующей игре.",
        reply_markup=games_menu()
    )

# ===== Игра 2 =====

@dp.callback_query(F.data == "game2")
async def game2(callback: CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="Поле-независимая / Рефлексивная / Высокая", callback_data="game2_correct")
    kb.button(text="Поле-зависимая / Импульсивная / Низкая", callback_data="game2_wrong")
    kb.button(text="⬅ Назад", callback_data="menu_games")
    kb.adjust(1)
    await callback.message.edit_text(
        "Игра 2.\nОписание: пользователи читают отзывы и сравнивают.\n"
        "Выберите параметры аудитории:",
        reply_markup=kb.as_markup()
    )

@dp.callback_query(F.data.startswith("game2_"))
async def game2_result(callback: CallbackQuery):
    user = get_user(callback.from_user.id)
    if not user["game2"]:
        if callback.data == "game2_correct":
            user["score"] += 3
        user["game2"] = True
        user["games_completed"] += 1

    await callback.message.edit_text(
        "Игра 2 завершена.\n"
        "Вы можете перейти к следующей игре.",
        reply_markup=games_menu()
    )

# ===== Игра 3 =====

@dp.callback_query(F.data == "game3")
async def game3(callback: CallbackQuery):
    kb = InlineKeyboardBuilder()
    kb.button(text="Вариант A", callback_data="game3_wrong")
    kb.button(text="Вариант B", callback_data="game3_correct")
    kb.button(text="⬅ Назад", callback_data="menu_games")
    kb.adjust(1)
    await callback.message.edit_text(
        "Игра 3.\nАудитория: поле-независимая, рефлексивная, высокая сложность.\n"
        "Выберите вариант рекламы:",
        reply_markup=kb.as_markup()
    )

@dp.callback_query(F.data.startswith("game3_"))
async def game3_result(callback: CallbackQuery):
    user = get_user(callback.from_user.id)
    if not user["game3"]:
        if callback.data == "game3_correct":
            user["score"] += 3
        user["game3"] = True
        user["games_completed"] += 1

    text = "Игра 3 завершена.\n"

    if user["games_completed"] == 3:
        text += "\nВы прошли все игры.\nПерейдите в раздел «Результат»."

    await callback.message.edit_text(
        text,
        reply_markup=games_menu()
    )

# ======================
# РЕЗУЛЬТАТ
# ======================

@dp.callback_query(F.data == "menu_result")
async def result(callback: CallbackQuery):
    user = get_user(callback.from_user.id)
    score = user["score"]

    if score >= 8:
        result_text = "Высокий уровень понимания когнитивных стилей."
    elif score >= 5:
        result_text = "Средний уровень понимания. Есть зоны для развития."
    else:
        result_text = "Рекомендуется повторить обучение."

    await callback.message.edit_text(
        f"Ваш результат: {score} из 9 баллов.\n\n{result_text}",
        reply_markup=main_menu()
    )

# ======================
# Назад
# ======================

@dp.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):
    await callback.message.edit_text(
        "Главное меню.",
        reply_markup=main_menu()
    )

# ======================
# Запуск
# ======================

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
