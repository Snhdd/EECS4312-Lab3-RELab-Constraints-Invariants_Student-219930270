import pytest
from src.dispense import DispenseEvent, invariant_holds

def test_negative_dose():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Aspirin", -5, 1)

def test_invalid_quantity():
    with pytest.raises(ValueError):
        DispenseEvent("P1", "Aspirin", 100, 0)

def test_duplicate_dispense():
    e1 = DispenseEvent("P1", "Aspirin", 100, 1)
    e2 = DispenseEvent("P1", "Aspirin", 200, 1)
    assert invariant_holds([e1], e2) == False
