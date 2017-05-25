from flask import Flask, request
import telepot
import urllib3

# pythonanywhere stuff
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of pythonanywhere stuff

secret = "b6612fe7-5ea6-444d-a315-e3f21faa2b39"
# connecting to Telegram
bot = telepot.Bot('343392414:AAECRTAnbVpxr9__x-gdfCUpwwIf3pAcLJs')
bot.setWebhook("https://doktortm93.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["nessage"]["text"]
        chat_id = update["message"]["chat"]["id"]
        bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        return "OK"



