 # Функционал связи с менеджером закрыт.


# from aiogram import Router, F, types
# from keyboards.inline.inline_second_level import get_inline_connection_manager
#
# router = Router()
#
#
# @router.callback_query(F.data == 'manager')
# async def get_inline_manager_kb(callback: types.CallbackQuery):
#     await callback.message.answer(text="👇👇Сделай выбор друже 👇👇", reply_markup=get_inline_connection_manager())
#
#
# @router.callback_query(F.data == 'connect2')
# async def inline_connect_manager_chat(callback: types.CallbackQuery):
#     await callback.message.answer(text=f'<a href="tg://user?id=1006569664">{callback.from_user.first_name} '
#                                        f'это ссылка в чат с менеджером🤓. Нажми.</a>')
#
#
# @router.callback_query(F.data == 'connect1')
# async def inline_connect_manager_phone(callback: types.CallbackQuery):
#     await callback.message.answer(text=f'Позвонить менеджеру\n'
#                                        f'☎ +375291803164')
