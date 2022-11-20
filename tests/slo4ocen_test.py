from main import ElephantSolver

""" This test runs rather long, it takes over 22 minutes"""


def test_results(capsys) -> None:
    ElephantSolver(["Data/slo4ocen.in"])
    captured = capsys.readouterr()
    with open("Data/slo4ocen.out", "r") as f:
        res = f.readline()
    assert res == captured.out
