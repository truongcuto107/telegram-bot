from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TOKEN")

# Menu nút bấm
keyboard = [
    ["📦 Mô tả Fluorite", "💰 Giá"],
    ["📞 Admin", "📥 Hướng dẫn cài đặt"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "👋 Chào mừng đến FLUORITE IOS 👾\n\nChọn chức năng bên dưới để được hỗ trợ:",
        reply_markup=reply_markup
    )

# xử lý tin nhắn thường (keyword)
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.lower()

    if "mô tả fluorite" in text:
        await update.message.reply_text(
            """📦 **FLUORITE iOS – BẢN TỐI ƯU CAO CẤP**

---

👀 **ESP Features:**
🔹 Line / Box / Health / Distance hiển thị đầy đủ
🔹 Quan sát đối thủ chính xác, rõ ràng

🎯 **Aim System:**
🔸 FOV linh hoạt
🔸 Silent Aim mượt mà, khó phát hiện

⚡️ **Hiệu năng & tối ưu:**
🚀 Tăng độ chính xác & phản hồi nhanh
🗺️ Hỗ trợ **Antiban toàn bộ map**

---

✨ **Tính năng bổ sung:**
🛡️ Ẩn màn hình khi sử dụng (tránh bị phát hiện)
📱 Tương thích mọi thiết bị iOS
⚙️ Hoạt động ổn định – tối ưu hiệu năng tối đa

---

🎁 **Quyền lợi khi sử dụng:**
🔑 Key mới 100% – bảo hành theo thời hạn
♻️ Bao reset trong thời gian sử dụng
🛠️ Hỗ trợ setup từ **A → Z**
💬 Support **1–1** xuyên suốt quá trình sử dụng

---

📲 **Liên hệ Admin:**
👉 @dct_overlordx
💬 Nhận key + file IPA + hỗ trợ cài đặt nhanh chóng

---

🔥 *Trải nghiệm mượt – ổn định – an toàn!*""",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif "giá" in text:
        await update.message.reply_text(
            """🍎 **FLUORITE iPA – ANTIBAN | SAFE MAIN ACCOUNT**

---

💎 **Bảng giá thuê Key:**
🌟 **90K** / 1 ngày
🌟 **200K** / 7 ngày
🌟 **350K** / 31 ngày

---

🔓 **ACC CLONE LV5 (sẵn sàng sử dụng):**
🌟 **3K / 1 acc**

---

💳 **Thanh toán:**
🏦 Bank Việt Nam ✅ Nhanh – tiện – an toàn

---

🎯 **Ưu đãi & hỗ trợ:**
♻️ Thuê Key **bao reset** trong thời gian sử dụng
⚡ Hỗ trợ nhanh chóng – setup tận tình
💬 Tư vấn chọn gói phù hợp

---

📲 **Liên hệ Admin:**
👉 @dct_overlordx
🔥 Nhận Key + Acc + hỗ trợ đầy đủ từ A → Z

---

🚀 *Ổn định – an toàn – trải nghiệm mượt mà!*""",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif "admin" in text:
        await update.message.reply_text(
            """📞 **LIÊN HỆ ADMIN**

💬 Hỗ trợ nhanh chóng – phản hồi tận tình
🛠️ Giải đáp mọi thắc mắc & hướng dẫn cài đặt
🔑 Cung cấp Key, file IPA & Acc Clone

---

👉 **Admin:** @dct_overlordx

---

⚡ *Inbox ngay để được hỗ trợ chi tiết từ A → Z!*""",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif "hướng dẫn cài đặt" in text:
        await update.message.reply_text(
            """📥 **HƯỚNG DẪN CÀI ĐẶT IPA (iOS)**

🔧 **Phương pháp:** Cài IPA qua **ESign + Chứng chỉ unBan (1 năm)**

---

📌 **Bước 1: Tải ứng dụng ESign**
👉 Link download: https://khoindvn.io.vn/#app

📌 **Bước 2: Mua & nhập chứng chỉ**
💳 Link mua chứng chỉ + hướng dẫn nhập: https://muacert.com

---

✅ **Sau khi hoàn thành 2 bước trên:**
🎬 Truy cập link sau để xem video hướng dẫn chi tiết cách:

* Ký file IPA
* Cài đặt ứng dụng
* Sử dụng ESign

👉 Link video: *(thêm link tại đây)*

---

📞 **Hỗ trợ & nhận file IPA:**
💬 Liên hệ **Admin** để:

* Được hỗ trợ cài đặt nhanh chóng
* Nhận file **IPA Fluorite** mới nhất
* Giải đáp mọi thắc mắc trong quá trình sử dụng

---

✨ *Lưu ý:* Làm đúng từng bước để tránh lỗi khi cài đặt nhé!""",
            parse_mode="Markdown",
            disable_web_page_preview=True,
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text(
            "Chọn chức năng bên dưới 👇",
            reply_markup=reply_markup
        )

# chạy bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()