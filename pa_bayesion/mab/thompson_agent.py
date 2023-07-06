import pandas as pd
import numpy as np

class thompson_agent:

    def get_page():
        data = thompson_agent.load_data()

        data['no_click'] = data['visit'] - data['click']
        click_array = data.groupby('group').sum().reset_index()[['click', 'no_click']].T.to_numpy()
        #click_array = click_array[['click', 'no_click']].T.to_numpy()

        success = click_array[0]
        failed = click_array[1]

        prob_reward = np.random.beta(success, failed)
        
        return 'blue' if np.argmax(prob_reward) == 0 else 'red'

    def load_data():
        return pd.read_csv('pa_bayesion/mab/data_experiment.csv')

    