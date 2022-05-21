import numpy as np
import scipy
from matplotlib import pyplot as plt
import Calculus.NumericalRoots as NR

def f(u, v=90, ell=5):
    # Example from https://stackoverflow.com/q/14878110/3015186
    w = np.sqrt(v ** 2 - u ** 2)

    jl = scipy.special.jn(ell, u)
    jl1 = scipy.special.yn(ell - 1, u)
    kl = scipy.special.kn(ell, w)
    kl1 = scipy.special.kn(ell - 1, w)

    return jl / (u * jl1) + kl / (w * kl1)

if __name__ == "__main__":

    r = NR.RootFinder(1, 20, 0.01)
    args = (90, 5)
    roots = r.find(f, *args)
    print("Roots: ", roots)

    # plot results
    u = np.linspace(1, 20, num=600)
    fig, ax = plt.subplots()
    ax.plot(u, f(u, *args))
    ax.scatter(roots, f(np.array(roots), *args), color="r", s=10)
    ax.grid(color="grey", ls="--", lw=0.5)
    plt.show()

