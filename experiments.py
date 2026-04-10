"""
Synchrocity experiment runner.

Runs a baseline multi-agent swarm simulation and reports
core Synchrocity metrics.
"""

from core import ThirdMindSwarm
from metrics import compute_metrics


def run_baseline(n_agents=10, steps=200):
    swarm = ThirdMindSwarm(n_agents=n_agents)

    for _ in range(steps):
        swarm.step()

    return compute_metrics(swarm.history)


if __name__ == "__main__":
    results = run_baseline()

    print("\n--- Synchrocity Results ---")
    print(f"Individual Variance (IV): {results['individual_variance']:.6f}")
    print(f"Collective Variance (CV): {results['collective_variance']:.6f}")
    print(f"Coherence Ratio (CR): {results['coherence_ratio']:.6f}")
    print(f"Mean Norm: {results['mean_norm']:.6f}")
