import pandas as pd
import os

class Inputs(object):
    def __init__(self, input_path, *filename):
        self.basedir = input_path
        self.filelist = filename
        self.data_dict = {}

    def read_csv(self, fpath):
        df = pd.read_csv(fpath)
        n, d = df.shape
        print(f"Reading {n} rows and {d} columns from {fpath}.")
        return df

    def load_all_df(self):
        for fn in self.filelist:
            k = fn.replace('.csv', '')
            fpath = os.path.join(self.basedir, fn)
            self.data_dict[k] = self.read_csv(fpath)

