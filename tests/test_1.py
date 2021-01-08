import pickle
import hashlib

def get_pickle(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
 
    
def test1():
    t = get_pickle('q8.pickle')
    r = t.shape
    assert ((577, 17)==r)
    # print(r)

def test2():
    t = get_pickle('q1b.pickle')
    r = t[52]
    z = 'Kolkata'
    assert z == r
    # print(r)


def test3():
    t = get_pickle('q2b.pickle')
    r = type(t)
    g=['df','dgrd']
    assert type(t) == type(g)
    # print(g)


def test4():
    t = get_pickle('q3b.pickle')
    r = t[200]
    z = 'SL Malinga'
    assert z == r
    # print(r)

def test5():
    t = get_pickle('q4b.pickle')
    r = t[540]
    z = 2016
    assert z == r

    
def test7():
    t = get_pickle('q6b.pickle')
    r = type(t)
    g=['df','dgrd']
    assert type(t) == type(g)
    # print(g)


def test8():
    t = get_pickle('q7b.pickle')
    r = t[222]
    z = 'Delhi Daredevils'
    assert z == r
    # print(r)


