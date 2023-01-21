from bmi_calculator import exercise_plan
import plotly.graph_objects as go
import pytest


def test_standard_case():
    """Test standard case"""
    assert exercise_plan(weight=68, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30)["General running"] == 45, "Incorrect exercise plan calculation"
    assert exercise_plan(weight=80, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30)["General running"] == 74, "Incorrect exercise plan calculation"
    assert exercise_plan(weight=120, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30)["General running"] == 170, "Incorrect exercise plan calculation"

def test_return_graph():
    """Test when return_graph=True"""
    graph = exercise_plan(weight=68, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30, return_graph = True)
    assert isinstance(graph, go.Figure), "Plotly Figure object should be returned"
    assert ('data' in graph and 'layout' in graph), "Plotly Figure structure not properly set"
    assert graph.layout['title']['text'] == 'Recommended Daily Activities', "Plotly Figure title not properly set"

def test_exception_cases():
    """Test exception cases"""
    with pytest.raises(Exception):
        exercise_plan(weight=None, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        exercise_plan(weight=68, height=None, sex=2, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        exercise_plan(weight=68, height=1.83, sex=None, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        exercise_plan(weight=68, height=1.83, sex=2, age=None, target_weight=65, number_of_days=30)
    with pytest.raises(Exception):
        exercise_plan(weight=68, height=1.83, sex=2, age=27, target_weight=None, number_of_days=30)
    with pytest.raises(Exception):
        exercise_plan(weight=68, height=1.83, sex=2, age=27, target_weight=65, number_of_days=None)
    with pytest.raises(Exception):
        exercise_plan()

def test_negative_or_zero_inputs():
    """Test negative or zero inputs"""
    with pytest.raises(ValueError):
        exercise_plan(weight=-2, height=1.83, sex=2, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        exercise_plan(weight=63, height=0, sex=2, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        exercise_plan(weight=63, height=1.83, sex=3, age=27, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        exercise_plan(weight=63, height=1.83, sex=2, age=0, target_weight=65, number_of_days=30)
    with pytest.raises(ValueError):
        exercise_plan(weight=63, height=1.83, sex=2, age=27, target_weight=-65, number_of_days=30)
    with pytest.raises(ValueError):
        exercise_plan(weight=63, height=1.83, sex=2, age=27, target_weight=65, number_of_days=0)
