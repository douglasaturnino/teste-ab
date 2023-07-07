import os
import pandas as pd

class variante(object):
    def __init__(self, visit, click, group):
        self.visit = visit
        self.click = click
        self.group = group

    def salvar_experiment(self):
        home = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(home, 'dataset', 'data_experiment.csv')

        data = pd.DataFrame(
            {
                'click': self.click,
                'visit': self.visit,
                'group': self.group

            },index=[0]
        )
        data.to_csv(caminho, mode='a', index=False, header=False)
                
        return caminho            
if __name__ == '__main__':
    caminho = variante(1,1, 'red')

    caminho.salvar_experiment()
