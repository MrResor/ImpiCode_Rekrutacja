from main import ElephantSolver
import sys

""" This file contains all shorter test that can be done
"""


def check(capsys, name):
    sys.stdin = open('Data/' + name + '.in', 'r')
    ElephantSolver()
    captured = capsys.readouterr()
    with open('Data/' + name + '.out', 'r') as f:
        res = f.readline()
    assert res == captured.out


# Had those test written done in for loop form, but did not like the result
# because they were all bundled up together
def test_slo1(capsys) -> None:
    check(capsys, 'slo1')


def test_slo1ocen(capsys) -> None:
    check(capsys, 'slo1ocen')


def test_slo2(capsys) -> None:
    check(capsys, 'slo2')


def test_slo2ocen(capsys) -> None:
    check(capsys, 'slo2ocen')


def test_slo3(capsys) -> None:
    check(capsys, 'slo3')


def test_slo3ocen(capsys) -> None:
    check(capsys, 'slo3ocen')


def test_slo4(capsys) -> None:
    check(capsys, 'slo4')
