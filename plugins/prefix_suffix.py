from pyrogram import Client, filters, enums
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_caption(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**Ooh~ A new prefix? I love that!**\n\n__Whisper it to me like this:__\n`/set_prefix @Suh0_Kang`\n\nC’mon, don’t keep me waiting~")
    prefix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~")
    await jishubotz.set_prefix(message.from_user.id, prefix)
    await JishuDeveloper.edit("**Mmm~ Prefix saved nice and tight, just how I like it~ ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):

    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~)
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if not prefix:
        return await JishuDeveloper.edit("**Oopsie~ Looks like you haven’t set a prefix yet, darling! ❌**")
    await jishubotz.set_prefix(message.from_user.id, None)
    await JishuDeveloper.edit("**All gone! Your prefix has been tossed into the trash 🗑️✨**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_caption(client, message):

    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~")
    prefix = await jishubotz.get_prefix(message.from_user.id)
    if prefix:
        await JishuDeveloper.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await JishuDeveloper.edit("**Oopsie daisy! You don’t have any prefix set yet ❌ Come on, give me something cute to add!**")


# SUFFIX
@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_csuffix(client, message):

    if len(message.command) == 1:
        return await message.reply_text("**Hey cutie~ Give me a suffix to spice things up!**\n\nExample: `/set_suffix @Suh0_Kang`")
    suffix = message.text.split(" ", 1)[1]
    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~")
    await jishubotz.set_suffix(message.from_user.id, suffix)
    await JishuDeveloper.edit("**Ooh la la~ Your suffix is saved, darling! ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):

    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if not suffix:
        return await JishuDeveloper.edit("**Hey cutie! Looks like you don’t have any suffix set yet! ❌**")
    await jishubotz.set_suffix(message.from_user.id, None)
    await JishuDeveloper.edit("**Your suffix just got *charmingly* erased! All yours again! ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_csuffix(client, message):

    JishuDeveloper = await message.reply_text("⏳ Hold on, sweetheart... I’m getting things ready for you~")
    suffix = await jishubotz.get_suffix(message.from_user.id)
    if suffix:
        await JishuDeveloper.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await JishuDeveloper.edit("**Hey you, no suffix found here yet! Wanna add one? ❌**")
