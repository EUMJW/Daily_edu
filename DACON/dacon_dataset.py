import numpy as np
import pandas as pd
import os

def load_npy(name,directory):
    name = np.load(directory)
    return name







if __name__ == "__main__":
    if os.path.isfile('./data/train.csv'):
        train = np.array(pd.read_csv('./data/train.csv'))
        np.save('./data/train',train)
    else:
        print('Not exist train')

    if os.path.isfile('./data/test.csv'):
        test = np.array(pd.read_csv('./data/test.csv'))
        np.save('./data/test',test)
    else:
        print('Not exist test')


    if os.path.isfile('./data/submission.csv'):
        submission = np.array(pd.read_csv('./data/submission.csv'))
        np.save('./data/submission',submission)
    else:
        print('Not exist submission')


    if os.path.isfile('./data/train.csv') and os.path.isfile('./data/test.csv') and os.path.isfile('./data/submission.csv'):
        print('All data loaded')

