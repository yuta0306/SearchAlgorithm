from typing import Dict, Union
import sys

__all__ = [
    'BFS',
]

class BFS:
    def __init__(self, graph: Dict[Union[str, int], Union[str, int]],
                start: Union[str, int]=None, goal: Union[str, int]=None) -> None:
        self.graph = graph
        self.OPEN = list()
        self.CLOSED = list()
        self.PTR = dict()
        self.start = start
        self.goal = goal

    def search(self, start: Union[str, int]=None, goal: Union[str, int]=None, verbose: int=0):
        start = start if start is not None else self.start
        goal = goal if goal is not None else self.goal
        assert start is not None and goal is not None

        self.OPEN.append(start)
        count = 0
        while len(self.OPEN) > 0:
            count += 1
            if goal in self.OPEN:
                break

            n = self.OPEN.pop(0)
            if verbose < 0:
                sys.stdout.write(f'STEP : {count}\n')
                sys.stdout.write(f'Current Node ===> {n}\n')
            children = [
                child for child in self.graph[n] if child not in self.CLOSED
            ]
            if verbose < 0:
                if len(children) > 0:
                    sys.stdout.write(f'Next Node ======> {" ".join(children)}\n')
                else:
                    sys.stdout.write(f'Next Node ======> {" ".join(self.OPEN[0])}\n')
            self.CLOSED.append(n)
            self.OPEN.extend(children)
            self.PTR[n] = children

        route = self._get_route(start, goal)

        return route

    def _get_route(self, start, goal):
        assert len(self.PTR) > 0
        history = list()
        node = [k for k, v in self.PTR.items() if goal in v]
        assert len(node) > 0
        node = node[0]
        history.append(node)

        while node != start:
            node = [k for k, v in self.PTR.items() if node in v][0]
            history.append(node)

        return history