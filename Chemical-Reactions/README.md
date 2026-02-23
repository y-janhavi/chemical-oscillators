## Chemical Kinetics: Deterministic & Stochastic Simulations
This folder explores the fascinating world of non-linear chemical dynamics. It contains implementations of classic reaction models, comparing the smooth, predictable nature of Ordinary Differential Equations (ODEs) with the inherent "noise" of Stochastic Simulation Algorithms (SSA).

## Featured Models
I have implemented four cornerstone models of computational chemistry:

4-Reaction Model: A foundational system to understand basic kinetic steps.

Lotka-Volterra: The classic "predator-prey" oscillator applied to chemical concentrations.

Brusselator: A theoretical model for auto-catalytic reactions that demonstrates how systems far from equilibrium can self-organize.

Oregonator: A sophisticated model designed to simulate the complex behavior of the Belousov-Zhabotinsky (BZ) reaction.

Radioactive Decay (A ---> B): The simplest first-order kinetic model. It serves as the baseline for verifying the Gillespie Algorithm against the analytical solution N(t) = N_0 e^{-kt}
