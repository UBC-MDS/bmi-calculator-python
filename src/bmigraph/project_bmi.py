import pandas as pd
import numpy as np
import plotly.express as px
import plotly

def project_bmi(weight, height, target_bmi, number_of_days, return_graph=False):
    """Compute average BMI change per week based on current weight, height, age
    and target BMI.

    The average BMI increase or decrease each day is computed. If `return_graph`
    is `True`, a `plotly.graph_objects.Figure` is given based on forcasted BMI
    for the target timeframe.

    Parameters
    ----------
    weight : float
        Weight, in kilograms.
    height : float
        Height, in meters.
    target_bmi : float
        Target BMI.
    number_of_days : int
        Number of days to reach the target BMI
    return_graph : bool
        Whether to return a graph instead of a dictionary

    Returns
    -------
    float or `plotly.graph_objects.Figure`
        If `return_graph` is `True`, we get the average BMI change per week.
        If `return_graph` is `False`, we get a dictionary with key to be different
        exercises, and the value to be number of minutes (rounded to nearest
        integer) needed for that activity. Note that each of the activities are
        associated as an "or". If `return_graph` is True, we get a
        `plotly.graph_objects.Figure` instead that can be saved or shared.
    
    Example
    -------
    >>> project_bmi(weight=108, height=1.88, target_bmi = 28, number_of_days=60)
    >>> -0.3
    """
    # check for bad inputs
    if not (
        isinstance(weight, (int, float))
        & isinstance(height, (int, float))
        & isinstance(target_bmi, (int, float))
        & isinstance(number_of_days, (int, float))
        & isinstance(return_graph, bool)
    ):
        raise TypeError("TypeError! Please check the type of input parameters! ")
    if not ((weight > 0) & (height > 0) & (target_bmi > 0) & (number_of_days > 0)):
        raise ValueError(
            "ValueError! Please enter a positive value for weight, height, target_bmi, and number of days!"
        )
    # BMI change computation
    current_bmi = weight / height**2
    bmi_change = target_bmi - current_bmi
    bmi_change_per_day = bmi_change / number_of_days
    # return computation or graph
    if not return_graph:
        return round(bmi_change_per_day * 7, 2)
    else:
        df = {
            "Days": np.arange(number_of_days),
            "BMI change": np.linspace(
                current_bmi, target_bmi, len(np.arange(number_of_days))
            ),
        }
        fig = px.line(df, x="Days", y="BMI change", title="Projected BMI trajectory")
        fig.update_yaxes(
            range=[
                min(current_bmi, target_bmi) - 3,
                max(current_bmi, target_bmi) + 3,
            ]
        )
        return fig
