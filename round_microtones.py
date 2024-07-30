import numpy as np

TARGETS = [-100, -75, -50, -25, 0, 25, 50, 75, 100]

D_MIDI = 62
A_MIDI = 69
A_HZ = 440


def midi_to_hz(midi):
    return A_HZ * 2 ** ((midi - A_MIDI) / 12)


def hz_to_midi(f):
    return A_MIDI + 12 * np.log2(f / A_HZ)


D_HZ = midi_to_hz(D_MIDI)


def round_to_nearest(cents, targets=tuple(TARGETS)):
    rounded = []
    for cent in cents:
        nearest = min(targets, key=lambda x: abs(x - cent))
        rounded.append(nearest)
    return rounded


def get_deviation(cents):
    return cents - np.round(cents)


def main():
    overtones = np.arange(1, 36, 1) * midi_to_hz(0)
    cents = hz_to_midi(overtones)
    deviation = get_deviation(cents) * 100
    rounded_deviation = round_to_nearest(deviation)

    cents = [c % 12 for c in cents]

    values = list(
        zip(
            range(1, 36),
            (float(c.round(2)) for c in cents),
            rounded_deviation,
            (float(d.round(2)) for d in deviation),
        )
    )

    # values = [v for v in values if v[2] != 0]

    for v in values:
        print(v)


if __name__ == "__main__":
    main()
