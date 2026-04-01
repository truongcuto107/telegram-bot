from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("TOKEN")

# Menu nút bấm
keyboard = [
    ["📦 Menu", "💰 Giá"],
    ["📞 Admin", "📥 Hướng dẫn"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Chào mừng đến FLUORITE iOS 👾\n\nChọn chức năng bên dưới: ",
        reply_markup=reply_markup
    )

# xử lý tin nhắn thường (keyword)
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "menu" in text:
        await update.message.reply_text(
            "📦 *FLUORITE iOS*\n\n"
            "👀 *ESP:* Line / Box / Health / Distance ...\n"
            "🎯 *Aim System:* FOV / Silent Aim\n"
            "⚡ *Tối ưu:* độ chính xác & phản hồi\n"
            "🗺️ *Hỗ trợ:* antiban all map\n\n"
            "✨ *Tính năng bổ sung:*\n"
            "🛡️ Ẩn màn hình khi sử dụng\n"
            "📱 Tương thích toàn bộ thiết bị iOS\n"
            "⚙️ Hoạt động ổn định, tối ưu hiệu năng\n\n"
            "🎁 *Quyền lợi:*\n"
            "🔑 Key mới 100%, bảo hành theo thời hạn\n"
            "🛠️ Hỗ trợ setup từ A → Z\n"
            "💬 Support 1–1 trong quá trình sử dụng\n\n"
            "📲 Admin: @dct\\_overlordx404",
            parse_mode="Markdown"

        )

    elif "giá" in text:
        await update.message.reply_text("💰 Inbox admin để nhận bảng giá mới nhất\n📲 @dct_overlordx")

    elif "admin" in text:
        await update.message.reply_text("📞 Liên hệ admin: @dct_overlordx")

    elif "hướng dẫn" in text:
        await update.message.reply_text("📥 Sau khi mua sẽ được hướng dẫn chi tiết A–Z bởi admin")

    else:
        await update.message.reply_text("Chọn chức năng bên dưới 👇", reply_markup=reply_markup)

# chạy bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()