def exercise_plan(weight, height, target_bmi, age, number_of_days, return_graph=False):
    """Create an exercise plan based on current weight, height, age and target
    BMI.

    The calorie consumption needed each day is computed and a set of activities
    is suggested accordingly. If `return_graph` is `True`, an `alt.Chart` object
    instead of a dictionary.

    Parameters
    ----------
    weight : float
        Weight, in kilograms.
    height : float
        Height, in meters.
    target_bmi : float
        Target BMI.
    age : int or float
        Current age, in years.
    number_of_days : int
        Number of days to reach the target BMI
    return_graph : bool
        Whether to return a graph instead of a dictionary
    
    Returns
    -------
    dict or alt.Chart
        If `return_graph` is `False`, we get a dictionary with key to be different
        exercises, and the value to be number of minutes (rounded to nearest
        integer) needed for that activity. Note that each of the activities are
        associated as an "or". If `return_graph` is True, we get an `alt.Chart`
        instead that can be saved or shared.
    """
    pass
