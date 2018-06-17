import numpy
from matplotlib import pyplot as plt
from scipy.signal import freqz


def main():
    αs = [0.05, 0.1, 0.2, 0.5, 0.7, 0.9, 0.95]

    for α in αs:
        w, h = freqz(b=[α], a=[1, 1 - α])
        plt.ylim(0, 1)
        plt.plot(w, numpy.abs(h))
        plt.show()


if __name__ == '__main__':
    main()
