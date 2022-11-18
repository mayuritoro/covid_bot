def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
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
        print(response.query_result.fulfillment_text)
        i=0
        i+=1
        print(i)

    



# first_response=int(input('enter 1 for  english and 2 for hindi'))
# if first_response == 1:
#     lang_code='en'
#     print(lang_code)
# elif first_response == 2:
#     lang_code='hi'
# while True:
#     text=[]
#     query=input('Enter query:- ')
#     text.append(query)
# message=['vaccine available on 400055']
# detect_intent_texts('covid-bot-invk','5658497823',message,'en')
message=['06-05-2022']

detect_intent_texts('covid-bot-invk','5658497823',message,'en')
import string    
import random
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))    
print("The randomly generated string is : " + str(ran))