from datetime import datetime
from pony.orm import db_session,  select, commit, sql_debug
from db.models import db_factory, dados_iniciais


def grava_viagem(cidade: str, periodo: datetime, conexao: dict, Clima: type):
    rol = set()
    db, Roupa, Viagem = db_factory(**conexao)
    dados_iniciais(Roupa)
    clima = Clima(
        cidade=cidade,
        periodo=periodo,
        model=Viagem
    )
    @db_session
    def faz_mala():
        mala = []
        sql_debug(True)
        for chuva, temperatura in clima.dados:
            temp_min, temp_max = temperatura -5.0, temperatura + 5.0
            roupas = select(
                r for r in Roupa
                if r.chuva == chuva
                and r.temperatura >= temp_min
                and r.temperatura <= temp_max
            )[:]
            for roupa in roupas:
                if roupa not in mala:
                    mala.append(roupa)
                    rol.add(roupa.nome)
        sql_debug(False)
        Viagem(
            cidade=cidade,
            periodo=periodo,
            mala=mala
        )
        commit()
    faz_mala()
    return rol
