# # # import json

# # # data="""

# # # {"sessions":[{"center_id":562094,"name":"V N Desai Hospital 1","address":"V.N. DESAI GENERAL MUNICIPAL HOSPITAL  SANTACRUZ EAST","state_name":"Maharashtra","district_name":"Mumbai","block_name":"Ward H East Corporation - MH","pincode":400055,"from":"09:00:00","to":"15:00:00","lat":0,"long":0,"fee_type":"Free","session_id":"9daff918-9935-4f49-b1d1-d06ebd8107b1","date":"30-03-2022","available_capacity":44,"available_capacity_dose1":19,"available_capacity_dose2":6,"fee":"0","min_age_limit":15,"allow_all_age":true,"vaccine":"COVAXIN","slots":["09:00AM-10:00AM","10:00AM-11:00AM","11:00AM-12:00PM","12:00PM-03:00PM"]},{"center_id":562094,"name":"V N Desai Hospital 1","address":"V.N. DESAI GENERAL MUNICIPAL HOSPITAL  SANTACRUZ EAST","state_name":"Maharashtra","district_name":"Mumbai","block_name":"Ward H East Corporation - MH","pincode":400055,"from":"09:00:00","to":"15:00:00","lat":0,"long":0,"fee_type":"Free","session_id":"f3341a3d-b61a-4987-8df8-44a95f78b07a","date":"30-03-2022","available_capacity":48,"available_capacity_dose1":48,"available_capacity_dose2":0,"fee":"0","min_age_limit":12,"max_age_limit":44,"allow_all_age":false,"vaccine":"CORBEVAX","slots":["09:00AM-10:00AM","10:00AM-11:00AM","11:00AM-12:00PM","12:00PM-03:00PM"]},{"center_id":562094,"name":"V N Desai Hospital 1","address":"V.N. DESAI GENERAL MUNICIPAL HOSPITAL  SANTACRUZ EAST","state_name":"Maharashtra","district_name":"Mumbai","block_name":"Ward H East Corporation - MH","pincode":400055,"from":"09:00:00","to":"15:00:00","lat":0,"long":0,"fee_type":"Free","session_id":"b79fa965-a98f-4f06-89b8-3e208dfe87cc","date":"30-03-2022","available_capacity":43,"available_capacity_dose1":10,"available_capacity_dose2":8,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":["09:00AM-10:00AM","10:00AM-11:00AM","11:00AM-12:00PM","12:00PM-03:00PM"]}]}

# # # """

# # # var= json.loads(data)
# # # variable=var['sessions']
# # # for i in range(len(variable)):
# # #     print(var['sessions'][i]['name']['address'])
# # #     print(var['sessions'][i]['address'])

# # import requests
# # import json
# # url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'
# # pincode='416416'
# # date='01-04-2022'
# # params={'pincode':pincode,'date':date}
# # json_data=requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}')
# # json_data=json_data.json()
# # sessions=json_data['sessions']
# # # print(sessions)
# # data=[]
# # # print(len(sessions))
# # for i in range(len(sessions)):
# #     val=[]
# #     val*=0
# #     val.append([json_data['sessions'][i]['name']])
# #     val.append([json_data['sessions'][i]['vaccine']])
# #     val.append(json_data['sessions'][i]['slots'])
# #     data.append(val)
# # # print(data[1][1])    
# # # print(sessions)
# # # for i in range(len(sessions)):
# # #     print(json_data['sessions'][i]['name'])
# # #     print(json_data['sessions'][i]['vaccine'])
# # #     print(json_data['sessions'][i]['slots'])
# # # data=[]
# # # for i in range(len(sessions)):
# # #     val=[]
# # #     for j in range(len(sessions)):
# # #         val.append([json_data['sessions'][i]['name']])
# #         # val.append([json_data['sessions'][i]['vaccine']])
# #         # val.append(json_data['sessions'][i]['slots'])
# #     # data.append([val])
# # #     print(val)
# # #     # val*=0
# # # for i in range(len(data)):
# # #     print(data[i])
# # #     print()
# # # for i in range(len(data)-1):
# # #     message=f'hospital name:{data[0]}, vaccine:{data[1]}'
# # #     print(message)

# # reply=''
# # for i in range(len(data)):
# #             # dates=','.join(data[2])
# #             # message=f'hospital name:{data[0]}, vaccine:{data[1]},time:{dates}'
# #             # reply+=str(message)
# #             # for j in range(len(data[i])):
# #     name=','.join(data[i][0])
# #     vaccine=','.join(data[i][1])
# #     time_slot=','.join(data[i][2])
# #     message=f'hospital name: {name},vaccine: {vaccine}, time: {time_slot}\n'
# #     reply+=str(message)
# #     # print(message)
# # print(reply)



