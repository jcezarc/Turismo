import os
from datetime import datetime
import requests

MAXIMO_DIAS = 5


class Clima:
    def __init__(self, cidade: str, periodo: datetime, **args):
        dias = (periodo - datetime.now()).days + 1
        if dias not in range(MAXIMO_DIAS+1):
            raise ValueError(f'Período deve ser entre hoje e {MAXIMO_DIAS} dias')
        url = self.url_weather(
            q=cidade,
            cnt=dias,
            appid=os.environ.get('WEATHER_API_KEY'),
            units='metric'
        )
        self.dados = []
        for resp in requests.get(url).json()['list']:
            chuva = resp["weather"][0]["main"] == "Rain"
            temperatura = resp["main"]["temp"]
            self.dados.append((chuva, temperatura))

    
    def url_weather(self, **args):
        return 'https://api.openweathermap.org/data/2.5/forecast?{}'.format(
            '&'.join(f'{k}={v}' for k, v in args.items())
        )
