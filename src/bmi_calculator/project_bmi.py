def project_bmi(weight, height, target_bmi, number_of_days, return_graph=False):
    """Compute averge BMI change per day based on current weight, height, age and target
    BMI.

    The average BMI increase or decrease each day is computed. If `return_graph` is `True`, an `alt.Chart` is given based on forcasted BMI for the targetted timeframe 

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
    float
        Averrage BMI change per day
    alt.Chart
        If `return_graph` is `False`, we get a dictionary with key to be different
        exercises, and the value to be number of minutes (rounded to nearest
        integer) needed for that activity. Note that each of the activities are
        associated as an "or". If `return_graph` is True, we get an `alt.Chart`
        instead that can be saved or shared.
    """
    pass