# # import requests

# # api_response='''{"sessions":[{"center_id":8679,
# # "name":"Sugar Factory UPHC No.2",
# # "address":"Near Vasantdada Sugar Factory Madhavnagar Road Sangli",
# # "state_name":"Maharashtra","district_name":"Sangli",
# # "block_name":"Miraj",
# # "pincode":416416,
# # "from":"09:00:00","to":"18:00:00",
# # "lat":16,"long":74,
# # "fee_type":"Free",
# # "session_id":"b03e1be9-71c5-4475-93bd-800788f913ca",
# # "date":"28-04-2022",
# # "available_capacity":299,
# # "available_capacity_dose1":100,
# # "available_capacity_dose2":100,
# # "fee":"0",
# # "min_age_limit":18,
# # "max_age_limit":44,
# # "allow_all_age":false,
# # "vaccine":"COVISHIELD",
# # "slots":[{"time":"09:00AM-11:00AM","seats":0},
# #         {"time":"11:00AM-01:00PM","seats":0},
# #         {"time":"01:00PM-03:00PM","seats":0},
# #         {"time":"03:00PM-06:00PM","seats":0}]},
# # {"center_id":655326,"name":"Diagnostic Centre Dawakhana","address":"Panchmukhi Maruti Road Khanbhag Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"e939bb86-beb6-40b3-9410-fd9b4644cfcb","date":"28-04-2022","available_capacity":300,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":11564,"name":"Hanumannagar UPHC COVAXIN","address":"Near D-Mart Mall 100 Ft. Road Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"33724d05-9a9e-42dc-b7b2-53001d4fe57b","date":"28-04-2022","available_capacity":296,"available_capacity_dose1":99,"available_capacity_dose2":97,"fee":"0","min_age_limit":15,"allow_all_age":true,"vaccine":"COVAXIN","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":687887,"name":"Wadar Colony Allo. Dawa.No.7","address":"Wadar Colony Ward No.10 Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"7b4a090f-4743-4937-92c5-0de43f754b7e","date":"28-04-2022","available_capacity":298,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":595376,"name":"Abhaynagar UPHC No.6","address":"State Bank Colony Abhaynagar Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"21865600-c1ca-496f-b1e1-b1dd8e4f2004","date":"28-04-2022","available_capacity":298,"available_capacity_dose1":100,"available_capacity_dose2":99,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":655326,"name":"Diagnostic Centre Dawakhana","address":"Panchmukhi Maruti Road Khanbhag Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"c3fb085f-0149-464a-8d4c-3f239074c56d","date":"28-04-2022","available_capacity":0,"available_capacity_dose1":0,"available_capacity_dose2":0,"fee":"0","min_age_limit":12,"max_age_limit":44,"allow_all_age":false,"vaccine":"CORBEVAX","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":8696,"name":"Shamraonagar UPHC No.3","address":"Near Gadi Karkhana Shamraonagar Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"c6598dee-da20-4e12-9a2e-277ed33e0e6e","date":"28-04-2022","available_capacity":300,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":11560,"name":"Hanumannagar UPHC No.4","address":"Near D-Mart Mall 100 Ft. Road Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"7739e430-1b70-438b-ac51-d7e85374bf0e","date":"28-04-2022","available_capacity":298,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":8707,"name":"Vishrambaug UPHC No.5","address":"Near Purva Garden Behind District Court Vijaynagar Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"84153d07-70b8-4924-8905-82a36e389cd4","date":"28-04-2022","available_capacity":300,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":8664,"name":"Jamwadi UPHC No.1","address":"Near Corporation School No. 25 Jamwadi Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"47d2a735-61c5-492a-b470-916e420a9341","date":"28-04-2022","available_capacity":299,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":8707,"name":"Vishrambaug UPHC No.5","address":"Near Purva Garden Behind District Court Vijaynagar Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"f52ea8d9-b4d5-458f-9169-c86f03137ba6","date":"28-04-2022","available_capacity":0,"available_capacity_dose1":0,"available_capacity_dose2":0,"fee":"0","min_age_limit":12,"max_age_limit":44,"allow_all_age":false,"vaccine":"CORBEVAX","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":563585,"name":"Sangli Civil Hosp. COVISHIELD","address":"Civil Hospital Chowk Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"8b8af7a4-9a2f-480a-8fb0-b5335e4b8ab5","date":"28-04-2022","available_capacity":200,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":692402,"name":"Police Dawakhana Covishield","address":"Police Head Quarters Vishrambaug Sangli","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"494df0f6-723f-4cbc-aca2-0835f3ae5a3e","date":"28-04-2022","available_capacity":300,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]},{"center_id":8671,"name":"Sangliwadi AllopathicDawakhana","address":"Gadgil Plot Ward No.13 Sangliwadi","state_name":"Maharashtra","district_name":"Sangli","block_name":"Miraj","pincode":416416,"from":"09:00:00","to":"18:00:00","lat":16,"long":74,"fee_type":"Free","session_id":"88296f38-e1a2-4b50-9414-9e6239cc0f38","date":"28-04-2022","available_capacity":300,"available_capacity_dose1":100,"available_capacity_dose2":100,"fee":"0","min_age_limit":18,"max_age_limit":44,"allow_all_age":false,"vaccine":"COVISHIELD","slots":[{"time":"09:00AM-11:00AM","seats":0},{"time":"11:00AM-01:00PM","seats":0},{"time":"01:00PM-03:00PM","seats":0},{"time":"03:00PM-06:00PM","seats":0}]}]}'''



