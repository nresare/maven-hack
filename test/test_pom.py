
from maven_hack import pom


def test_pom():
    p = pom.Pom("apache-3.pom")
    print p.packaging
    assert p.packaging == "pom"