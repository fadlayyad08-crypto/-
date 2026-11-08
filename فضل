import streamlit as st
from datetime import datetime, timedelta

# إعدادات صفحة الموقع
st.set_page_config(page_title="Fadhl Trading Bot - اشتراكات التداول", page_icon="📈", layout="centered")

# تصميم واجهة المستخدم
st.title("🚀 منصة اشتراكات بوت التداول الآلي")
st.write("أهلاً بك! احصل على إشارات وتوصيات التداول الحية المدعومة بالذكاء الاصطناعي وخوارزميات السكالبينج.")

st.markdown("---")

# قسم خطط الأسعار والاشتراكات
st.header("💎 خطط الاشتراكات المتاحة")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🔹 اشتراك VIP الشهري")
    st.markdown("""
    * **السعر:** **150$ دولار**
    * **المدة:** **شهر كامل (30 يوماً)**
    * توصيات فورية لزوج BTC/USDT والأزواج الرئيسية.
    * إدارة صارمة لمخاطر الصفقات (Stop Loss & Take Profit).
    * تحديثات مباشرة على مدار الساعة.
    """)

with col2:
    st.subheader("💳 وسائل الدفع المعتمدة")
    st.markdown("""
    لإتمام الاشتراك وتحويل مبلغ **150$**، يجوز الدفع عبر إحدى الطرق التالية:
    * **بينانس (Binance Pay / USDT):** `fadhl.crypto@binance`
    * **جوال باي (Jawwal Pay):** `059xxxxxxx`
    * **باي بال (PayPal):** التحويل المباشر
    """)

st.markdown("---")

# قسم طلب الاشتراك والدفع
st.header("📝 نموذج طلب الاشتراك والتفعيل")
with st.form("subscription_form"):
    subscriber_name = st.text_input("اسمك الكريم / معرف التليجرام:")
    payment_method = st.selectbox("اختر وسيلة الدفع المستخدمة:", ["Binance (USDT)", "جوال باي (Jawwal Pay)", "PayPal"])
    transaction_id = st.text_input("رقم عملية التحويل (Transaction ID / الإيصال):")
    
    submit_button = st.form_submit_button(label="إرسال طلب الاشتراك")
    
    if submit_button:
        if subscriber_name and transaction_id:
            # حساب تاريخ انتهاء الاشتراك بعد شهر (30 يوم)
            start_date = datetime.now()
            expiry_date = start_date + timedelta(days=30)
            
            st.success(f"تم استلام طلبك بنجاح يا {subscriber_name}!")
            st.info(f"📅 سيتم تفعيل حسابك لمدة شهر كامل ليصبح صالحاً لغاية: **{expiry_date.strftime('%Y-%m-%d')}** فور التحقق من عملية التحويل عبر {payment_method}.")
        else:
            st.warning("⚠️ الرجاء إدخال اسمك ورقم عملية التحويل لتأكيد الطلب.")

st.markdown("---")

# قسم لوحة تحكم المشتركين (لإدخال كود التفعيل ورؤية الإشارات)
st.header("📊 لوحة تحكم المشتركين (الإشارات الحية)")
access_code = st.text_input("أدخل كود التفعيل الخاص بك لعرض الصفقات الحية:", type="password")

if access_code:
    # كود تجريبي للتفعيل (يمكنك تغليفه أو ربطه بقاعدة بيانات لاحقاً)
    if access_code == "FADHL2026-VIP":
        st.success("🎉 أهلاً بك في القسم الخاص بالمشتركين النشطين!")
        st.metric(label="سعر السوق الحي (BTC/USDT)", value="68,450.00 $", delta="+1.8%")
        st.info("🟢 **الصفقة الحالية:** شراء (BUY) عند 68,100 | الهدف: 69,200 | الوقف: 67,600")
    else:
        st.error("❌ كود التفعيل غير صحيح أو منتهي الصلاحية. تأكد من الإدارة أو جدد اشتراكك بـ 150$.")
