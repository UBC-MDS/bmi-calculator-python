from bmigraph import project_bmi
import plotly.express as px
import plotly
import pytest


def test_standard_case():
    """Test standard case"""
    assert project_bmi(weight=108, height=1.88, target_bmi = 28, number_of_days=60) == -0.30, "Incorrect BMI calculation!"
    assert project_bmi(weight=108, height=1.88, target_bmi = 33, number_of_days=60) == 0.29, "Incorrect BMI calculation!"
    assert project_bmi(weight=78, height=1.69, target_bmi = 25, number_of_days=100) == -0.16, "Incorrect BMI calculation!"

def test_return_graph():
    """Test when return_graph=True"""
    graph = project_bmi(weight=108, height=1.88, target_bmi = 33, number_of_days=60, return_graph = True)
    assert isinstance(graph, plotly.graph_objs._figure.Figure), "Plotly Figure object should be returned."
    assert ('data' in graph and 'layout' in graph), "Plotly Figure structure not properly set."
    assert graph.layout['title']['text'] == 'Projected BMI trajectory', "Plotly Figure title not properly set."
    assert round(graph.data[0]['y'][0],2) == 30.56, "Plotly Figure bmi data not properly calculated."

def test_exception_cases():
    """Test exception cases"""
    with pytest.raises(Exception):
        project_bmi(weight=None, height=1.88, target_bmi = 28, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=None, target_bmi = 28, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=1.88, target_bmi = None, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=1.88, target_bmi = 28, number_of_days=None)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=1.88, target_bmi = 28, number_of_days=60, return_graph=1)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=1.88, target_bmi = 28, number_of_days=60, return_graph=0)
    with pytest.raises(Exception):
        project_bmi()

def test_negative_or_zero_inputs():
    """Test negative or zero inputs"""
    with pytest.raises(Exception):
        project_bmi(weight=-10, height=1.88, target_bmi = 28, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=108, height=0, target_bmi = 28, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=90, height=1.88, target_bmi = -2, number_of_days=60)
    with pytest.raises(Exception):
        project_bmi(weight=90, height=1.88, target_bmi = 20, number_of_days=-40)
