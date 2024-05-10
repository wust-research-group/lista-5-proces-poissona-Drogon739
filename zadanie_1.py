import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def generate_poisson_process(lambd, T):
    N = poisson.rvs(mu=lambd * T)
    event_times = np.sort(np.random.uniform(low=0, high=T, size=N))
    return event_times

def plot_poisson_process(event_times, T):
    N_t = np.arange(1, len(event_times) + 1)
    
    times = np.concatenate(([0], event_times, [T]))
    counts = np.concatenate(([0], N_t, [N_t[-1]] if N_t.size > 0 else [0]))
    
    plt.figure(figsize=(10, 4))
    plt.step(times, counts, where='post', linewidth=2, label='N(t)')
    plt.xlabel('Czas')
    plt.ylabel('Liczba wystąpień')
    plt.title('Poisson Process Trajectory')
    plt.grid(True)
    plt.ylim(bottom=0)
    plt.xlim(0, T)
    plt.show()

T = 4
lambd = 2

event_times = generate_poisson_process(lambd, T)
plot_poisson_process(event_times, T)
