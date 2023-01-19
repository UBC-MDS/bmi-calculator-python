from bmi_calculator import project_calories

import plotly.express as px
import pytest

def test_standard_case():
    """Test standard case"""
    assert round(project_calories(weight=68, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30), 2) == 2334.29, "Incorrect daily caloric intake calculation!"
    assert round(project_calories(weight=90, height=1.90, sex=1, age=30, pal=1.2, target_weight=25, number_of_days=40), 2) == 1233.31, "Incorrect daily caloric intake calculation!"
    assert round(project_calories(weight=55, height=1.23, sex=2, age=19, pal=1.4, target_weight=45, number_of_days=25), 2) == 1421.68, "Incorrect daily caloric intake calculation!"

def test_return_graph():
    """Test when return_graph=True"""
    graph = project_calories(weight=90, height=1.90, sex=1, age=30, pal=1.2, target_weight=25, number_of_days=40, return_graph=True)
    assert isinstance(graph, px.Figure), "Plotly Figure object should be returned."
    assert ('data' in graph and 'layout' in graph), "Plotly Figure structure not properly set."
    assert graph.data[0].title.text == 'Projected Weight Loss', "Plotly Figure title not properly set."
    assert round(graph.data[0].value, 2) == 18.37, "Plotly Figure bmi data not properly calculated."

def test_exception_cases():
    """Test exception cases"""
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=2, age=27, pal=1.6, target_weight=None, number_of_days=30)
    with pytest.raises(Exception):
        project_calories(weight=68, height=None, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=None, age=27, pal=1.6, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        project_calories(weight=None, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30)      
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=2, age=None, pal=1.6, target_weight=65, number_of_days=30)  
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=2, age=27, pal=None, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        project_calories(weight=68, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=None)    
    with pytest.raises(Exception):
        project_calories()

def test_negative_or_zero_inputs():
    """Test negative or zero inputs"""
    with pytest.raises(ValueError):
        project_calories(weight=-2, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30)    
    with pytest.raises(ValueError):
        project_calories(weight=63, height=0, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        project_calories(weight=63, height=1.83, sex=2, age=0, pal=1.6, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        project_calories(weight=63, height=1.83, sex=2, age=27, pal=1.6, target_weight=0, number_of_days=30)
    with pytest.raises(ValueError):
        project_calories(weight=63, height=1.83, sex=2, age=27, pal=1.6, target_weight=65, number_of_days=0)    
