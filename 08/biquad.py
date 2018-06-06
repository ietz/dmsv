from matplotlib import pyplot as plt


class Biquad:
    def __init__(self, a1, a2, b0, b1, b2):
        self.a1, self.a2 = a1, a2
        self.b0, self.b1, self.b2 = b0, b1, b2
        self.w1, self.w2 = 0, 0

    def process(self, x):
        w0 = x + -self.a1*self.w1 + -self.a2*self.w2
        y = self.b0*w0 + self.b1*self.w1 + self.b2*self.w2

        self.w1, self.w2 = w0, self.w1

        return y


def aufgabe(nr, biquad):
    response = impulse_response(biquad)
    print(response)

    plt.title("Aufgabe {}".format(nr))
    plt.plot(response)
    plt.show()


def impulse_response(biquad):
    ys = [biquad.process(1)]
    for i in range(39):
        ys.append(biquad.process(0))
    return ys


if __name__ == '__main__':
    aufgabe(1, Biquad(-3/2, -1, 1/2, -1, 0))
    aufgabe(2, Biquad(6, 9, 3, 9, 0))
