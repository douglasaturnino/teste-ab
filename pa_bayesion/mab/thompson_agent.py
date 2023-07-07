import os
import pandas as pd
import numpy as np

class thompson_agent:

    def get_page():
        data = thompson_agent.load_data()

        data['no_click'] = data['visit'] - data['click']
        click_array = data.groupby('group').sum().reset_index()
        click_array = click_array[['click', 'no_click']].T.to_numpy()

        success = click_array[0]
        failed = click_array[1]

        try:
            prob_reward = np.random.beta(success, failed)
            return 'blue' if np.argmax(prob_reward) == 0 else 'red'
        except ValueError:
            random_page = np.random.randint(low=0, high=2, size=1)
            return 'blue' if random_page == 0 else 'red'



    def load_data():
        caminho = thompson_agent.verificar_arquivo_exist()
        return pd.read_csv(caminho)

    def verificar_arquivo_exist():
        home = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(home, 'dataset', 'data_experiment.csv')

        data = pd.DataFrame(columns=['click','visit','group'],)
        
        if not os.path.exists(caminho):
            os.mkdir(os.path.dirname(caminho))
            data.to_csv(caminho,index=False)
        
        return caminho

if __name__ == '__main__':
    pass

    