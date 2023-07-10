import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.style.use("kaihoplots.presentation")
    fig, ax = plt.subplots()
    
    x = np.linspace(0, 2*np.pi, 100)
    for i in range(8):
        ax.plot(x, np.sin(x + i*np.pi/4))
    fig.savefig("test.png")

if __name__ == '__main__':
    main()
