from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
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

# Nút admin bấm mở chat
admin_button = InlineKeyboardMarkup([
    [InlineKeyboardButton("📞 Liên hệ Admin", url="https://t.me/dct_overlordx")]
])

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "👋 Chào mừng đến FLUORITE IOS 👾\n\nChọn chức năng bên dưới để được hỗ trợ:",
        reply_markup=reply_markup
    )

# xử lý tin nhắn thường
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text.lower()

    if "mô tả fluorite" in text:
        await update.message.reply_text(
            """📦 <b>FLUORITE iOS – BẢN TỐI ƯU CAO CẤP</b>


👀 <b>ESP Features:</b>
🔹 Line / Box / Health / Distance hiển thị đầy đủ
🔹 Quan sát đối thủ chính xác, rõ ràng

🎯 <b>Aim System:</b>
🔸 FOV linh hoạt
🔸 Silent Aim mượt mà, khó phát hiện

⚡️ <b>Hiệu năng & tối ưu:</b>
🚀 Tăng độ chính xác & phản hồi nhanh
🗺️ Hỗ trợ <b>Antiban toàn bộ map</b>


✨ <b>Tính năng bổ sung:</b>
🛡️ Ẩn màn hình khi sử dụng (tránh bị phát hiện)
📱 Tương thích mọi thiết bị iOS
⚙️ Hoạt động ổn định – tối ưu hiệu năng tối đa


🎁 <b>Quyền lợi khi sử dụng:</b>
🔑 Key mới 100% – bảo hành theo thời hạn
♻️ Bao reset trong thời gian sử dụng
🛠️ Hỗ trợ setup từ <b>A → Z</b>
💬 Support <b>1–1</b> xuyên suốt quá trình sử dụng


📲 <b>Liên hệ Admin:</b>
👉 @dct_overlordx
💬 Nhận key + file IPA + hỗ trợ cài đặt nhanh chóng


🔥 <i>Trải nghiệm mượt – ổn định – an toàn!</i>""",
            parse_mode="HTML",
            reply_markup=admin_button
        )

    elif "giá" in text:
        await update.message.reply_text(
            """🍎 <b>FLUORITE iPA – ANTIBAN | SAFE MAIN ACCOUNT</b>


💎 <b>Bảng giá thuê Key:</b>
🌟 <b>90K</b> / 1 ngày
🌟 <b>200K</b> / 7 ngày
🌟 <b>350K</b> / 31 ngày


🔓 <b>ACC CLONE LV5 (sẵn sàng sử dụng):</b>
🌟 <b>3K / 1 acc</b>


💳 <b>Thanh toán:</b>
🏦 Bank Việt Nam ✅ Nhanh – tiện – an toàn


🎯 <b>Ưu đãi & hỗ trợ:</b>
♻️ Thuê Key <b>bao reset</b> trong thời gian sử dụng
⚡ Hỗ trợ nhanh chóng – setup tận tình
💬 Tư vấn chọn gói phù hợp


📲 <b>Liên hệ Admin:</b>
👉 @dct_overlordx
🔥 Nhận Key + Acc + hỗ trợ đầy đủ từ A → Z


🚀 <i>Ổn định – an toàn – trải nghiệm mượt mà!</i>""",
            parse_mode="HTML",
            reply_markup=admin_button
        )

    elif "admin" in text:
        await update.message.reply_text(
            """📞 <b>LIÊN HỆ ADMIN</b>

💬 Hỗ trợ nhanh chóng – phản hồi tận tình
🛠️ Giải đáp mọi thắc mắc & hướng dẫn cài đặt
🔑 Cung cấp Key, file IPA & Acc Clone


👉 <b>Admin:</b> @dct_overlordx


⚡ <i>Inbox ngay để được hỗ trợ chi tiết từ A → Z!</i>""",
            parse_mode="HTML",
            reply_markup=admin_button
        )

    elif "hướng dẫn cài đặt" in text:
        await update.message.reply_text(
            """📥 <b>HƯỚNG DẪN CÀI ĐẶT IPA (iOS)</b>

🔧 <b>Phương pháp:</b> Cài IPA qua <b>ESign + Chứng chỉ unBan (1 năm)</b>


📌 <b>Bước 1:</b> Tải ứng dụng ESign
👉 https://khoindvn.io.vn/#app

📌 <b>Bước 2:</b> Mua & nhập chứng chỉ
💳 https://muacert.com


✅ <b>Sau khi hoàn thành 2 bước trên:</b>
🎬 Truy cập link sau để xem video hướng dẫn chi tiết cách:

• Ký file IPA  
• Cài đặt ứng dụng  
• Sử dụng ESign  

👉 Link video: (thêm link tại đây)


📞 <b>Hỗ trợ & nhận file IPA:</b>
💬 Liên hệ <b>Admin</b> để:

• Được hỗ trợ cài đặt nhanh chóng  
• Nhận file <b>IPA Fluorite</b> mới nhất  
• Giải đáp mọi thắc mắc  


✨ <i>Lưu ý: Làm đúng từng bước để tránh lỗi khi cài đặt nhé!</i>""",
            parse_mode="HTML",
            disable_web_page_preview=True,
            reply_markup=admin_button
        )

    else:
        await update.message.reply_text(
            "Chọn chức năng bên dưới 👇",
            reply_markup=reply_markup
        )

# chạy bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

app.run_polling()
