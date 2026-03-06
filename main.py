from algorithms.fifo import fifo
from algorithms.lru import lru
from algorithms.optimal import optimal
from utils.metrics import compute_metrics
from utils.reference_generator import generate_random_reference

def run():
    reference_string = generate_random_reference(20,8)
    frame_size=3
    fifo_faults=fifo(reference_string,frame_size)
    lru_faults=lru(reference_string,frame_size)
    optimal_faults=optimal(reference_string,frame_size)
    fifo_metrics = compute_metrics(fifo_faults, len(reference_string))
    lru_metrics = compute_metrics(lru_faults, len(reference_string))
    optimal_metrics = compute_metrics(optimal_faults, len(reference_string))
    print("Reference String:", reference_string)
    print("Frame Size:", frame_size)
    print("FIFO:", fifo_metrics)
    print("LRU:", lru_metrics)
    print("Optimal:", optimal_metrics)


if __name__ == "__main__":
    run()