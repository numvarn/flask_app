from flask import Flask, request
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    TextSendMessage, FlexSendMessage, BubbleContainer, ImageComponent, URIAction
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
    if intent == 'Intent5':
        flex_message = FlexSendMessage(
            alt_text='hello',
            contents=BubbleContainer(
                direction='ltr',
                hero=ImageComponent(
                    url='https://trc.taboola.com/manageronline-managercoth/log/3/click?pi=%2Fsport%2Fdetail%2F9620000010473&ri=6f76ff0a57751d8d7a47db3a5363a195&sd=v2_73cd1250c31656207d822a3245e98e5f_32ccc33b-c105-4c88-8956-67d39097e681-tuct8f2555c_1643696092_1643696092_CAwQvotDGO3or5_rLyABKAEw0gE4xN0NQKTeDUi669YDUP___________wFYAGAAaJmq7524vvbHfXAB&ui=32ccc33b-c105-4c88-8956-67d39097e681-tuct8f2555c&it=text&ii=-4964610247906537328&pt=text&li=rbox-t2v&sig=e533206c0f101aa9b4192417fd4c67c36e4047d86c1d&url=https%3A%2F%2Fmgronline.com%2Fsport%2Fdetail%2F9650000010492&vi=1643696092269&r=40&tvi2=-2&lti=deflated&ppb=CK8F&cpb=EhIyMDIyMDEzMS01LVJFTEVBU0UYwZAeIJz__________wEqGXNnLnRhYm9vbGFzeW5kaWNhdGlvbi5jb20yCHdhdGVyMzY0OIACQMTdDUik3g1QuuvWA1j___________8BYwj-__________8BEP7__________wEYAmRjCNcWENUfGCNkYwjc__________8BENz__________wEYJGRjCNIDEOAGGAhkYwiWFBCYHBgYZGMI9f__________ARD1__________8BGAtkYwj0FBCeHRgfZGMI0f__________ARDR__________8BGC9kcgwmBlTAb0ASCAAAAAB4AYABpm-IAe65nMQBkAEX',
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
                    action=URIAction(
                        uri='http://www.sanook.com', label='label')
                )
            )
        )

        text_message = TextSendMessage(
            text='สวัสดี {} \nทดสอบสำเร็จ'.format(disname))

        # line_bot_api.reply_message(reply_token, text_message)
        line_bot_api.reply_message(reply_token, [flex_message, text_message])


if __name__ == '__main__':
    app.run(debug=True)
