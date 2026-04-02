from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv("TOKEN")

# Menu nút bấm
keyboard = [
    ["📦 Mô tả Fluorite", "💰 Giá"],
    ["📞 Admin", "📥 Hướng dẫn cài đặt"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Chào mừng đến FLUORITE IOS 👾\n\nChọn chức năng bên dưới để được hỗ trợ:",
        reply_markup=reply_markup
    )

# xử lý tin nhắn thường (keyword)
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "mô tả fluorite" in text:
        await update.message.reply_text(
            "📦 *FLUORITE iOS*\n\n" "👀 *ESP:* line / box / health / distance ...\n" 
  	    "🎯 *Aim System:* fov / silent aim\n" 
	"⚡ *Tối ưu:* độ chính xác & phản hồi\n" 
	"🗺️ *Hỗ trợ:* antiban all map\n\n" 
	"✨ *Tính năng bổ sung:*\n" 
	"🛡️ Ẩn màn hình khi sử dụng\n" 
	"📱 Tương thích toàn bộ thiết bị iOS\n" 
	"⚙️ Hoạt động ổn định, tối ưu hiệu năng\n\n" 
	"🎁 *Quyền lợi:*\n" 
	"🔑 Key mới 100%, bảo hành theo thời hạn, bao reset\n" 
	"🛠️ Hỗ trợ setup từ A → Z\n" 
	"💬 Support 1–1 trong quá trình sử dụng\n\n" 
	"📲 Admin: @dct\\_overlordx", parse_mode="Markdown"
        )

    elif "giá" in text:
        await update.message.reply_text(
            "🍎 *Fluorite .iPA Antiban Safe Main Account*\n"
            "🌟90K/1 DAY\n"
            "🌟200K/7 DAY\n"
            "🌟350K/31 DAY\n\n"
            "🔓 *Acc Clone Lv5*\n"
            "🌟3K/1 ACC\n\n"
            "🚩 *Payments:* Bank Việt ✅\n"
            "🔫 Thuê Key Bao Reset, Mua Acc Clone Liên Hệ Admin\n"
            parse_mode="Markdown"
        )

    elif "admin" in text:
        await update.message.reply_text("📞 Liên hệ admin: @dct_overlordx")

    elif "hướng dẫn cài đặt" in text:
        await update.message.reply_text(
            "📥 *Hướng dẫn cài đặt*\n\n"
            "Sau khi mua, admin sẽ hướng dẫn chi tiết từng bước từ A → Z.\n"
            "Đảm bảo cài đặt thành công và sử dụng ổn định.",
            parse_mode="Markdown"
        )

    else:
        await update.message.reply_text("Chọn chức năng bên dưới 👇", reply_markup=reply_markup)

# chạy bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, reply))

app.run_polling()