"""Cellular Automata pattern."""
from patterns.base.agent_base import AgentBase

class CellularAutomataAgent(AgentBase):
    """Grid-based agents with local interactions for spatial coordination."""
    def __init__(self, config):
        super().__init__(config)
        self.grid_size = config.get("grid_size", 10)
        self.grid = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]

    def run(self, input_data):
        self._update_grid()
        return f"Grid updated: {self.grid[0][:3]}..."

    def _update_grid(self):
        # Simple cellular automaton rule
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                neighbors = self._count_neighbors(i, j)
                self.grid[i][j] = 1 if neighbors == 3 else 0

    def _count_neighbors(self, i, j):
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni, nj = i + di, j + dj
                if 0 <= ni < self.grid_size and 0 <= nj < self.grid_size:
                    count += self.grid[ni][nj]
        return count

    def get_config(self):
        return self.config
