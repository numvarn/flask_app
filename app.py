from flask import Flask, request
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextSendMessage,
)


app = Flask(__name__)

line_bot_api = LineBotApi(
    'OfUecJfUK9JXszTysTV2DJmN3P9ckblUryfYIW+LUh/AWXt9KPL26U5cl1sPFcsCmAUd7d5uJfDvxqlDEGCuz8AncGqLozRrkCQBzxQ1nvaChSiqjo4ml37/Q8oUSNadaYVOmT14p8vlaHpEXm8mIwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('18faa98b8de47b520f83083dbc4ff534')


@app.route('/')
def home():
    return "Hello My First Flask Project, Phisan Sookkhee"


@app.route("/callback", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    # print(body)
    req = request.get_json(silent=True, force=True)
    intent = req["queryResult"]["intent"]["displayName"]
    text = req['originalDetectIntentRequest']['payload']['data']['message']['text']
    reply_token = req['originalDetectIntentRequest']['payload']['data']['replyToken']
    id = req['originalDetectIntentRequest']['payload']['data']['source']['userId']
    disname = line_bot_api.get_profile(id).display_name

    print('id = ' + id)
    print('name = ' + disname)
    print('text = ' + text)
    print('intent = ' + intent)
    print('reply_token = ' + reply_token)

    reply(intent, text, reply_token, id, disname)

    return 'OK'


def reply(intent, text, reply_token, id, disname):
    if intent == 'intent 5':
        text_message = TextSendMessage(text='ทดสอบสำเร็จ')
        line_bot_api.reply_message(reply_token, text_message)


if __name__ == '__main__':
    app.run(debug=True)
