"""
Synchrocity Experiment Runner

Runs a multi-agent system and evaluates whether it reaches
a stable collective coherence while preserving individual variation.
"""

import numpy as np
from core import Agent
from metrics import compute_metrics

def run_experiment(num_agents=10, steps=500, dim=3, seed=42):
    np.random.seed(seed)

    agents = [Agent(dim) for _ in range(num_agents)]
    history = []

    for _ in range(steps):
        states = np.array([agent.state for agent in agents])
        mean_state = np.mean(states, axis=0)

        new_states = []
        for agent in agents:
            new_states.append(agent.update(mean_state))

        history.append(new_states)

    metrics = compute_metrics(history)

    return metrics


if __name__ == "__main__":
    results = run_experiment()

    print("\n--- Synchrocity Results ---")
    print(f"Individual Variance (IV): {results['individual_variance']:.4f}")
    print(f"Collective Variance (CV): {results['collective_variance']:.4f}")
    print(f"Coherence Ratio (CR): {results['coherence_ratio']:.4f}")
    print(f"Mean Norm: {results['mean_norm']:.4f}")
