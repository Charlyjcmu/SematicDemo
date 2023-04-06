"""
This is the module in which you define your pipeline functions.

Feel free to break these definitions into as many files as you want for your
preferred code structure.
"""
# Sematic
import sematic
import plotly
from dataclasses import dataclass

from movie_rec.exploration import (load_data,
                        ratings_hist_fun, 
                        test_split,
                        train_split, 
                        train_rmse)

# @dataclass
# class PipelineOutput:
#     rmse = float
#     #ratings_hist: plotly.graph_objs.Figure

@sematic.func
def pipeline(features: int) -> float:
    """
    The root function of the pipeline.
    """
    data = load_data()
    #ratings_hist = ratings_hist_fun(data)
    train = train_split(data)
    test = test_split(data)
    rmse = train_rmse(train, test,features)

    return rmse
    
