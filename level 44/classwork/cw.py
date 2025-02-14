def count_by(x, n):
    arr = []
    for i in range (1, n + 1):
        arr.append(i*x)
    return arr



def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    counter = 1
    for i in range(human_years):
        if counter == 1:
            cat += 15
            dog += 15
            counter += 1
            continue 
        cat += 5
        dog += 5
        
        return[human_years,cat,dog]