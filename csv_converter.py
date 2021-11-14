import requests

res = requests.get('https://www.hpb.health.gov.lk/api/get-current-statistical')
pcr_testing_data = res.json()['data']['daily_pcr_testing_data']

with open('pcr_testing_data.csv', 'w') as file:
    file.write('Date,PCR count'+'\n')
    for i in pcr_testing_data:
        file.write(i['date']+','+i['pcr_count']+'\n')
