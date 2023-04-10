# SIR BOILERPLATE CODE FROM CHATGPT
import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Load data from Kaggle Ebola dataset
df = pd.read_csv("sir-model/data-sets/ebola_2014_2016_clean.csv")
# Define initial conditions
I0 = df["Cumulative_cases"].iloc[0]
R0 = df["Cumulative_deaths"].iloc[0]
S0 = 1 - I0 - R0
y0 = [S0, I0, R0]


# Define time points
t = np.linspace(0, len(df)-1, len(df))

# Define SIR model
def SIR(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Define model parameters
N = 1  # Total population size
beta = 0.5  # Infection rate
gamma = 0.1  # Recovery rate

# Integrate SIR equations over time
sol = odeint(SIR, y0, t, args=(N, beta, gamma))

# Plot results
plt.plot(t, sol[:, 0], label="Susceptible")
plt.plot(t, sol[:, 1], label="Infected")
plt.plot(t, sol[:, 2], label="Recovered")
plt.xlabel("Days")
plt.ylabel("Fraction of population")
plt.title("SIR Model for Ebola Outbreak")
plt.legend()
plt.show()
