import plotly.express as px
from .project_calories import project_calories


def exercise_plan(weight, height, sex, age, target_weight, number_of_days, return_graph=False):
    """Create an exercise plan based on current weight, height, age and target
    BMI.

    The calorie consumption needed each day is computed and a set of activities
    is suggested accordingly. If `return_graph` is `True`, a
    `plotly.graph_objects.Figure` object instead of a dictionary.

    Parameters
    ----------
    weight : float
        Weight, in kilograms.
    height : float
        Height, in meters.
    sex : int
        Sex, used in the Harris–Benedict equation estimation, 1 for male and
        2 for female.
    age : int
        Current age, in years.
    target_weight : float
        Target weight, in kilograms.
    number_of_days : int
        Number of days to reach the target weight.
    return_graph : bool
        Whether to return a graph instead of a dictionary.
    
    Returns
    -------
    dict or plotly.graph_objects.Figure
        If `return_graph` is `False`, we get a dictionary with key to be different
        exercises, and the value to be number of minutes (rounded to nearest
        integer) needed for that activity. Note that each of the activities are
        associated as an "or". If `return_graph` is True, we get a
        `plotly.graph_objects.Figure` instead that can be saved or shared.
    
    Examples
    --------
    >>> exercise_plan(100, 1.83, 2, 27, 68, 30)
    >>> {'Leisure cycling or walking': 213,
    >>> 'Moderate rope-jumping': 88,
    >>> 'General running': 112,
    >>> 'Leisure swimming': 156}
    """
    # Compute daily calorie loss, assume the lowest activity level
    calorie_loss_projection = project_calories(
        weight, height, sex, age, 1.2, target_weight, number_of_days, return_graph=False
    )

    # Use target consumption to calculate the daily activity level
    target_calorie_consumption = 2200 # heuristic
    calorie_consumption_each_day = target_calorie_consumption - calorie_loss_projection
    if calorie_consumption_each_day < 0:
        raise ValueError("Calorie consumption out of range, please verify your numbers")

    # Selected activities simplified and computed from here, it is on per minute:
    # https://www.nutristrategy.com/activitylist4.htm
    activities = {
        "Leisure cycling or walking": 330.0 / 60,
        "Moderate rope-jumping": 800.0 / 60,
        "General running": 630.0 / 60,
        "Leisure swimming": 450.0 / 60
    }

    # Calculate daily activity needed, on an "or" manner
    activity_time = {}
    for _, (activity, calorie_per_min) in enumerate(activities.items()):
        activity_time[activity] = round(calorie_consumption_each_day / calorie_per_min)

    if return_graph:
        graph_bars = {
            "Activity": list(activity_time.keys()),
            "Time, in Minutes": list(activity_time.values())
        }
        return px.bar(graph_bars, x='Time, in Minutes', y='Activity', title="Recommended Daily Activities")
    else:
        return activity_time
