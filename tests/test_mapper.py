from datamaker_faker import Field


def test_no_mapper():
    s1 = Field("sex")
    assert s1.generate()[0] in ["male", "female"]


def test_mapper():
    s2 = Field("sex", mapper={"male": "m", "female": "f"})
    assert s2.generate()[0] in ["f", "m"]
