import plotly.graph_objects as go


def calculate_bmi(weight, height, return_graph=False):
    """Calculate the body mass index (BMI) based on current weight and height.

    Body Mass Index (BMI) is a calculated measure of weight relative to height,
    defined as body weight in kilograms divided by height in meters squared
    (Keys et al., 1972). If `return_graph` is `True`, an
    `plotly.graph_objects.Figure` object instead of a bmi value.

    Parameters
    ----------
    weight : float
        Weight, in kilograms. Must have a positive value.
    height : float
        Height, in meters. Must have a positive value.
    return_graph : bool
        Whether to return a graph instead of a value

    Returns
    -------
    float or plotly.graph_objects
        If `return_graph` is `False`, we get a value of the body mass index.
        If `return_graph` is True, we get a `plotly.graph_objects.Figure`
        instead that can be saved or shared.
    
    Examples
    -------
    >>> calculate_bmi(100, 1.85, return_graph=False)
    >>> 29.218407596785973
    
    """
    if not (
        isinstance(weight, (int, float))
        & isinstance(height, (int, float))
        & isinstance(return_graph, bool)
    ):
        raise TypeError(
            "TypeError! Please check carefully on the type of input parameters! "
        )

    if not ((weight > 0) & (height > 0)):
        raise ValueError(
            "ValueError! Please enter a positive non-zero weight and height!"
        )

    bmi = weight / (height**2)
    if return_graph == False:
        return bmi
    else:
        fig = go.Figure(
            go.Indicator(
                mode="gauge+number+delta",
                value=bmi,
                domain={"x": [0, 1], "y": [0, 1]},
                title={"text": "Body Mass Index", "font": {"size": 24}},
                delta={"reference": 25, "increasing": {"color": "Pink"}},
                gauge={
                    "axis": {"range": [None, 50], "tickwidth": 1, "tickcolor": "black"},
                    "bar": {"color": "Red"},
                    "bgcolor": "white",
                    "borderwidth": 2,
                    "bordercolor": "black",
                    "steps": [
                        {"range": [0, 18.5], "color": "lightblue"},
                        {"range": [18.5, 25], "color": "lightgreen"},
                        {"range": [25, 30], "color": "lightyellow"},
                        {"range": [30, 35], "color": "orange"},
                        {"range": [35, 50], "color": "Pink"},
                    ],
                },
            )
        )
        fig.update_layout(font={"color": "darkblue", "family": "Arial"})
        return fig
