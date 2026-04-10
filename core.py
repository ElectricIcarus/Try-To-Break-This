"""
Core multi-agent dynamics for Synchrocity.

Defines:
- ThirdMindAgent: individual state evolution
- ThirdMindSwarm: coupled multi-agent system

Implements heterogeneous agents with weak diffusive coupling.
"""

import numpy as np
from typing import List

class ThirdMindAgent:
    def __init__(self, id: int, eps: float = 0.05, kq: float = 0.2):
        self.id = id
        self.state = np.random.randn(3) * 5.0
        self.eps = eps
        self.kq = kq

    def step(self, coupling_influence: np.ndarray, dt: float = 0.05):
        x, y, z = self.state

        dx = 10*(y - x) - self.eps * (x+y+z)/3 + self.kq * np.sin(y - x) * np.cos(z)
        dy = x*(28 - z) - y - self.eps * (x+y+z)/3 + self.kq * np.sin(x - z) * np.cos(y)
        dz = x*y - (8/3)*z - self.eps * (x+y+z)/3 + self.kq * np.sin(z - x) * np.cos(y)

        # IMPORTANT: coupling is applied here (this makes it a real swarm)
        self.state += (np.array([dx, dy, dz]) + coupling_influence) * dt

        return self.state


class ThirdMindSwarm:
    def __init__(self, n_agents: int = 10, base_coupling: float = 0.01):
        self.agents: List[ThirdMindAgent] = []
        self.n = n_agents

        for i in range(n_agents):
            eps = 0.05 + np.random.uniform(-0.01, 0.01)
            kq = 0.2 + np.random.uniform(-0.05, 0.05)
            self.agents.append(ThirdMindAgent(i, eps, kq))

        self.coupling = base_coupling
        self.history = []

    def step(self):
        influences = np.zeros((self.n, 3))

        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    influences[i] += self.coupling * (self.agents[j].state - self.agents[i].state)

        new_states = []

        for i, agent in enumerate(self.agents):
            new_states.append(agent.step(influences[i]))

        self.history.append([a.state.copy() for a in self.agents])

        return np.array(new_states)
