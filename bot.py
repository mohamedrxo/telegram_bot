#first we mast import the dependencies the telegram librarie
from telegram import Update
from telegram.ext import Application, ConversationHandler, MessageHandler, filters, ContextTypes, CommandHandler

token = "Your_API_Kye"
bot_name = "@yout_bot_name"

#we must define the CommandHandler for our bot
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am the best chatbot in the world')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I can help you manage your stock market portfolio')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')

# now the logic of the bot for example if the message contain the word hello then the responce should be "Hi there"

def handle_response(text: str) -> str:
    text = text.lower()
    if "hello" in text:
        return "Hi there"
    if "how are you" in text:
        return "I am good"
    if "how is the market today" in text:
        return "Hot"
    return "I don't understand you"

#this function help use identifie the if our bot in privite or group chat and meke the responce and get the is of the user

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f'User ID {update.message.chat.id} in {message_type}: {text}')
    if message_type == 'group':
        if bot_name in text:
            new_text = text.replace(bot_name, "").strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)
    
    print('BOT:', response)
    await update.message.reply_text(response)

#this function return the errors in case

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    print(f'Update {update} caused error {context.error}')

# and this how we run the code

if __name__ == "__main__":


    # we create the server and add the api token to it
    
    print('Starting Bot...')
    
    app = Application.builder().token(token).build()

    # Command handlers
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Message handler
    
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error handler
    
    app.add_error_handler(error)

    print("Polling...")
    
    #poll_interval define the time of the rendering
    
    app.run_polling(poll_interval=3)
