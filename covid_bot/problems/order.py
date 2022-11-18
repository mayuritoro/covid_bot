import sys


def double_one(text):
    string_2=text
    string_1=''
    if len(set(string_2))==1:
        return string_2
    else:
        for i in range(0,len(string_2)-1):
            if ord(string_2[i])<ord(string_2[i+1]):
                string_1+=string_2[i]
                string_1+=string_2[i]
            
            else:
                string_1+=string_2[i]
        string_1+=string_2[-1]
        return string_1

if len(sys.argv) > 1:
    input_file = open(sys.argv[1],'r')
else:
    input_file = open("/home/excellarate/django/covid_bot/problems/sample_ts1_input.txt","r")

num_test_strings = int(input_file.readline())

for case_itr in range(num_test_strings):
    text = input_file.readline().rstrip()
    doubleone = double_one(text)

    print(f"Case #{case_itr+1}: {doubleone}")

input_file.close()
# result=double_one('PEEL')
# print(result)
# result=double_one('AAAAAAAAAA')
# print(result)
# result=double_one('CODEJAMDAY')
# print(result)