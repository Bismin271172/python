import numpy as np
def rmse(obs, model):
    a = np.sqrt(((obs - model) ** 2).mean())
    return a