import os
from datetime import datetime, timedelta
from util.viagem import grava_viagem
from clima import api, historico


MY_PONY = {
    'provider': 'mysql',
    'user': 'root',
    'passwd': os.environ.get('MYSQL_PASSWORD'),
    'db': 'turismo',
}
DESTINO = 'Rio de Janeiro'


"""
Faz uma viagem HOJE para o Rio de Janeiro usando a API
Depois faz a mesma viagem daqui a 15 dias, usando o Histórico
"""
print('='*20, '\n', 'Consultando API...'.center(30), '\n', '='*20)
m1 = grava_viagem(
    cidade=DESTINO,
    periodo=datetime.now(),
    conexao=MY_PONY,
    Clima=api.Clima
)
print('='*20, '\n', 'Acessando Histórico...'.center(30), '\n', '='*20)
m2 = grava_viagem(
    cidade=DESTINO,
    periodo=datetime.now() + timedelta(days=15),
    conexao=MY_PONY,
    Clima=historico.Clima
)
print('-'*70)
print('Malas para cada viagem:')
print('\t', m1, '\n', '\t', m2)
