from django.shortcuts import render
from datetime import datetime
from django.template.loader import get_template
from trips.models import contactdata
import pandas as pd 
import numpy as np

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, ImageSendMessage, \
    VideoSendMessage, LocationSendMessage, StickerSendMessage ,ButtonsTemplate,\
        TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

#HospitalDf = pd.read_csv('.\hospital20190131.csv',low_memory=False)

##from chatterbot import ChatBot
##from chatterbot.trainers import ChatterBotCorpusTrainer
#chatbot = ChatBot('jim')
# Create a new trainer for the chatbot
##trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")
# 載入中文的基本語言庫
#trainer.train("chatterbot.corpus.chinese")
#trainer.export_for_training('./my_export.json')

def index(request):
    template = get_template('indexform.html')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    views_time = '今天是：' + time
    html = template.render({'html_time':views_time})
    return HttpResponse(html)

@csrf_exempt
def linebot(request):
    #return HttpResponse()
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            #print(event)
            if (event.type == 'message'):
                if (event.message.type == 'text'):
                    user_id = event.source.user_id
                    #print("user_id =", user_id)
                    try:
                        profile = line_bot_api.get_profile(user_id)
                        #print(profile.display_name)
                        #print(profile.user_id)
                        #print(profile.picture_url)
                        #print(profile.status_message)
                    except LineBotApiError as e:
                        None
                        #print(e)
                    repleM=TextSendMessage(profile.display_name+' 抱歉我還沒有辦法回答這類問題，不過已經將您的問題記錄下來，待我詢問專業人員後，再回答您')
                    #text=chatbot.get_response(event.message.text)
                    #repleM=TextSendMessage(text.text)
                    #print(repleM)
                    if event.message.text == '中風資訊':
                        repleM=TextSendMessage('請幫我填問卷，然後告訴我機率好嗎，網址是 http://120.126.47.101/trips/')
                    if event.message.text == '中風機率':
                        repleM=TextSendMessage('是高危險群，請立即就醫，請告訴我您的居住地，縣市、鄉鎮或行政區，如北投區，將給您當地有相關醫療的資訊')
                    '''    
                    if event.message.text.find('區')>0:
                        try:
                            df1=HospitalDf[HospitalDf.縣市鄉鎮.str.find(event.message.text)>0]
                            df2=df1[df1.醫師>10]
                            hospitaltext = event.message.text+'供中風相關醫療的醫院，'
                            for i in range(len(df2)):
                                url2=' https://www.google.com/search?q='
                                hospitaltext = hospitaltext + url2 + df2.loc[i].機構名稱
                            repleM=TextSendMessage(hospitaltext)
                        except:
                            repleM=TextSendMessage('行政區有誤或無相關醫院')
                    '''        
                    if event.message.text == '榮總位置':
                        title = "台北榮民總醫院"
                        address = "112台北市北投區石牌路二段201號"
                        latitude = 25.120406
                        longitude = 121.520200
                        repleM=LocationSendMessage(title=title, address=address, latitude=latitude, longitude=longitude)
                    if event.message.text == '不舒服':
                        imagesurl='https://2.bp.blogspot.com/-uqJrnDMhKsE/WN2c06tCjUI/AAAAAAAALBA/g96hnygATOIH7RTRRzg4ByQQbJArxEmaQCLcB/s1600/%25E4%25B8%25AD%25E9%25A2%25A8%25E6%2587%25B6%25E4%25BA%25BA%25E5%258C%2585-04.png'
                        repleM=ImageSendMessage(original_content_url=imagesurl, preview_image_url=imagesurl)
                    if event.message.text == '選單':
                        button_template_message =ButtonsTemplate(
                            thumbnail_image_url="https://speciality.medicaldialogues.in/wp-content/uploads/2018/06/fatal-stroke-e1528349468632.jpg",
                            title='Menu', 
                            text='Please select',
                            ratio="1.51:1",
                            image_size="cover",
                            actions=[
#                                PostbackTemplateAction 點擊選項後，
#                                 除了文字會顯示在聊天室中，
#                                 還回傳data中的資料，可
#                                 此類透過 Postback event 處理。
                                PostbackTemplateAction(
                                    label='postback還會回傳data參數', 
                                    text='postback text',
                                    data='action=buy&itemid=1'
                                ),
                                MessageTemplateAction(
                                    label='message會回傳text文字', text='message text'
                                ),
                                URITemplateAction(
                                    label='uri可回傳網址', uri='http://www.xiaosean.website/'
                                )
                            ]
                        )
                        repleM=TemplateSendMessage(alt_text="Template Example", template=button_template_message)
                        if event.message.text == '問卷':
                            button_template_message =ButtonsTemplate(
                                thumbnail_image_url="https://speciality.medicaldialogues.in/wp-content/uploads/2018/06/fatal-stroke-e1528349468632.jpg",
                                title='Menu', 
                                text='Please select',
                                ratio="1.51:1",
                                image_size="cover",
                                actions=[
    #                                PostbackTemplateAction 點擊選項後，
    #                                 除了文字會顯示在聊天室中，
    #                                 還回傳data中的資料，可
    #                                 此類透過 Postback event 處理。
                                    PostbackTemplateAction(
                                        label='postback還會回傳data參數', 
                                        text='postback text',
                                        data='action=buy&itemid=1'
                                    ),
                                    MessageTemplateAction(
                                        label='message會回傳text文字', text='message text'
                                    ),
                                    URITemplateAction(
                                        label='uri可回傳網址', uri='http://www.xiaosean.website/'
                                    )
                                ]
                            )
                            repleM=TemplateSendMessage(alt_text="Template Example", template=button_template_message)
       
                    #傳U2影片網址
                    #replytext='https://youtu.be/iKUwMUjavP4replytext='
                            
                    if isinstance(event, MessageEvent):
                        line_bot_api.reply_message(
                            event.reply_token,
                            repleM
                        )

                if (event.message.type == 'sticker'):#image,video,audio,file,location                
                    import random
                    package_id = 1
                    sticker_id = random.randint(1,17)
                    line_bot_api.reply_message(
                        event.reply_token,
                        StickerSendMessage(package_id=package_id, sticker_id=sticker_id))
        return HttpResponse()
    else:
        return HttpResponseBadRequest()


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def news(request):
    return render(request, 'news.html')

def contact(request):
    datalist=[]
    if 'name' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contactdata.objects.create(name=name,
                            email=email,
                            subject=subject,
                            message=message,
                            created_at=datetime.now())
        datalist='data record'
    context = {'datalist': datalist,
                   }
    return render(request, 'contact.html', context)