from numpy import array
from operator import mul, add


class ElephantSolver():
    """ Sole class for solving an Elephant problem.\n

        Attributes:\n
        count       -- holds number of elephants in current problem.\n
        weight      -- contains weights of all elephants.\n
        curr_order  -- current order of elephants.\n
        want_order  -- desired order of elephants.\n

        Methods:\n
        parser_prep -- sets up argparse and retreives arguments.\n
        read_data   -- retrieves information from input file.\n
        solution    -- function responsible for finding the solution.\n
        get_sets    -- retrieves cycles from given orders and
        puts then into sets.
    """
    def __init__(self) -> None:
        self.read_data()
        self.solution()

    def read_data(self) -> None:
        """ Reads file line by line and saves the read data.
        """
        # read data, strip newlines and then split into list on ' '
        self.count = int(input())
        self.weight = array([int(w) for w in input().strip().split(' ')])
        self.curr_order = [int(w) - 1 for w in input().strip().split(' ')]
        self.want_order = [int(w) - 1 for w in input().strip().split(' ')]

    def solution(self) -> None:
        """ Later part of algorithm, calls get_sets to get cycles and then
            finds minimas and sums of cycles and with this gets a result.
        """
        sets = self.get_sets()
        # this is fastest way i found,
        # other include two list comprehensions and for loop
        all = array([[sum(self.weight[list(s)]), min(self.weight[list(s)])]
                    for s in sets])
        method1 = list(map(add, all[:, 0], map(mul, [len(s) - 2 for s in sets],
                                               all[:, 1])))
        # even autolint refused to indent this part properly
        method2 = list(map(add, all[:, 0], map(add, all[:, 1],
                    [(len(s) + 1) * min(all[:, 1]) for s in sets])))
        res = sum(list(map(min, method1, method2)))
        print(res)

    def get_sets(self) -> set:
        """ Initial part of algorithm, finds a cycles in the exhanges that
            need to be done and returns the cycles found.
        """
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
        return sets


if __name__ == '__main__':
    ElephantSolver()
