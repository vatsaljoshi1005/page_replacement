def optimal(reference_string,frame_size):
    frames=[]
    page_faults=0
    
    for i,page in enumerate(reference_string):
        if page not in frames:
            page_faults+=1

            if len(frames)<frame_size:
                frames.append(page)
            else:
                future=reference_string[i+1:]
                page_to_remove=None
                farthest_use= -1
                for f in frames:
                    if f not in future:
                        page_to_remove=f
                        break
                    else:
                        next_use=future.index(f)
                        if next_use>farthest_use:
                            farthest_use=next_use
                            page_to_remove=f
                        
                frames.remove(page_to_remove)
                frames.append(page)
    return page_faults