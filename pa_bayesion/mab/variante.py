import os
import pandas as pd
from infra.repository.experimento_repository import ExperimentoRepository


class variante(object):
    def __init__(self, visit, click, group):
        self.visit = visit
        self.click = click
        self.group = group

    def salvar_experiment(self):
       repo = ExperimentoRepository()
       repo.insert(self.click, self.visit, self.group)

    def load_data():
        repo = ExperimentoRepository()
        return repo.select()

if __name__ == '__main__':
    caminho = variante(1,1, 'red')

    caminho.salvar_experiment()