# import requests
# # import json
# # url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'
# # pincode='416416'
# # date='29-04-2022'
# # params={'pincode':pincode,'date':date}
# # json_data=requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}')
# # api_response_json=json_data.json()



# # for i in range(len(api_response_json['sessions'])):
# #         print(api_response_json['sessions'][i]['name'])
# #         print(api_response_json['sessions'][i]['address'])
# #         print(api_response_json['sessions'][i]['vaccine'])
# #         for j in range(len(api_response_json['sessions'][i]['slots'])):
# #                 print(api_response_json['sessions'][i]['slots'][j]['time'])
# #                 print(api_response_json['sessions'][i]['slots'][j]['seats'])



# from datetime import date
# def pin_code(*args):
#     url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?'
#     pincode=int(args[0])
#     print(len(args))
#     if len(args)==1:
#         date1 = date.today().strftime("%d-%m-%Y")
#         print('------->',date1,type(date))
#     else:
#         date1=args[1]
#     print(date1)

#     params={'pincode':pincode,'date':date1}
#     json_response=requests.get(url=url,params=params)
#     api_response_data=json_response.json()
#     data=[]
#     for i in range(len(api_response_data['sessions'])):
#         val=[]
#         val*=0
#         val.append([api_response_data['sessions'][i]['name']])
#         val.append([api_response_data['sessions'][i]['address']])
#         val.append([api_response_data['sessions'][i]['vaccine']])
#         for j in range(len(api_response_data['sessions'][i]['slots'])):
#                 val.append(api_response_data['sessions'][i]['slots'][j]['time'])
#                 val.append(api_response_data['sessions'][i]['slots'][j]['seats'])
#         data.append(val)
#     print(data)
#     return data

# print(pin_code('400055','29-04-2022'))
# import datetime

# date='2022-04-05T12:00:00+05:30'
# format="%Y-%m-%dT%H:%M:%S%z"
# date_str=datetime.datetime.strptime(date,format)
# print(date_str.date())
from googletrans import Translator

def hi_translator(mystory):
    translator = Translator()
    output = translator.translate(mystory, dest='hi')
    return output.text

output=hi_translator('hospital name: Wadar Colony Allo. Dawa.No.7, Address: Wadar Colony Ward No.10 Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Diagnostic Centre Dawakhana, Address: Panchmukhi Maruti Road Khanbhag Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Sugar Factory UPHC No.2, Address: Near Vasantdada Sugar Factory Madhavnagar Road Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Hanumannagar UPHC No.4, Address: Near D-Mart Mall 100 Ft. Road Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Gaonbhag Allopathic Dawakhana, Address: Near Jain Basti Gaonbhag Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Sangli Civil Hosp. COVISHIELD, Address: Civil Hospital Chowk Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Sangliwadi AllopathicDawakhana, Address: Gadgil Plot Ward No.13 Sangliwadi ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Shree Tekke Eye Clinic, Address: 100 Feet Road Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Jamwadi UPHC No.1, Address: Near Corporation School No. 25 Jamwadi Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Vishrambaug UPHC No.5, Address: Near Purva Garden Behind District Court Vijaynagar Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Abhaynagar UPHC No.6, Address: State Bank Colony Abhaynagar Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Police Dawakhana Covishield, Address: Police Head Quarters Vishrambaug Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Abhaynagar UPHC COVAXIN, Address: State Bank Colony Abhaynagar Sangli ,Vaccine Name: COVAXIN,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Shamraonagar UPHC No.3, Address: Near Gadi Karkhana Shamraonagar Sangli ,Vaccine Name: COVISHIELD,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM,hospital name: Shamraonagar UPHC COVAXIN, Address: Near Gadi Karkhana Shamraonagar Sangli ,Vaccine Name: COVAXIN,time: 09:00AM-11:00AM,11:00AM-01:00PM,01:00PM-03:00PM,03:00PM-06:00PM')
print(output)