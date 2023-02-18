from aiogram import types
from loader import bot, dp, translator

from functions.reply_checker import check_for_reply as is_reply

@dp.message_handler(commands=['set_role'], commands_prefix='!', chat_type=["group", "supergroup"], is_chat_admin=True, custom_title=True)
async def set_someone(msg: types.Message):
    if not await is_reply(msg):
        return
    role = msg.get_args()
    member = await bot.get_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
    if member.status not in ["creator", "administrator"]:
        try:
            await bot.promote_chat_member(
                chat_id=msg.chat.id, 
                user_id=msg.reply_to_message.from_user.id, 
                can_manage_chat=True
            )
        except Exception as e:
            e = translator.translate(str(e))
            await msg.reply(f"Виникла помилка: <code>{e}</code>")
            return
    try:
        await bot.set_chat_administrator_custom_title(chat_id=msg.chat.id, user_id=msg.reply_to_message.from_user.id, custom_title=role)
    except Exception as e:
        e = translator.translate(str(e))
        await msg.reply(f"Виникла помилка: <code>{e}</code>")
        #logging.warning(f'| {msg.from_user.first_name} | {msg.from_user.language_code} | {msg.chat.type} | {e}')
        return
    await msg.answer(f'💬 Користувачу <code>{msg.reply_to_message.from_user.full_name.replace(">", "").replace("<", "")}</code> встановлено роль [{role}]')