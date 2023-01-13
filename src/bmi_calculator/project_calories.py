def project_calories(weight, height, target_bmi, age, number_of_days, return_graph=False):
    """Load text from a text file and return as a string.

    Parameters
    ----------
    weight : float
        Current weight in kilograms (kg).
    height : float
        Current height in centimeters (meters).
    target_bmi: int
        Body mass index (BMI) goal to be achieved in number_of_days.
    age : int
        Current age in years.
    number_of_days : int
        Number of days alotted to achieve target_bmi
    return_graph : bool
        If `return_graph` is `False`, returns a float specifying caloric intake/number_of_days
        If `return_graph` is `True`, returns a straight line graph of projected caloric intake/day

    Returns
    -------
    float or alt.Chart
        If `return_graph` is `False`, specifies caloric intake/number_of_days. If `return_graph` is `True`, 
        returns a straight line graph of projected caloric intake/day

    Examples
    --------
    >>> project_calories(68.1, 1.83, 22, 25, 100, return_graph=True)
    """
    pass