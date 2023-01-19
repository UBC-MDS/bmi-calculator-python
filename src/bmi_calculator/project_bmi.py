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
    def project_bmi(weight, height, target_bmi, number_of_days, return_graph=False):
        current_bmi = weight/height**2
        bmi_change = target_bmi - current_bmi

        if not (
            isinstance(weight, (int, float))
            & isinstance(height, (int, float))
            & isinstance(return_graph, bool)
        ):
            raise TypeError(
                "TypeError! Please check the type of input parameters! "
            )

        if not ((weight > 0) & (height > 0)):
            raise ValueError(
                "ValueError! Please enter a positive non-zero weight and height!"
            )

        bmi_change_per_day = bmi_change/number_of_days
        
        df = {'Days': np.arange(0, number_of_days), 
              'BMI change': np.arange(current_bmi, target_bmi,
              bmi_change_per_day)}

        if return_graph:
          fig = px.line(df, x="Days", y="BMI change", title='Projected BMI trajectory')
          fig.show()
    
    return round(bmi_change_per_day*7, 2)
