def lru(reference_string,frame_size):

    frames=[]
    page_faults=0
    last_used={}
    
    for i, page in enumerate(reference_string):
        if page not in frames:
            page_faults+=1
            if len(frames)<frame_size:
                frames.append(page)
            else:
                #find least recently used page
                lru_page=min(frames,key=lambda x: last_used[x]) #find pg whose last used time is min
                frames.remove(lru_page)
                frames.append(page)
        last_used[page]=i
    return page_faults
