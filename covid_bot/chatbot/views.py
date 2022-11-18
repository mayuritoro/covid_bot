from fnmatch import translate
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from dateutil.parser import parse
from google.cloud import dialogflow_v2beta1 as dialogflow
from googletrans import Translator
from .models import Chatbot
import goslate
from google.protobuf.json_format import MessageToDict

def index(request):
    import os
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/excellarate/Downloads/testbot-tujk-5c804f9b8c01.json"
    message=[]
    lang_code_1 = ''
    

    if request.method == 'POST':
        input_1 = request.POST.get('input_1')
    
        message.append(input_1)
        translator = Translator()
        print(input_1,type(input_1))
        lang_code = translator.detect(str(input_1))
        lang_code_1 = (lang_code.lang)
        print(lang_code_1)
        # return lang_code_1
        
        #return language
    if not request.session.exists(request.session.session_key):
        request.session.create()
        print(request.session.session_key)
        default_trigger=['hello']
        reply=detect_intent_texts('testbot-tujk',request.session.session_key,default_trigger, 'en')
    #if request.session.exists(request.session.session_key):
    else:
        reply=detect_intent_texts('testbot-tujk',request.session.session_key, message, lang_code_1)

    if reply == ['']:
        reply = ['vaccines are not available']
    else:
        reply = reply
    #request.session.flush()
    return render (request,'home.html', {'reply':reply})

def detect_intent_texts(project_id, session_id, texts, language_code):

    from google.cloud import dialogflow_v2 as dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
    response_json = MessageToDict(response._pb)
    result = response_json['queryResult']
    
    text_1 = []

    for i in range(len(result['fulfillmentMessages'])):

        text_1.append(result['fulfillmentMessages'][i]['text']['text'][0])
        #print(text_1)

    return text_1
        


@csrf_exempt    
def webhook(request):
    req =json.loads(request.body)
    action=req.get('queryResult').get('action')
    num=req.get('queryResult').get('parameters')
    lang_code=req.get('queryResult').get('languageCode')
    output=req.get('session')
    pincode=(num.get('pin_code'))
    user_date=num.get('user_date')
    print(user_date)

    reply=''
    if action=='pincode':
        data=pin_code(request,pincode,user_date, lang_code)
        for i in range(len(data)):
            name=''.join(data[i][0])
            address=''.join(data[i][1])
            vaccine = ''.join(data[i][2])
            time_slot = ','.join(data[i][3])
            #seats = ''.join(data[i][4])
            message=f'hospital name: {name}, Address: {address} ,Vaccine Name: {vaccine},time: {time_slot},'# Availability: {seats},\n'
            reply+=str(message)
    if lang_code == 'hi':
        fulfillmentText={'fulfillmentText':hi_translator(request, reply)}
    else:
        fulfillmentText={'fulfillmentText':reply}
    return JsonResponse(fulfillmentText,safe=True)

def pin_code(request,pincode,user_date, lang_code):
    url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'
    # if user_date == '' or user_date == 'today':
    #     user_date = date.today().strftime('%d-%m-%Y')
    # else:
    # if lang_code == 'en':
    #     user_date = parse(user_date).strftime('%m-%d-%Y')
    # else:
    user_date = parse(user_date).strftime('%d-%m-%Y')
    print(user_date)
    params={'pincode':pincode,'date':user_date}
    json_data=requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={user_date}')
    api_response_json=json_data.json()
    data=[]
    for i in range(len(api_response_json['sessions'])):
        val = []
        val *= 0
        val.append(api_response_json['sessions'][i]['name'])
        val.append(api_response_json['sessions'][i]['address'])
        val.append(api_response_json['sessions'][i]['vaccine'])
        add = []
        add *= 0
        for j in range(len(api_response_json['sessions'][i]['slots'])):
            add.append(api_response_json['sessions'][i]['slots'][j]['time'])
        val.append(add)
        data.append(val)
        #print(data)
   
    return data

def translate(request,**kwargs):
    translator=Translator()
    result=[]
    for values in kwargs.values():
        output=translator.translate(values, dest='en')
        result.append(output.text)
    return result

def hi_translator(request, mystory):
    translator = Translator()
    output = translator.translate(mystory, dest='hi')
    return output.text

def gs_trans(request, mystory):
    gs = goslate.Goslate()
    output = gs.translate(mystory, 'hi')
    return output

def numconvert(requests, message):
    from englisttohindi.englisttohindi import EngtoHindi
    trans = EngtoHindi(message)
    return (trans.convert)
