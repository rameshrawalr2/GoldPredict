from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import acf
import pmdarima as pm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def model(df):
    # Plot
    # fig, axes = plt.subplots(2, 1, figsize=(10, 5), dpi=100, sharex=True)

    # Usual Differencing
    # axes[0].plot(df[:], label='Original Series')
    # axes[0].plot(df.diff(5), label='Usual Differencing')
    # axes[0].set_title('Usual Differencing')
    # axes[0].legend(loc='upper left', fontsize=10)
    #
    # # Seasinal Dei
    # axes[1].plot(df[:], label='Original Series')
    # axes[1].plot(df[:].diff(12), label='Seasonal Differencing', color='green')
    # axes[1].set_title('Seasonal Differencing')
    # plt.legend(loc='upper left', fontsize=10)
    # plt.suptitle('a10 - Drug Sales', fontsize=16)
    # plt.show()
    # # 1,1,2 ARIMA Model
    # model = ARIMA(df.Price_g, order=(3, 2, 1))
    # model_fit = model.fit(disp=-1)
    # print(model_fit.summary())
    # model_fit.plot_predict(dynamic=False)
    # plt.show()
    # residuals = pd.DataFrame(model_fit.resid)
    # fig, ax = plt.subplots(1, 2)
    # residuals.plot(title="Residuals", ax=ax[0])
    # residuals.plot(kind='kde', title='Density', ax=ax[1])
    # plt.show()
    # return model
    # model = ARIMA(train, order=(1,2,1))
    model = pm.auto_arima(df.Price_g, start_p=1, start_q=1,
                         test='adf',
                         max_p=3, max_q=3, m=12,
                         start_P=0, seasonal=True,
                         d=None, D=1, trace=True,
                         error_action='ignore',
                         suppress_warnings=True,
                         stepwise=True)
    model.plot_diagnostics(figsize=(7, 5))
    plt.show()
    n_periods = 24
    fc, confint = model.predict(n_periods=n_periods, return_conf_int=True)
    index_of_fc = np.arange(len(df.Price_g), len(df.Price_g) + n_periods)

    # make series for plotting purpose
    fc_series = pd.Series(fc, index=index_of_fc)
    lower_series = pd.Series(confint[:, 0], index=index_of_fc)
    upper_series = pd.Series(confint[:, 1], index=index_of_fc)

    # Plot
    plt.plot(df.Price_g)
    plt.plot(fc_series, color='darkgreen')
    plt.fill_between(lower_series.index,
                     lower_series,
                     upper_series,
                     color='k', alpha=.15)

    plt.title("Final Forecast of WWW Usage")
    plt.show()
