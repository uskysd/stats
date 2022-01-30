# Created by Yusuke Yoshida on 1/29/2022
# Run a repeatad meausre ANOVA

import os
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import pingouin as pg

datafile = "input\\sample.csv"
INPUT = "input"
OUTPUT = "output"

def main():
    for fname in os.listdir(INPUT):
        fpath = os.path.join(INPUT, fname)
        print("Reading file: {}".format(fpath))
        df = pd.read_csv(fpath)

        # Create a box plot 
        ax = sns.boxplot(x="session", y="score", data=df)
        plt.show()

        # Run a repeated measure ANOVA
        result = pg.rm_anova(dv='score', within='session', subject='patient', data=df, detailed=True)
        print(result)

        # Export data
        outfile = os.path.join(OUTPUT, "rmanova_"+fname)
        result.to_csv(outfile)


if __name__=="__main__":
    main()