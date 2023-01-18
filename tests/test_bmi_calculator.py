from bmi-calculator-python import calculate_bmi as calc_bmi # Need to figure out how to call the function.
import plotly.graph_objects as go
import pytest

def test_calculate_bmi():
    """Test plot_histogram on a dataframe."""
    # Case 1: Test default settings and return. 
    assert round(calculate_bmi(weight=108, height=1.88),2) == 30.56, "Incorrect BMI calculation!"
    assert round(calculate_bmi(weight=50, height=1.65),2) == 18.37, "Incorrect BMI calculation!"
    assert round(calculate_bmi(weight=250, height=1.65,),2) == 91.83, "Incorrect BMI calculation!"
    
    # Case 2: Test when return_graph=True and return.
    graph = calculate_bmi(weight=50, height=1.65, return_graph = True)
    assert isinstance(graph, go.Figure), "Plotly Figure object should be returned."
    assert ('data' in graph and 'layout' in graph), "Plotly Figure structure not properly set."
    assert graph.data[0].title.text == 'Body Mass Index', "Plotly Figure title not properly set."
    assert graph.data[0].mode == 'gauge+number+delta', "Plotly Figure mode not properly set."
    assert round(graph.data[0].value, 2) == 18.37, "Plotly Figure bmi data not properly calculated."

    # Case 3: Test missing or erroneous inputs
    with pytest.raises(Exception):
        calculate_bmi(weight=None, height=1.65)
        calculate_bmi(weight=100, height=None)
        calculate_bmi(weight=100, height=1.65, return_graph=1)
        calculate_bmi(weight=100, height=1.65, return_graph=0)
        calculate_bmi()

    # Case 4: Test negative or zero inputs
    with pytest.raises(Exception):
        calculate_bmi(weight=-100, height=1.65)
        calculate_bmi(weight=100, height=-1.65)
        calculate_bmi(weight=0, height=1.65)
        calculate_bmi(weight=100, height=0)