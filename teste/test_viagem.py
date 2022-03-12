import os
os.chdir('c:/users/julio/turismo')
import sys
sys.path.append('.')
sys.path.append('..')
from datetime import datetime, timedelta
from util.viagem import grava_viagem
from db.models import DB_PATH
from clima import simulador


CONEXAO_LOCAL = {
    'provider': 'sqlite',
    'filename': f'{DB_PATH}turismo.db',
    'create_db': True
}

def test_roupas_para_frio():
    mala = grava_viagem(
        cidade='Nárnia',
        periodo=datetime.now() + timedelta(days=8),
        conexao=CONEXAO_LOCAL,
        Clima=simulador.Clima
    )
    esperado = set([
        'capa grossa',
        'casaco de nylon',
        'bota couro sintético',
        'calça jeans']
    )
    assert mala == esperado


def test_roupas_para_calor():
    mala = grava_viagem(
        cidade='Mordor',
        periodo=datetime.now() + timedelta(days=1),
        conexao=CONEXAO_LOCAL,
        Clima=simulador.Clima
    )
    esperado = set(['camiseta regata', 'tênis leve cano baixo', 'bermuda'])
    assert mala == esperado
