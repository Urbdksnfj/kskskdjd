import telebot
from telebot.types import *
from database_main import *
from functions_to_my_bots import *
from telebot.handler_backends import ContinueHandling


def Ckick_Mute_Ban(message: Message):
    chat_id = message.chat.id
    user_ = message.from_user
    msg_text = message.text
    if (
        msg_text in ["طرد"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = ban_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            bot.ban_chat_member(chat_id, IDD.id)
            Vandals.add_user(chat_id, IDD.id, is_banned=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["كتم"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = mute_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_muted=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["حظر"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = block_function_van(message, My_id)
        if "True" in FD2V:
            bot.get_chat_member(chat_id, IDD.id)
            bot.restrict_chat_member(
                chat_id,
                IDD.id,
                until_date=None,
                can_send_messages=False,
                can_send_media_messages=False,
                can_send_other_messages=False,
                can_add_web_page_previews=False,
            )

            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_blocked=True)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["الغاء الكتم"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = unmute_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_muted=False)
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["الغاء الحظر"]
        and Compulsory_subscription(message)
        and message.reply_to_message
        and check_group(chat_id)
    ):
        IDD = message.reply_to_message.from_user
        FD2V = unblock_function_van(message, My_id)
        if "True" in FD2V:
            bot.send_message(chat_id, FD2V[1], reply_to_message_id=message.id)
            Vandals.add_user(chat_id, IDD.id, is_blocked=False)
            bot.restrict_chat_member(
                chat_id,
                IDD.id,
                until_date=None,
                can_send_messages=True,
                can_send_media_messages=True,
                can_send_other_messages=True,
                can_add_web_page_previews=True,
            )
        else:
            bot.send_message(chat_id, FD2V, reply_to_message_id=message.id)

    if (
        msg_text in ["مسح المكتومين"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            bot.send_message(
                chat_id, "تم مسح جميع المكتومين", reply_to_message_id=message.id
            )
            Vandals.delete_users(chat_id, is_muted=True)

        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

    if (
        msg_text in ["مسح المحظورين"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            bot.send_message(
                chat_id, "تم مسح جميع المحظورين", reply_to_message_id=message.id
            )
            uss = Vandals.delete_users(chat_id, is_blocked=True)
            for user_id in uss:
                try:
                    bot.restrict_chat_member(
                        chat_id,
                        user_id,
                        until_date=None,
                        can_send_messages=True,
                        can_send_media_messages=True,
                        can_send_other_messages=True,
                        can_add_web_page_previews=True,
                    )
                except:
                    pass
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )
    if (
        msg_text in ["مسح المطرودين"]
        and Compulsory_subscription(message)
        and check_group(chat_id)
    ):
        if Get_rank_user(chat_id, user_.id) not in [
            "member",
            "distinct",
            "blocked",
            "muted",
            "banned",
        ]:
            bot.send_message(
                chat_id, "تم مسح جميع المطرودين", reply_to_message_id=message.id
            )
            uss = Vandals.delete_users(chat_id, is_blocked=True)
            for user_id in uss:
                try:
                    bot.unban_chat_member(chat_id, user_id, only_if_banned=True)
                except:
                    pass
        else:
            bot.send_message(
                chat_id, "هذا الامر مخصص للمدراء فقط", reply_to_message_id=message.id
            )

muted_users = []
@app.on_message(filters.command(["كتم"], ""), group=39)
async def mute_user(client, message):
    global muted_users    
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:    
        if message.reply_to_message.from_user.id == 6909581339:
            await app.send_message(message.chat.id, "عذرا لا يمكنك كتم المطور فيجا")
        else: 
         if message.reply_to_message:
           user_id = message.reply_to_message.from_user.mention
         if user_id not in muted_users:
            muted_users.append(user_id)
            await message.reply_text(f" {user_id}\nكتمته\n༄")
         else:
           await message.reply_text(f"{user_id}\nمكتوم  من قبل\n༄")
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")


@app.on_message(filters.command(["الغاء الكتم"], ""), group=62)
async def unmute_user(client, message):
   global muted_users
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339: 
    user_id = message.reply_to_message.from_user.mention
    if user_id in muted_users:
        muted_users.remove(user_id)
        await message.reply_text(f" {user_id}\nابشر الغيت كتمه\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")    
       
        
        
       
@app.on_message(filters.text)
async def handle_message(client, message):
    if message.from_user and message.from_user.id in muted_users:
        await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)

@app.on_message(filters.command(["المكتومين"], ""), group=137)
async def get_rmuted_users(client, message):
    global muted_users
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
         count = len(muted_users)
         user_ids = [str(user) for user in muted_users]
         response = f" <u>قائمة المكتومين وعددهم :</u> {count}\n"
         response += "⭓━⭓⭓⭓⭓━⭓\n"
         response += "\n".join(user_ids)
         await message.reply_text(response)
    else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")



@app.on_message(filters.command(["مسح المكتومين"], ""), group=136)
async def unmute_all(client, message):
   usr = await client.get_chat(message.from_user.id)
   name = usr.first_name
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] or message.from_user.id == 6909581339:
    global muted_users
    count = len(muted_users)
    chat_id = message.chat.id
    failed_count = 0

    for member in muted_users.copy():
        user_id = member
        try:
            muted_users.remove(member)
        except Exception:
            failed_count += 1

    successful_count = count - failed_count

    if successful_count > 0:
        await message.reply_text(f"مسحت {successful_count} من المكتومين\n༄")
    else:
        await message.reply_text("↢ لا يوجد مستخدمين مكتومين ليتم مسحهم\n༄")

    if failed_count > 0:
        await message.reply_text(f"↢ فشل في مسح {failed_count}\nمن المكتومين\n༄")
   else:
        await message.reply_text(f"حجي هذا الامر ليس لك \n༄")
