from bmi_calculator import calculate_bmi
import plotly.graph_objects as go
import pytest


def test_standard_case():
    """Test standard case"""
    assert round(calculate_bmi(weight=108, height=1.88),2) == 30.56, "Incorrect BMI calculation!"
    assert round(calculate_bmi(weight=50, height=1.65),2) == 18.37, "Incorrect BMI calculation!"
    assert round(calculate_bmi(weight=250, height=1.65,),2) == 91.83, "Incorrect BMI calculation!"

def test_return_graph():
    """Test when return_graph=True"""
    graph = calculate_bmi(weight=50, height=1.65, return_graph = True)
    assert isinstance(graph, go.Figure), "Plotly Figure object should be returned."
    assert ('data' in graph and 'layout' in graph), "Plotly Figure structure not properly set."
    assert graph.data[0].title.text == 'Body Mass Index', "Plotly Figure title not properly set."
    assert graph.data[0].mode == 'gauge+number+delta', "Plotly Figure mode not properly set."
    assert round(graph.data[0].value, 2) == 18.37, "Plotly Figure bmi data not properly calculated."

def test_exception_cases():
    """Test exception cases"""
    with pytest.raises(Exception):
        calculate_bmi(weight=None, height=1.65)
    with pytest.raises(Exception):
        calculate_bmi(weight=100, height=None)
    with pytest.raises(Exception):
        calculate_bmi(weight=100, height=1.65, return_graph=1)
    with pytest.raises(Exception):
        calculate_bmi(weight=100, height=1.65, return_graph=0)
    with pytest.raises(Exception):
        calculate_bmi()

def test_negative_or_zero_inputs():
    """Test negative or zero inputs"""
    with pytest.raises(Exception):
        calculate_bmi(weight=-100, height=1.65)
    with pytest.raises(Exception):
        calculate_bmi(weight=100, height=-1.65)
    with pytest.raises(Exception):
        calculate_bmi(weight=0, height=1.65)
    with pytest.raises(Exception):
        calculate_bmi(weight=100, height=0)
