from main import ElephantSolver

""" This test runs rather long, arround 53 seconds"""


def test_results(capsys) -> None:
    ElephantSolver(["Data/slo5.in"])
    captured = capsys.readouterr()
    with open("Data/slo5.out", "r") as f:
        res = f.readline()
    assert res == captured.out
