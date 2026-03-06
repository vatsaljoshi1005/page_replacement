def fifo(reference_string, frame_size):
    
    frames=[] #initially memory is empty
    page_faults=0
    queue=[]
    #loop through reference string
    for page in reference_string:
        #check for hit
        if page in frames:
            continue

        #else miss
        page_faults+=1
        #add till frame is not full
        if len(frames)<frame_size:
            frames.append(page)
            queue.append(page)
        #else replace first pg from queue as it is fifo
        else:
            removed=queue.pop(0)
            frames.remove(removed)
            #append current page in frame and queue
            frames.append(page)
            queue.append(page)

    return page_faults
