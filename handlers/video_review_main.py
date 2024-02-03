from aiogram import Router, F, types
from keyboards.inline.inline_main_second_menu import create_inline_kb_reviews

router = Router()


@router.callback_query(F.data == 'reviews')
async def get_review_menu(callback: types.CallbackQuery):
    keyboard = create_inline_kb_reviews(2, 'review_bilding', 'review_cars', 'review_electronics', 'review_food',
                                        'btn_main_menu_1')
    await callback.message.answer(
        text='В данном блоке находятся обзоры, разделенные по тематике.',
        reply_markup=keyboard
    )
    await callback.message.delete()
