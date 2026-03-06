def compute_metrics(page_faults, total_references):

    hits = total_references - page_faults
    hit_ratio = hits / total_references
    fault_ratio = page_faults / total_references

    return {
        "faults": page_faults,
        "hits": hits,
        "hit_ratio": hit_ratio,
        "fault_ratio": fault_ratio
    }