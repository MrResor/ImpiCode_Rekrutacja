from main import ElephantSolver

""" This file contains all shorter test that can be done
"""


# Had those test written done in for loop form, but did not like the result
# because they were all bundled up together
def test_slo1(capsys) -> None:
    ElephantSolver(["Data/slo1.in"])
    captured = capsys.readouterr()
    with open("Data/slo1.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo1ocen(capsys) -> None:
    ElephantSolver(["Data/slo1ocen.in"])
    captured = capsys.readouterr()
    with open("Data/slo1ocen.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo2(capsys) -> None:
    ElephantSolver(["Data/slo2.in"])
    captured = capsys.readouterr()
    with open("Data/slo2.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo2ocen(capsys) -> None:
    ElephantSolver(["Data/slo2ocen.in"])
    captured = capsys.readouterr()
    with open("Data/slo2ocen.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo3(capsys) -> None:
    ElephantSolver(["Data/slo3.in"])
    captured = capsys.readouterr()
    with open("Data/slo3.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo3ocen(capsys) -> None:
    ElephantSolver(["Data/slo3ocen.in"])
    captured = capsys.readouterr()
    with open("Data/slo3ocen.out", "r") as f:
        res = f.readline()
    assert res == captured.out


def test_slo4(capsys) -> None:
    ElephantSolver(["Data/slo4.in"])
    captured = capsys.readouterr()
    with open("Data/slo4.out", "r") as f:
        res = f.readline()
    assert res == captured.out
