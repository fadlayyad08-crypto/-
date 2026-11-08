import streamlit as st
import requests

# 1. إعدادات بوت التليجرام الخاص بك (ضع توكن بوتك والآي دي الخاص بك هنا)
TELEGRAM_BOT_TOKEN = "ضع_توكن_البوت_هنا"
ADMIN_CHAT_ID = "ضع_الآي_دي_الخاص_بك_هنا"

# 2. بيانات الدفع (يمكنك تعديلها لاحقاً أو تركها كما هي)
BINANCE_USDT_ADDRESS = "TXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # عنوان محفظة باينانس (USDT - BEP20)
JAWWAL_PAY_NUMBER = "059xxxxxxx"  # رقم جوال باي

def send_telegram_notification(text):
    if TELEGRAM_BOT_TOKEN != "ضع_توكن_البوت_هنا":
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": ADMIN_CHAT_ID,
            "text": text,
            "parse_mode": "Markdown"
        }
        try:
            requests.post(url, json=payload)
        except Exception as e:
            pass

# تصميم الصفحة للموبايل وإخفاء قائمة وشعار Streamlit وزر "إدارة التطبيق" نهائياً
st.set_page_config(page_title="سكريبتات التداول", page_icon="📈", layout="centered")

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none;}
    div[data-testid="stStatusWidget"] {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; direction: rtl;">
        <h2>أهلاً بكم في سكريبتات التداول</h2>
        <p style="color: #ff4b4b; font-weight: bold;">⚠️ نحن غير مسؤولين على اي مخاطرة في التداول، نحن نعطيكم اشتراكات تداول بسعر 150 دولار.</p>
        <hr>
        <p><b>تفاصيل الباقة:</b> اشتراك شهري (شهر واحد) بسعر <b>150 دولار</b>.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 📝 نموذج طلب الاشتراك الشهري")

with st.form("subscription_form"):
    username = st.text_input("اسم المستخدم المطلوب:")
    password = st.text_input("كلمة المرور:", type="password")
    
    payment_method = st.selectbox(
        "اختر طريقة الدفع:",
        ["باينانس (Binance)", "جوال باي (Jawwal Pay)"]
    )
    
    if payment_method == "باينانس (Binance)":
        st.info(f"💳 تحويل بقيمة **150$** إلى محفظة باينانس (USDT):\n`{BINANCE_USDT_ADDRESS}`")
    else:
        st.info(f"🟢 تحويل بقيمة **150$** إلى محفظة جوال باي:\n`{JAWWAL_PAY_NUMBER}`")
        
    payment_proof = st.text_input("أدخل رقم حركة الدفع أو تفاصيل الإيصال:")
    
    submitted = st.form_submit_button("🚀 إرسال طلب الاشتراك")
    
    if submitted:
        if not username or not password or not payment_proof:
            st.error("❌ يرجى تعبئة جميع الحقول المطلوبة ورقم حركة الدفع!")
        else:
            # إرسال الإشعار لتليجرامك مباشرة
            msg = (
                f"🚨 *طلب اشتراك جديد عبر الموقع!* 🚨\n\n"
                f"👤 اسم المستخدم: `{username}`\n"
                f"🔑 كلمة المرور: `{password}`\n"
                f"💳 طريقة الدفع: {payment_method}\n"
                f"📝 رقم الحركة / الإيصال: `{payment_proof}`"
            )
            send_telegram_notification(msg)
        import streamlit as st

st.markdown("""
<style>
    /* إخفاء القائمة الرئيسية والترويسة والفوتر */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* إخفاء زر إدارة التطبيق وأزرار النشر والعرض العائمة في الزاوية */
    .stAppDeployButton {display: none !important;}
    div[class*="viewerBadge"] {display: none !important;}
    div.viewerBadge_container__1QSob {display: none !important;}
</style>
""", unsafe_allow_html=True)

            st.success("✅ تم إرسال طلبك وإثبات الدفع بنجاح للإدارة! سيتم تفعيل اشتراكك الشهري قريباً.
