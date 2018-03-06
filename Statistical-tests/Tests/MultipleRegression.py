import numpy as np
import pandas as pd

import statsmodels.api as sm

from sklearn import datasets
from pandas.core import datetools

class MultipleRegression():
    def __init__(self, x, y, independent_columns, dependent_column):
        """
            x - array of dictionaries which contain the independent values
            y - array of dictionaries which contain the dependent values for which we can apply linear regression
            independent_columns - array of column names which contain values that are independent
            dependent_column - column names which contain values that are dependent to independent values
        """

        self.x = pd.DataFrame(x)
        self.y = pd.DataFrame(y)
        self.independent_columns = independent_columns
        self.dependent_column = dependent_column

    def run(self):
        x_axis = self.x[self.independent_columns]
        y_axis = self.y[self.dependent_column]

        model = sm.OLS(y_axis, x_axis).fit()
        predictions = model.predict(x_axis) # make the predictions by the model

        # R-squared - coefficient of determination, is a statistical measure of how well the regression line
        ##   approximates the real data points

        # F-statistic - The F-statistic is simply a ratio of two variances. Variances are a measure of dispersion,
        ##   or how far the data are scattered from the mean. Larger values represent greater dispersion.

        # Prob (F-statistic): the probability of obtaining the estimated value of the parameter
        ##   if the actual parameter value is zero

        # Log-Likelihood: probability of predicting the actual value

        # Akaike information criterion (AIC) - is an estimator of the relative quality of
        ##    statistical models for a given set of data

        # Bayesian information criterion (BIC) or Schwarz criterion (also SBC, SBIC) is a criterion
        ##    for model selection among a finite set of models; the model with the lowest BIC is preferred

        print(model.summary())


def run_test():
    boston_dataset = datasets.load_boston()
    independent_columns = ["RM", "LSTAT"]
    dependent_column = "MEDV"

    x = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
    y = pd.DataFrame(boston_dataset.target, columns=[dependent_column])
    model = MultipleRegression(x, y, independent_columns, dependent_column)

    model.run()

run_test()
