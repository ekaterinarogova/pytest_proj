from utils.dicts import get_val

def test_get_val():
    assert get_val({1:'один', 2: 'два', 3: 'три'}, 2) == 'два'
    assert get_val({1:'один', 2: 'два', 3: 'три'}, 0) == 'git'
    assert get_val({1:'один', 2: 'два', 3: 'три'}, 'десять', 'нет такого значения') == 'нет такого значения'