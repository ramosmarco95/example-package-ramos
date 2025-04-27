from src.example_package_ramos import example

def test_add_one():
    assert example.add_one(1) == 2
    assert example.add_one(2) == 3
    assert example.add_one(-1) == 0
    assert example.add_one(0) == 1