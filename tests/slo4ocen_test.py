from main import ElephantSolver
import sys

""" This test runs rather long, it takes over 22 minutes"""


def test_results(capsys) -> None:
    sys.stdin = open('Data/slo4ocen.in', 'r')
    ElephantSolver()
    captured = capsys.readouterr()
    with open('Data/slo4ocen.out', 'r') as f:
        res = f.readline()
    assert res == captured.out
