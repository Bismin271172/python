import numpy as np
def mae (obs, model):
    b = np.abs((obs-model)).mean()
    return b