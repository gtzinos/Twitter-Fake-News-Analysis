import numpy
from numpy import array
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import datetime
from pandas import pandas as pd
import matplotlib.ticker as ticker

import matplotlib.dates as md
import dateutil


def getDates(mdb):
    dateDict = (mdb['w_3'].distinct("tweetObject.retweet"))
    return dateDict


def plotDates(mdb):
    # THIS WORKS
    df = pd.DataFrame(getDates(mdb), columns=['retweetCreatedAt'])
    print(df)
    df['tweets'] = df.groupby(level=0).count()
    df.index = pd.to_datetime(df['retweetCreatedAt'])

    del df['retweetCreatedAt']
    print(df)
    # print(df.groupby(df.index.to_period('D'), axis=0).sum())
    prePlot = df.resample(rule='1H', closed='left', label='left').sum()
    plot = prePlot.plot(kind='line', title='Tweets Diffusion in time', grid=True)
    plot.set(xlabel="Time", ylabel="Tweets")
    print(df)
    plt.show()

    # data = getDates(mdb)
    # dataArr = array(data)
    # print(type(dataArr))
