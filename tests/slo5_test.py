from main import ElephantSolver
import sys

""" This test runs longer than most tests, arround 53 seconds"""


def test_results(capsys) -> None:
    sys.stdin = open('Data/slo5.in', 'r')
    ElephantSolver()
    captured = capsys.readouterr()
    with open('Data/slo5.out', 'r') as f:
        res = f.readline()
    assert res == captured.out
