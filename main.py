import os
import pandas as pd
import numpy as np

from pgmpy.models import BayesianNetwork

from pgmpy.estimators import HillClimbSearch, BDsScore
from pgmpy.factors.discrete import State

import config

# ---- Read CSV and short preprocessing ---------------------------------
dir = os.getcwd()
file_path = os.path.join(dir, "definitive_data.csv")

df = pd.read_csv(file_path, index_col = None)

print("Successful data read")
# -----------------------------------------------------------------------


# ---- Structure Learning -----------------------------------------------
target = config.inputs["target"]
blck_lst = config.structure["black_list"]
fxd_edges = config.structure["fixed_edges"]

from pgmpy.estimators import HillClimbSearch, BDsScore

est = HillClimbSearch(data = df)
model = est.estimate(scoring_method=BDsScore(df, equivalent_sample_size = 5), fixed_edges=fxd_edges, black_list=blck_lst)
print("Successful structure learning")
# -----------------------------------------------------------------------


# ----- Save learned model ----------------------------------------------

if not os.path.exists("images"):
        os.mkdir("images")

if not os.path.exists("riskmap_datasets"):
        os.mkdir("riskmap_datasets")

# PRIOR NET
import pyAgrum as gum
import pyAgrum.lib.image as gumimage
import matplotlib.pyplot as plt
import graphviz

bn_gum = gum.BayesNet()
bn_gum.addVariables(list(df.columns))
bn_gum.addArcs(list(fxd_edges))

path = "images/"
file_name = str('cancer_breast_prior') + '.png'
file_path = os.path.join(path,file_name)

gumimage.export(bn_gum, file_path, size = "20!",
                nodeColor = config.node_color,
                            )

# POSTERIOR NET
bn_gum_2 = gum.BayesNet()
bn_gum_2.addVariables(list(df.columns))
bn_gum_2.addArcs(list(model.edges))

arcColor_mine = dict.fromkeys(bn_gum_2.arcs(), 0.3)
for elem in list(bn_gum.arcs()):
    arcColor_mine[elem] = 1

path = "images/"
file_name = str('cancer_breast_learned_bds') + '.png'
file_path = os.path.join(path,file_name)

gumimage.export(bn_gum_2, file_path, size = "20!",
                 nodeColor = config.node_color,
              
                cmapArc =  plt.get_cmap("hot"),
                arcColor= arcColor_mine )

print("Successful graphic models save")
