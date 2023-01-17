def calculate_bmi(weight, height, return_graph=False):
    """Calculate the body mass index (BMI) based on current weight and height.

    Body Mass Index (BMI) is a calculated measure of weight relative to height,
    defined as body weight in kilograms divided by height in meters squared
    (Keys et al., 1972). If `return_graph` is `True`, an `alt.Chart` object
    instead of a bmi value.

    Parameters
    ----------
    weight : float
        Weight, in kilograms.
    height : float
        Height, in meters.
    return_graph : bool
        Whether to return a graph instead of a value
    
    Returns
    -------
    float or alt.Chart
        If `return_graph` is `False`, we get a value of the body mass index. 
        If `return_graph` is True, we get an `alt.Chart` instead that can be
        saved or shared. Could be a simplified version of 
        https://cdn.dribbble.com/users/31916/screenshots/310892/bmi-chart.png
    """
    bmi = weight/(height ** 2)
    if return_graph == False:
        return bmi
    else:
        bmi=28.5
        fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = bmi,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Body Mass Index", 'font': {'size': 24}},
            delta = {'reference': 25, 'increasing': {'color': "Pink"}},
            gauge = {
                'axis': {'range': [None, 50], 'tickwidth': 1, 'tickcolor': "black"},
                'bar': {'color': "Red"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "black",
                'steps': [
                    {'range': [0, 18.5], 'color': 'lightblue'},
                    {'range': [18.5, 25], 'color': 'lightgreen'},
                    {'range': [25, 30], 'color': 'lightyellow'},
                    {'range': [30, 35], 'color': 'orange'},
                    {'range': [35, 50], 'color': 'Pink'}],
                }))
        
        fig.update_layout(font = {'color': "darkblue", 'family': "Arial"})
        
        fig.show()
        return fig
    