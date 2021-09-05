from basicmath import divide, add, sortlist

def test_divide():
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5

# from basicmath import add

def test_add():
    assert add(1, 3) == 4


#from basicmath import sortlist

def test_srt():
    l = [15, 2, 3, 7, 6, 0]
    l_sorted = [0, 2, 3, 6, 7, 15]

    assert sortlist(l) == l_sorted
