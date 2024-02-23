# Функционал связи с менеджером закрыт


# from aiogram import F, Router, types, Bot
# from aiogram.filters import Command, StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import default_state, State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.types import CallbackQuery, Message
# from keyboards.inline.inline_connection_manager import markup_yes_no
# from db.database_sqlite3 import edit_profile_agree
#
# storage = MemoryStorage()
# router = Router()
#
#
# user_dict: dict[int, dict[str, str | int | bool]] = {}
#
#
# # Cоздаем класс, наследуемый от StatesGroup, для группы состояний нашей FSM
# class FSMFillForm(StatesGroup):
#     fill_name = State()  # Состояние ожидания ввода имени
#     fill_question = State()  # Состояние ожидания вопрса
#     fill_wish_news = State()  # Состояние ожидания выбора получать ли новости
#
#
# # Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# # кроме состояния по умолчанию, и отключать машину состояний
# @router.message(Command(commands='cancel'), ~StateFilter(default_state))
# async def process_cancel_command_state(message: Message, state: FSMContext):
#     await message.answer(
#         text='Вы вышли из машины состояний\n\n'
#              'Чтобы снова перейти к заполнению анкеты - '
#              'отправьте команду /connect3'
#     )
#     # Сбрасываем состояние и очищаем данные, полученные внутри состояний
#     await state.clear()
#
#
# @router.callback_query(F.data == 'connect3', StateFilter(default_state))
# async def inline_fillform_command(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.answer(text=f'Пожлауйста введите ваше имя')
#     await state.set_state(FSMFillForm.fill_name)
#
#
# # Этот хэндлер будет срабатывать, если введено корректное имя
# # и переводить в состояние ожидания ввода согласия на получение новостей
# @router.message(StateFilter(FSMFillForm.fill_name), F.text.isalpha())
# async def process_name_sent(message: Message, state: FSMContext):
#     # Cохраняем введенное имя в хранилище по ключу "name"
#     await state.update_data(name=message.text)
#     await message.answer(text='Отправьте удобный для вас способ связи и напишите что вас интересует.')
#     # Устанавливаем состояние ожидания ввода вопроса
#     await state.set_state(FSMFillForm.fill_question)
#
#
# @router.message(StateFilter(FSMFillForm.fill_name))
# async def warning_not_name(message: Message):
#     await message.answer(
#         text='То, что вы отправили не похоже на имя\n\n'
#              'Пожалуйста, введите ваше имя\n\n'
#              'Если вы хотите прервать заполнение анкеты - '
#              'отправьте команду /cancel'
#     )
#
#
# @router.message(StateFilter(FSMFillForm.fill_question))
# async def process_question_sent(message: Message, state: FSMContext):
#     # Cохраняем введнный запрос в хранилище по ключу "question_user"
#     await state.update_data(question_user=message.text)
#     await message.answer(text='Одобряете ли вы рассылку с интересными'
#                               ' предложениями от нас?', reply_markup=markup_yes_no)
#     # Устанавливаем состояние ожидания ввода вопроса
#     await state.set_state(FSMFillForm.fill_wish_news)
#
#
# # # Этот хэндлер будет срабатывать на выбор получать или
# # # не получать новости и выводить из машины состояний
# @router.callback_query(StateFilter(FSMFillForm.fill_wish_news),
#                        F.data.in_(['yes_news', 'no_news']))
# async def process_wish_news_press(callback: CallbackQuery, bot: Bot, state: FSMContext, CHAT_ID=None):
#     # Cохраняем данные о получении новостей по ключу "wish_news"
#     await state.update_data(wish_news=callback.data == 'yes_news')
#     # Добавляем в "базу данных" анкету пользователя
#     # по ключу id пользователя
#     user_dict[callback.from_user.id] = await state.get_data()
#     # Завершаем машину состояний
#     await state.clear()
#     # Отправляем в чат сообщение о выходе из машины состояний
#     await callback.message.edit_text(
#         text='Спасибо! Ваши данные сохранены!\n\n')
#
#     await callback.bot.send_message(1006569664, "Звязаться с будущим клиентом.")
#     await callback.bot.send_message(1006569664, user_dict[callback.from_user.id]["name"])
#     await callback.bot.send_message(1006569664, user_dict[callback.from_user.id]["question_user"])
#
#     await callback.message.answer(
#         text='Чтобы посмотреть данные вашей '
#              'анкеты - отправьте команду /showdata'
#     )
#
#
# @router.message(StateFilter(FSMFillForm.fill_wish_news))
# async def warning_not_wish_news(message: Message):
#     await message.answer(
#         text='Пожалуйста, воспользуйтесь кнопками!\n\n'
#              'Если же вы хотите прервать заполнение анкеты - '
#              'отправьте команду /cancel'
#     )
#
#
# # Этот хэндлер будет срабатывать на отправку команды /showdata
# # и отправлять в чат данные анкеты, либо сообщение об отсутствии данных
# @router.message(Command(commands='showdata'), StateFilter(default_state))
# async def process_showdata_command(message: Message):
#     # Отправляем пользователю анкету, если она есть в "базе данных"
#     if message.from_user.id in user_dict:
#         await message.answer(text=f'Имя: {user_dict[message.from_user.id]["name"]}\n'
#                                   f'Запрос: {user_dict[message.from_user.id]["question_user"]}\n'
#                                   f'Получать новости: {user_dict[message.from_user.id]["wish_news"]}'
#                              )
#     else:
#         # Если анкеты пользователя в базе нет - предлагаем заполнить
#         await message.answer(
#             text='Вы еще не заполняли анкету. Чтобы приступить - '
#                  'отправьте команду /connect3'
#         )
