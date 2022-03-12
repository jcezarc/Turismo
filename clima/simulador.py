from datetime import datetime

CIDADES_FANTASIA = {
    'Nárnia': [(True, 10)],  #  ...Chuva e frio
    'Mordor': [(False, 30)],  #  Calor intenso!
}


class Clima:
    """
    Dados fictícios para testes
    * Se escolher `Nárnia` as roupas devem ser quentes e para chuva
    * Se escolher `Mordor` as roupas devem ser as mais leves possíveis
    """
    def __init__(self, cidade: str, periodo: datetime, **args):
        self.dados = CIDADES_FANTASIA[cidade]
