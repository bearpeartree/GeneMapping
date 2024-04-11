from main import extract_data
from main import separate_data

def test_extract_data():
    file_name = "../ExampleFiles/GameteExample1.txt"
    out_gametes = extract_data(file_name)
    assert out_gametes == ["A B C 349",
                            "A B c 128",
                            "A b C 5",
                            "A b c 114",
                            "a B C 116",
                            "a B c 4",
                            "a b C 124",
                            "a b c 360"]


def test_separate_data():
    some_data = "A B C 349"
    assert separate_data(some_data) == ["A B C", 349]


def test_separate_data_less_genes():
    some_data = "gc vg 28 "
    assert separate_data(some_data) == ["gc vg", 28]