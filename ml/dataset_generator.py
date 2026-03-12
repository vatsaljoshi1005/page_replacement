import csv
from utils.reference_generator import generate_random_reference

def generate_dataset():
    file=open("data/ml_dataset.csv","w",newline="")
    writer=csv.writer(file)
    writer.writerow([
        "frame1",
        "frame2",
        "frame3",
        "next_page",
        "evict_page"
    ])
    #when we dont want to assign loop variable , just wants to run this loop we use _ 
    for _ in range(500):
        reference_string=generate_random_reference(30,10)
        frames=[]
        for i, page in enumerate(reference_string):
            if page not in frames:
                if len(frames)<3:
                    frames.append(page)
                else:
                    future=reference_string[i+1:]
                    victim=None
                    farthest=-1
                    for f in frames:
                        if f not in future:
                            victim=f
                            break
                        else:
                            next_use=future.index(f)
                            if next_use>farthest:
                                farthest=next_use
                                victim=f
                    writer.writerow([
                        frames[0],
                        frames[1],
                        frames[2],
                        page,
                        victim
                    ])

                    frames.remove(victim)
                    frames.append(page)

    file.close()