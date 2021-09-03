from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
TOKEN='1934365844:AAHYZ4eWj0zlcIWJb-VzCo-quzJWqx5AObE'
REQUEST_KWARGS={
    'proxy_url': 'socks5h://127.0.0.1:1080',
    # Optional, if you need authentication:
    # 'urllib3_proxy_kwargs': {
    #     'username': 'PROXY_USER',
    #     'password': 'PROXY_PASS',
    # }
}

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(TOKEN,request_kwargs=REQUEST_KWARGS)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()