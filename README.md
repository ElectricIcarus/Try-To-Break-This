# Try-To-Break-This

A minimal, falsifiable multi-agent system for testing **Synchrocity**:

> **bounded individual variability with stable collective coherence under disturbance**

This repository is designed to be run, challenged, stressed, and refined.

It is not a pitch.
It is a test.

---

## Synchrocity

**Synchrocity** is the dynamical regime in a multi-agent system where:

- individual agents maintain **bounded, non-identical trajectories**
- the collective state converges to and remains within a **stable attractor band**
- the system exhibits **continuous re-synchronization** under perturbation
- coherence emerges **without collapse into uniformity**

Plainly:

- everyone stays themselves
- the group stays together
- disturbances are absorbed rather than causing collapse

---

## What This Repository Measures

The system reports the following metrics:

- **IV (Individual Variance)**  
  Measures bounded diversity across agent trajectories.

- **CV (Collective Variance)**  
  Measures stability of the collective state over time.

- **CR (Coherence Ratio)**  
  Defined as Mean(IV) / CV.  
  High values indicate preserved individuality with collective coherence.

- **RT (Recovery Time)**  
  Measures how quickly the system returns to its attractor band after disturbance.

- **AS (Attractor Stability)**  
  Measures whether the collective band remains bounded and non-diverging.

---

## Synchrocity Conditions

Synchrocity is present only when all of the following hold:

- IV remains **greater than zero and bounded**
- CV remains **low and stable**
- CR remains **significantly greater than 1**
- RT is **finite and repeatable**
- AS remains **bounded over the observation window**

---

## Falsification Conditions

Synchrocity fails if any of the following occur:

- agents converge to near-identical states
- collective variance diverges or drifts unbounded
- recovery fails after perturbation
- coherence is only achieved by suppressing individuality

---

## Minimal Reproducible Setup

Baseline system:

- 10 agents
- 3D state vector per agent
- slight parameter heterogeneity
- weak diffusive coupling
- low stochastic noise
- perturbation-capable run loop

Expected outcome:

- distinct individual fluctuations
- a tight collective attractor band
- recovery after disturbance without collapse or rigid sameness

---

## Stress Tests

This repository is meant to be challenged.

### 1. Agent Removal
Remove 30–50% of agents mid-run.  
Question: does the remaining swarm re-stabilize?

### 2. Malicious / Noisy Agent
Inject one or more destabilizing agents.  
Question: does the system absorb, isolate, or collapse?

### 3. Communication Delay / Gradient
Introduce lag or uneven coupling.  
Question: does coherence persist across the network?

### 4. Increased Heterogeneity
Increase parameter spread between agents.  
Question: does the attractor still hold?

---

## Run It

```bash
pip install -r requirements.txt
python experiments.py
---

## Interpretation Note

If the system maintains high CR, bounded AS, and finite RT across stress tests,
this suggests the presence of a stable coherence regime with preserved individuality.

If not, the hypothesis does not hold under those conditions.

No further claims are implied.
