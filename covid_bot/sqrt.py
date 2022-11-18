# import math
# squares=[1,4,9,16,25,36,49,64,81]
# dividend='69169'
# check=0
# quotient=''
# divisor=''
# remainder=''
# if len(dividend)%2!=0& check==0:
#     for i in range(len(squares)):
#         if int(dividend[0])>=squares[i]:
#             divisor=str(squares[i])    
#     quotient=str(int(int(divisor[0])**0.5//int(dividend[0])))
#     remainder=str(int(int(divisor[0])**0.5%int(dividend[0])))
#     print(quotient)
#     print(divisor)
#     pair=0
#     for i in range(1,int(len(dividend)),2):
#         pair=dividend[i]+dividend[i+1]
#         remainder=str(str(remainder)+str(pair))
#         print('divisor',divisor)
#         print('quotient',quotient)
#         print('remainder',remainder)
#         divisor=int(divisor)+int(quotient[-1])
#         divisor=str(divisor)+str(int(remainder[0]+remainder[1])//int(divisor))
#         break
        
# print('quotient',quotient)
# print('divisor',divisor)
# print('remainder',remainder)

# dividend='69169'
# dividend=dividend[::-1]
# for i in range(0,len(dividend),2):
#     print(dividend[i],dividend[i+1])

number='69169'
squares=[1,4,9,16,25,36,49,64,81]
perfect=0
dividends=[]
dividend=''
quotient=''
remainder=''
if len(number)%2:
    number='0'+number
for i in range(0,int(len(number)),2):
        pair=number[i]+number[i+1]
        dividends.append(pair)
#first perfect square
for i in range(len(squares)):
    if int(dividends[0])>=squares[i]:
        divisor=int(squares[i]**0.5)
        perfect=1

quotient=str(round(int(divisor)/int(dividends[0])*10))
remainder=int(divisor)%int(dividends[0])

for i in range(1,len(dividends)):
    remainder=str(remainder)+str(dividends[i])
    print(divisor,remainder)
    print('---------')
    # print(int(str(divisor)+str(quotient[-1])))/int(remainder)
    a=lambda a: 
    break
    




















