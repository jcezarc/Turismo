from pony.orm import select, db_session
from datetime import datetime


class Clima:
    @db_session
    def __init__(self, cidade: str, periodo: datetime, **args):
        """
        Consulta viagens anteriores a esta mesma cidade no mesmo 
        período e retorna como o *clima* estava naquela ocasião:
        """
        Viagem = args['model']
        self.dados = select(
            (roupa.chuva, roupa.temperatura)
            for v in Viagem 
            for roupa in v.mala
            if v.cidade == cidade
            and v.periodo.month == periodo.month
        )[:5]
