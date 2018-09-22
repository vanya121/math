from dna import reverse_complement


def test_example1():
    assert reverse_complement('AAAACCCGGT') == 'ACCGGGTTTT'
