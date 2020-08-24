import numpy as np
import pandas as pd
import os

if __name__ == "__main__":
    if os.path.isfile('./data/train.csv'):
        train = np.array(pd.read_csv('./data/train.csv'))
    else:
        print('Not exist train')

    if os.path.isfile('./data/test.csv'):
        test = np.array(pd.read_csv('./data/test.csv'))
    else:
        print('Not exist test')


    if os.path.isfile('./data/submission.csv'):
        submission = np.array(pd.read_csv('./data/submission.csv'))
    else:
        print('Not exist submission')


    if os.path.isfile('./data/train.csv') and os.path.isfile('./data/test.csv') and os.path.isfile('./data/submission.csv'):
        print('All data loaded')