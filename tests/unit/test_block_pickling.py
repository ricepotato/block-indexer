import pickle


def test_load_block_pickle():
    with open("./tests/data/block_121681225.pickle", "rb") as f:
        obj = pickle.loads(f.read())
    assert obj
