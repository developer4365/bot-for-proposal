from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import config

import json

# Load messages from JSON file
try:
    with open('messages.json') as f:
        BUTTON_MESSAGES = json.load(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error loading messages.json: {e}")
    BUTTON_MESSAGES = {}

# Log group chat ID (replace this with your Telegram log group chat ID)
LOG_GROUP_CHAT_ID = -123456789  # Replace with your log group chat ID

async def log_activity(context: ContextTypes.DEFAULT_TYPE, log_message: str):
    """Send log messages to the log group"""
    try:
        await context.bot.send_message(chat_id=LOG_GROUP_CHAT_ID, text=log_message)
    except Exception as e:
        print(f"Failed to send log message: {e}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Log the start command
    user = update.effective_user
    log_message = f"User {user.first_name} (ID: {user.id}) started the bot."
    await log_activity(context, log_message)

    # Send the button menu
    keyboard = [
        [
            InlineKeyboardButton("Button 1 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 2 for my love Tejashvi", url="https://t.me/saket_tejashvi"),
            InlineKeyboardButton("Button 3 for my love Tejashvi", callback_data="button_3")
        ],
        [
            InlineKeyboardButton("Button 4 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 5 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 6 for my love Tejashvi", url="https://t.me/Legend_of_multiverse")
        ],
        [
            InlineKeyboardButton("Button 7 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 8 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 9 for my love Tejashvi", callback_data="button_9")  # Changed to callback
        ],
        [
            InlineKeyboardButton("Button 10 for my love Tejashvi", url="https://t.me/Legend_of_multiverse"),
            InlineKeyboardButton("Button 11 for my love Tejashvi", url="https://t.me/Legend_of_multiverse")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "💖 Welcome to this special proposal! 💖\n"
        "Please choose an option to discover a special message:",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    button_num = query.data  # Get the button callback data (e.g., "button_3", "button_9")

    # Special case for Button 3
    if button_num == "button_3":
        # Log the Button 3 click
        user = update.effective_user
        log_message = f"User {user.first_name} (ID: {user.id}) clicked Button 3: 'I love you Tejashvi Mishra my dear love'"
        await log_activity(context, log_message)

        # Send the custom message for Button 3
        await query.message.reply_text("I love you Tejashvi Mishra my dear love")
        return

    # Special case for Button 9
    if button_num == "button_9":
        # Log the Button 9 click
        user = update.effective_user
        log_message = f"User {user.first_name} (ID: {user.id}) clicked Button 9: 'Everything for you dear my Tejashvi, your Saket'"
        await log_activity(context, log_message)

        # Send the custom message for Button 9
        await query.message.reply_text("Everything for you dear my Tejashvi, your Saket")
        return

    # Handle other buttons (if using messages.json)
    message_data = BUTTON_MESSAGES.get(button_num, {"text": "No message set", "file": None})
    
    if message_data["file"]:
        try:
            with open(message_data["file"], 'rb') as file:
                await query.message.reply_document(
                    document=file,
                    caption=message_data["text"]
                )
        except FileNotFoundError:
            await query.message.reply_text("File not found!")
    else:
        await query.message.reply_text(message_data["text"])

def main():
    application = Application.builder().token(config.TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_click))
    
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
