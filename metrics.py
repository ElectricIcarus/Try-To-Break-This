"""
Synchrocity metric calculations.

Provides:
- IV (Individual Variance)
- CV (Collective Variance)
- CR (Coherence Ratio)

Used to evaluate whether the system exhibits stable collective coherence with preserved individuality.
"""

import numpy as np
from typing import List

def compute_metrics(states_history: List[np.ndarray], window: int = 50):
    """Returns IV, CV, CR, and mean norm over the final observation window."""
    norms = np.array([[np.linalg.norm(s) for s in step] for step in states_history])

    if len(norms) < window:
        window = len(norms)

    # Individual Variance (average variance across agents over final window)
    iv = np.mean(np.var(norms[-window:], axis=0))

    # Collective Variance (variance of collective mean norm over final window)
    collective_mean = np.mean(norms, axis=1)
    cv = np.var(collective_mean[-window:])

    # Coherence Ratio
    cr = iv / (cv + 1e-8) if cv > 0 else float("inf")

    return {
        "individual_variance": iv,
        "collective_variance": cv,
        "coherence_ratio": cr,
        "mean_norm": np.mean(collective_mean[-window:])
    }
