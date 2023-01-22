import pandas as pd
import numpy as np
import plotly.express as px


def project_calories(
    weight, height, sex, age, pal, target_weight, number_of_days, return_graph=False
):
    """Returns caloric intake per day based in a target weight. Assumption is
    that the goal is losing weight rather than gaining weight.

    Parameters
    ----------
    weight : float
        Current weight in kilograms (kg).
    height : float
        Current height in meters (m).
    sex : int
        Sex, used in the Harris–Benedict equation estimation, 1 for male and
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
        Number of days allotted to achieve target_weight.
    return_graph : bool
        Whether to return a graph instead of a float.

    Returns
    -------
    float or `plotly.graph_objects.Figure`
        If `return_graph` is `False`, returns a float specifying caloric intake
        divided by the number of days.
        If `return_graph` is `True`, returns a straight line graph of projected
        weight loss per day.

    Examples
    --------
    >>> project_calories(100, 1.85, 1, 25, 1.6, 75, 25, return_graph=False)
    >>> 2417.0400000000004
    """
    # Ensuring that inputs are valid
    if not (
        isinstance(weight, (int, float))
        & isinstance(height, (int, float))
        & isinstance(age, (int, float))
        & isinstance(pal, (int, float))
        & isinstance(target_weight, (int, float))
        & isinstance(number_of_days, (int, float))
        & isinstance(return_graph, bool)
    ):
        raise TypeError(
            "TypeError! Please check carefully on the type of input parameters! "
        )

    if (
        weight <= 0
        or height <= 0
        or age <= 0
        or target_weight <= 0
        or number_of_days <= 0
    ):
        raise ValueError(
            "Please check your input values and ensure that they are appropriate"
        )

    if pal not in [1.2, 1.4, 1.6, 1.75]:
        raise ValueError(
            "Please enter either 1.2, 1.4, 1.6, or 1.75 as a value for pal"
        )

    if target_weight > weight:
        raise ValueError(
            "This application is for weight loss only. Please enter a target weight that is lower than your current weight"
        )

    # Calories per day calculation
    if sex == 1:
        BMR = 66.47 + (13.75 * weight) + (5.003 * (height * 100)) - (6.755 * age)
    elif sex == 2:
        BMR = 665.1 + (9.563 * weight) + (1.85 * (height * 100)) - (4.676 * age)
    else:
        raise TypeError("Please enter either 1 for male or 2 for female as a sex value")

    calories_sustain_weight = BMR * pal
    calories_lose_weight = (weight - target_weight) * (1100 / number_of_days)

    calories_per_day = calories_sustain_weight - calories_lose_weight

    # Producing either final value or graph
    if return_graph == False:
        return calories_per_day
    else:
        df = {
            "Days": np.arange(number_of_days),
            "Weight": np.linspace(
                weight, target_weight, len(np.arange(number_of_days))
            ),
        }

        fig = px.line(df, x="Days", y="Weight", title="Projected Weight Loss")
        fig.update_yaxes(range=[target_weight - 5, weight + 5])
        return fig
