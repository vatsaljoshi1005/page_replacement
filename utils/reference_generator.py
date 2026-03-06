import random
#to generate random page reference string
def generate_random_reference(length=20, max_page=10):
    
    reference = []
    
    for _ in range(length):
        page = random.randint(0, max_page)
        reference.append(page)
        
    return reference

def generate_locality_reference(length=20, max_page=10, locality_size=3):
    
    reference = []
    current_base = random.randint(0, max_page)
    
    for _ in range(length):
        
        if random.random() < 0.8:
            page = random.randint(current_base, min(current_base+locality_size, max_page))
        else:
            page = random.randint(0, max_page)
            
        reference.append(page)
    
    return reference