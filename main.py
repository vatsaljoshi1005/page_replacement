from algorithms.fifo import fifo
from algorithms.lru import lru
from algorithms.optimal import optimal

from utils.reference_generator import generate_random_reference

from ml.ml_policy import ml_replace

import matplotlib.pyplot as plt


def optimal_victim(frames, reference_string, index):

    future = reference_string[index+1:]

    victim = None
    farthest = -1

    for f in frames:

        if f not in future:
            victim = f
            break

        else:
            next_use = future.index(f)

            if next_use > farthest:
                farthest = next_use
                victim = f

    return victim


def ml_accuracy_experiment():

    frame_size = 3
    experiments = 100

    correct_predictions = 0
    total_predictions = 0

    for _ in range(experiments):

        reference_string = generate_random_reference(30, 10)
        frames = []

        for i, page in enumerate(reference_string):

            if page not in frames:

                if len(frames) < frame_size:
                    frames.append(page)

                else:

                    # optimal decision
                    opt_victim = optimal_victim(frames, reference_string, i)

                    # ML decision
                    ml_victim = ml_replace(frames, page)

                    # safety check
                    if ml_victim not in frames:
                        ml_victim = frames[0]

                    if ml_victim == opt_victim:
                        correct_predictions += 1

                    total_predictions += 1

                    frames.remove(opt_victim)
                    frames.append(page)

    accuracy = correct_predictions / total_predictions

    print("ML Prediction Accuracy:", accuracy)

    # Plot graph
    plt.bar(["ML Accuracy"], [accuracy])

    plt.ylabel("Accuracy")
    plt.title("ML Replacement Prediction Accuracy")

    plt.ylim(0,1)

    plt.savefig("results_ml_accuracy.png")

    plt.show()


if __name__ == "__main__":
    ml_accuracy_experiment()