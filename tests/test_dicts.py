from utils.dicts import get_val
import pytest

@pytest.fixture
def coll():
    return {1:'один', 2: 'два', 3: 'три'}

def test_get_val(coll):
    assert get_val(coll, 2) == 'два'
    assert get_val(coll, 0) == 'git'
    assert get_val(coll, 'десять', 'нет такого значения') == 'нет такого значения'