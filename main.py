from decorators import file_open_err
from numpy import array
from operator import mul, add


class ElephantSolver:
    def __init__(self) -> None:
        self.read_data()
        self.solution()

    @file_open_err
    def read_data(self) -> None:
        with open("Data/slo2.in", "r") as f:
            self.count = int(f.readline())
            self.weight = array([int(w) for w in
                                f.readline().strip().split(' ')])
            self.curr_order = [int(w) - 1 for w in
                               f.readline().strip().split(' ')]
            self.want_order = [int(w) - 1 for w in
                               f.readline().strip().split(' ')]

    def solution(self) -> None:
        p = [self.curr_order[self.want_order.index(i)]
             for i in range(self.count)]
        visited = [False for _ in p]
        sets = set()
        for i in range(self.count):
            if not visited[i]:
                tmp = set()
                x = i
                while not visited[x]:
                    visited[x] = True
                    tmp.add(x)
                    x = p[x]
                sets.add(frozenset(tmp))
        sums = [sum(self.weight[list(s)]) for s in sets]
        minimas = [min(self.weight[list(s)]) for s in sets]
        # TODO this code may proof faster for longer arrays
        # sums = full((1, len(sets)), 0)
        # minimas = full((1, len(sets)), inf)
        # for i, s in enumerate(sets):
        #     for el in s:
        #         sums[0, i] += self.weight[el]
        #         minimas[0, i] = min(minimas[0, i], self.weight[el])
        method1 = list(map(add, sums, map(mul, [len(s) - 2 for s in sets],
                                          minimas)))
        mini = min(minimas)
        method2 = list(map(add, sums, map(add, minimas, [(len(s) + 1) * mini
                                                         for s in sets])))
        print([(len(s) + 1) * min(minimas) for s in sets])
        print(method1, method2)
        res = sum(list(map(min, method1, method2)))
        print(res)


if __name__ == '__main__':
    app = ElephantSolver()
