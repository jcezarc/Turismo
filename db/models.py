import sys
from os import path
from csv import reader
from datetime import datetime
from pony.orm import (
    Database,
    PrimaryKey,
    Required,
    Set,
    select,
    db_session,
    commit
)

DB_PATH = 'c:/users/julio/turismo/db/'


def db_factory(**args):
    db = Database()
    db.bind(**args)
    class Roupa(db.Entity):
        id = PrimaryKey(int, auto=True)
        nome = Required(str)
        temperatura = Required(float)
        chuva = Required(bool)
        viagens = Set('Viagem')
    class Viagem(db.Entity):
        id = PrimaryKey(int, auto=True)
        cidade = Required(str)
        periodo = Required(datetime)
        mala = Set(Roupa)
    db.generate_mapping(create_tables=True)
    return db, Roupa, Viagem

@db_session
def dados_iniciais(Roupa):
    if select(r for r in Roupa).count() == 0:
        with open(f'{DB_PATH}roupas.csv', 'r', encoding='utf-8') as f:
            csv_reader = reader(f, delimiter=',')
            header = next(csv_reader)
            schema = [str, float, lambda x: x == '1']
            for row in csv_reader:
                values = {k: t(v) for k, t, v in zip(header, schema, row)}
                Roupa(**values)  # ROUPA NOVA ("Minha pequena Eva..." :)
        commit()
