import telebot
from telebot import types

# 1. ضع هنا توكن البوت الخاص بك (تحصل عليه من @BotFather)
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# 2. ضع هنا رقم الآي دي (Admin Chat ID) الخاص بجوالك لكي تصلك الطلبات وحدك
ADMIN_CHAT_ID = 123456789  # استبدل هذا الرقم برقم الآي دي الخاص بك

bot = telebot.TeleBot(TOKEN)

# تخزين مؤقت لبيانات المستخدمين أثناء التسجيل
user_data = {}

# النص الترحيبي وإخلاء المسؤولية المطلوب
WELCOME_TEXT = (
    " أهلاً بكم في سكريبتات التداول.\n\n"
    "⚠️ **نحن غير مسؤولين على اي مخاطرة في التداول، نحن نعطيكم اشتراكات تداول بسعر 150 دولار.**\n\n"
    "📋 **تفاصيل الاشتراك:**\n"
    "• نوع الباقة: اشتراك شهري\n"
    "• السعر: 150 دولار\n"
    "• المدة: شهر واحد"
)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("🚀 اشترك الآن (150$ - شهر)", callback_data="start_sub")
    markup.add(btn)
    
    bot.send_message(chat_id, WELCOME_TEXT, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "start_sub")
def ask_username(call):
    chat_id = call.message.chat.id
    bot.answer_callback_query(call.id)
    bot.send_message(chat_id, "الخطوة (1/4): يرجى إدخال **اسم المستخدم** الذي تريده:")
    bot.register_next_step_handler(call.message, get_username)

def get_username(message):
    chat_id = message.chat.id
    user_data[chat_id]['username'] = message.text
    bot.send_message(chat_id, "الخطوة (2/4): يرجى إدخال **كلمة المرور** الخاصة بحسابك:")
    bot.register_next_step_handler(message, get_password)

def get_password(message):
    chat_id = message.chat.id
    user_data[chat_id]['password'] = message.text
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🟡 باينانس (Binance)", callback_data="pay_binance"))
    markup.add(types.InlineKeyboardButton("🟢 جوال باي (Jawwal Pay)", callback_data="pay_jawwal"))
    
    bot.send_message(chat_id, "الخطوة (3/4): اختر **طريقة الدفع** المفضلة لديك:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("pay_"))
def choose_payment(call):
    chat_id = call.message.chat.id
    bot.answer_callback_query(call.id)
    
    if call.data == "pay_binance":
        method = "باينانس (Binance)"
        details = "عنوان محفظة باينانس (USDT):\n`ضع_عنوان_محفظتك_هنا`"
    else:
        method = "جوال باي (Jawwal Pay)"
        details = "رقم محفظة جوال باي:\n`0590000000`"
        
    user_data[chat_id]['payment_method'] = method
    
    bot.send_message(
        chat_id, 
        f"لقد اخترت الدفع عبر **{method}**.\n\n"
        f"قم بالتحويل بقيمة **150 دولار** إلى الحساب التالي:\n{details}\n\n"
        f"الخطوة (4/4): بعد إتمام التحويل، يرجى إرسال **صورة إيصال الدفع** أو **رقم حركة الدفع** هنا مباشرة:", 
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(call.message, get_proof)

def get_proof(message):
    chat_id = message.chat.id
    data = user_data.get(chat_id, {})
    
    username = data.get('username', 'غير معروف')
    password = data.get('password', 'غير معروف')
    method = data.get('payment_method', 'غير معروف')
    
    # رسالة التنبيه التي ستصلك أنت (المدير) على جوالك
    admin_text = (
        f"🚨 **طلب اشتراك جديد بانتظار التأكيد!** 🚨\n\n"
        f"👤 اسم المستخدم: `{username}`\n"
        f"🔑 كلمة المرور: `{password}`\n"
        f"💳 طريقة الدفع: {method}\n"
        f"💬 معرف التيليجرام (Chat ID): `{chat_id}`\n"
    )
    
    # إرسال الطلب وإثبات الدفع إليك مباشرة
    if message.photo:
        photo_file_id = message.photo[-1].file_id
        bot.send_photo(ADMIN_CHAT_ID, photo_file_id, caption=admin_text + "\n📎 مرفق صورة الإيصال بالأعلى", parse_mode="Markdown")
    else:
        proof_text = message.text
        admin_text += f"📝 رقم الحركة/الإيصال: `{proof_text}`"
        bot.send_message(ADMIN_CHAT_ID, admin_text, parse_mode="Markdown")
        
    # الرد على الزبون
    bot.send_message(
        chat_id, 
        "✅ **تم إرسال طلبك وإثبات الدفع بنجاح!**\n\n"
        "جاري مراجعة العملية من قِبل الإدارة، وسيتم إرسال **كود التفعيل الشهري** إليك فور تأكيد التحويل."
    )

if __name__ == '__main__':
    print("Bot is running successfully...")
    bot.infinity_polling()
