import requests as rq
import json


url = 'https://api.thevirustracker.com/free-api?countryTimeline=IT'

answer = rq.get(url)

data = json.loads(answer.text)

new_daily_cases = 0
new_daily_deaths = 0
total_cases = 0
total_recoveries = 0
total_deaths = 0

custom_total_cases = 0
custom_total_recoveries = 0
custom_total_deaths = 0

for date in data['timelineitems'][0]:
    key = date
    info = data['timelineitems'][0][key]
    if key != 'stat': #and key[0] < '4':
        new_daily_cases += info['new_daily_cases']
        new_daily_deaths += info['new_daily_deaths']
        total_cases = info['total_cases']
        total_recoveries += info['total_recoveries']
        total_deaths = info['total_deaths']

        custom_total_cases += new_daily_cases
        custom_total_deaths += new_daily_deaths
        custom_total_recoveries = total_recoveries
        print('__________________________________________________________________________________')
        print(date, info)
        print('Официально зараженные:', total_cases, 'Зараженные по подсчетам:', custom_total_cases - total_recoveries - total_deaths)
        print('Официальная смертность:', total_deaths, 'Подсчитанная смертность:', custom_total_deaths)
        print('Подсчитанные выздоровевшие:', custom_total_recoveries)
