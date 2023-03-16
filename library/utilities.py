import sys
import os.path
import numpy as np
import array
import torch
import time
import random
import matplotlib.pyplot as plt


def ExtractCsv(path, debug=False):
    dir_files = os.listdir(path) 

    if(debug):
        print(f"Loaded path {path}")

    dir_files = [os.path.join(path, x) for x in dir_files]
    list_files = [x for x in dir_files if x[-3:] == 'csv']

    if(debug):
        print("Files in path:")
        print(list_files)
        print(f"Loaded {len(list_files)} CSVs")

    return list_files

def LoadCsvRaw(path, debug=False):
    with open(path) as f:
        content = f.read()
        content1D = content.split("\n")
        content2D = [entry.split(" ") for entry in content1D]
    if(debug):
        print("Loaded "+ path)
    return content2D

def LoadTxtRaw(path, debug=False):
    with open(path) as f:
        content = f.read()
        content1D = content.split("\n")
        content2D = [entry.split(" ") for entry in content1D]
    if(debug):
        print("Loaded "+ path)
    return content2D