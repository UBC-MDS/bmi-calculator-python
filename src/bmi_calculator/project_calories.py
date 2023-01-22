import pandas as pd
import numpy as np
import plotly.express as px

def project_calories(weight, height, sex, age, pal, target_weight, number_of_days, return_graph=False):
    """Returns caloric intake per day based in a target weight. Assumption is that the goal is losing weight
    rather than gaining weight.

    Parameters
    ----------
    weight : float
        Current weight in kilograms (kg).
    height : float
        Current height in meters (m).
    sex : int
        1 for male.
        2 for female.
    age : int
        Current age in years.
    pal : float
        Physcial activity level, can only be one of the four listed values
        1.2 for "Little/no exercise"
        1.4 for "Light exercise 1-3 times a week"
        1.6 for "Moderate exercise 3-5 times a week"
        1.75 for "Hard exercise 3-5 times a week"
    target_weight: int
        Weight goal to be achieved in number_of_days.
    number_of_days : int
        Number of days alotted to achieve target_bmi
    return_graph : bool
        If `return_graph` is `False`, returns a float specifying caloric intake/number_of_days
        If `return_graph` is `True`, returns a straight line graph of projected caloric intake/day

    Returns
    -------
    float or plotly.graph_objects.Figure
        If `return_graph` is `False`, specifies caloric intake/number_of_days. If `return_graph` is `True`, 
        returns a straight line graph of projected caloric intake/day

    Examples
    --------
    >>> project_calories(68.1, 1.83, 22, 25, 100, return_graph=True)
    """
    # Ensuring that inputs are valid
    if weight <= 0 or height <= 0 or age <=0 or target_weight <=0 or number_of_days <=0:
        raise ValueError("Please check your input values and ensure that they are appropriate")

    if pal not in [1.2, 1.4, 1.6, 1.75]:
        raise ValueError("Please enter either 1.2, 1.4, 1.6, or 1.75 as a value for pal")
    
    if target_weight > weight:
        raise ValueError("This application is for weight loss only. Please enter a target weight that is lower than your current weight")

    # Calories per day calculation 
    if sex == 1:
        BMR = 66.47 + (13.75*weight) + (5.003*(height*100)) - (6.755*age)
    elif sex == 2:
        BMR = 665.1 + (9.563*weight) + (1.85*(height*100)) - (4.676*age)
    else:
        raise TypeError("Please enter either 1 for male or 2 for female as a sex value")
    
    calories_sustain_weight = BMR * pal
    calories_lose_weight = (weight - target_weight) * (1100/number_of_days)

    calories_per_day = calories_sustain_weight - calories_lose_weight

    # Producing either final value or graph
    if return_graph == False:
        return calories_per_day
    else:
        df = {
            "days": np.arange(0, number_of_days),
            "weight": np.linspace(weight, target_weight, len(np.arange(0, number_of_days)))
        }
        
        fig = px.line(df, x="Days", y="Weight", title='Projected Weight Loss')
        fig.update_yaxes(range=[target_weight - 5, weight + 5])
        return fig
    

    
