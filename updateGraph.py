from numpy import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def grafico_calculos(vlab, ilab, iFab):
    tudo = []
    # amostra
    n = 200
    t = np.linspace(0, 0.100, n)
    angulo1 = 15
    angulo2 = 40
    angulo3 = 75
    f = 60
    w = 2*np.pi*f
    
    VLab =  vlab  #100 INPUT
    ILab = ilab   #1.237 INPUT
    iF = iFab   #0.714 INPUT

    def V1(segundos):
        resultado = []
        for segundo in segundos:
            ysolon = VLab*np.sin((w*segundo)+angulo1)
            resultado.append(ysolon)
        return resultado

    def V2(segundos):
        resultado = []
        for segundo in segundos:
            ysolon = ILab*np.sin((w*segundo)+angulo2)
            resultado.append(ysolon)
        return resultado

    def V3(segundos):
        resultado = []
        for segundo in segundos:
            ysolon = iF*np.sin((w*segundo)+angulo3)
            resultado.append(ysolon)
        return resultado

    v1 = V1(t)
    v2 = V2(t)
    v3 = V3(t)

    tudo.append(v1)
    tudo.append(v2)
    tudo.append(v3)
    tudo.append(t)

    return tudo