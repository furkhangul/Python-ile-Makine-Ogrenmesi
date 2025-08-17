"""
Kukla Değişken:
bir veriyi taklit eden veya başka bir kolonu ifade eden verilerdir.

mesela erkek ve kız değerlerine 0 ve 1 değerlerini atama.
erkek:1 , kız:0 gibi

makine öğrenmesinde aynı verileri birden fazla defa öğrenmeye sokarsanız diğer verilere
de zarar vermekte hata oranını arttırmaktadır.

kukla verileri ile ana veriyi aynı anda eklememiz doğru değildir.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

veriler = pd.read_csv("veriler.csv")
