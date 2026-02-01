import pandas as pd

from src.data import load_demo_data, INDICATORS
from src.matrix import build_association_matrix


def test_matrix_shape_correctness():
    observations, events, impact_links = load_demo_data()
    indicators = sorted(INDICATORS.keys())
    m = build_association_matrix(events=events, impact_links=impact_links, indicators=indicators)

    assert m.shape == (len(events), len(indicators))
    assert list(m.index) == events["event_id"].tolist()
    assert list(m.columns) == indicators
