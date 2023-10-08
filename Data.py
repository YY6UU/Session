from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [
        InlineKeyboardButton("بـدء استـخراج الجلسـة 🖥️", callback_data="generate")
    ]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="رجـوع 🔙", callback_data="home")],
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "𝗞𝗮𝗶𝗱𝗼 - سـورس كايـدو 🌐", url="https://t.me/kaido_q"
            )
        ],
        [
            InlineKeyboardButton("كيفيـة الاستـخدام   ⍰ ", callback_data="help"),
            InlineKeyboardButton("حـول البـوت ℹ️", callback_data="about"),
        ],
        [InlineKeyboardButton("المطـور 👷", url="https://t.me/HAIDAR_MY")],
    ]

    START = """
**⎆ مـرحبـًا** {}
**⎆ اضغـط عـلى بـدء استخـراج الجلسـة لبـدء الاستـخراج**
**⎆ أنـا بوت استـخراج كـود تيرمكـس وبايروجـرام لـ تنصيـب @kaido_q**
**⎆ هـذا الكـود خـطير جدًا لا تشاركـه لأحد .**
    """

    HELP = """
**أوامـر البـوت ⎙**
━━━━━━━━━━━━━━━━━
/about - لحول البوت ℹ️
/help - لمساعدتك ❓
/start - لبدء البوت ❗
/repo - لعرض معلومـات عـن السـورس 💡
/generate - لاستخراج الجلسات 👷
/cancel - لإلغاء الاستخراج 🥀
/restart - لترسيت البـوت ♻️
"""

    # About Message
    ABOUT = """
**حـول البـوت ⍰**

**هـذا البوت تـم تشـغيله بواسطـة 𝗞𝗮𝗶𝗱𝗼 و المـطور @HAIDAR_MY**

قنـاة السـورس 🖥️ : [𝗦𝗼𝘂𝗿𝗰𝗲 𝗞𝗮𝗶𝗱𝗼](https://t.me/kaido_q)
لغـة البرمجـة ℹ️ : [بـايروجرام](docs.pyrogram.org)
اللغـة 🌐 : [بايثون](www.python.org)
المـطور 👷 : @HAIDAR_MY
    """

    # Repo Message
    REPO = """
━━━━━━━━━━━━━━━━━━━━━━━━
**سـورس كايـدو - 𝗞𝗮𝗶𝗱𝗼 **
**لا تنسـى الصـلاة على النبي 🤍 .**
┏━━━━━━━━━━━━━━━━━┓
⎆ سـورس كايـدو - 𝗞𝗮𝗶𝗱𝗼 . [اضـغط هـنا ❗](https://t.me/kaido_q)
⎆ المطـور : [اضـغط هـنا ❗](https://t.me/HAIDAR_MY)
⎆ شـروحـات السـورس ℹ️ [اضـغط هـنا ❗](https://t.me/kaido_q)
┗━━━━━━━━━━━━━━━━━┛ 
**تابـع لـ - 𝗞𝗮𝗶𝗱𝗼 🌐**
   """
