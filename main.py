import csv
from algorithms.fifo import fifo
from algorithms.lru import lru
from algorithms.optimal import optimal
from utils.metrics import compute_metrics
from utils.reference_generator import generate_random_reference
from ml.dataset_generator import generate_dataset

generate_dataset()
def run():
    file=open("data/results.csv","w",newline="")
    writer=csv.writer(file)
    writer.writerow([
    "experiment",
    "reference_string",
    "fifo_faults",
    "lru_faults",
    "optimal_faults"
])
    frame_size=3
    for i in range(10):
        reference_string = generate_random_reference(20,8)
        fifo_faults=fifo(reference_string,frame_size)
        lru_faults=lru(reference_string,frame_size)
        optimal_faults=optimal(reference_string,frame_size)
        writer.writerow([
        i+1,
        reference_string,
        fifo_faults,
        lru_faults,
        optimal_faults
    ])
    file.close()


if __name__ == "__main__":
    run()