import numpy as np
import hjson 
import os

def main(inputAudioArray):
    config = hjson.load(open(os.path.dirname(os.path.realpath(__file__))+"/ampconfig.hjson"))
    return np.array(inputAudioArray)*config['multiplierConstant']
