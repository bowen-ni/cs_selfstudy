#remove nexted list using recursion
def flatten(l):
    flattened_list = []
    for i in l:
        if isinstance(i,str):
            flattened_list.append(i)
        flatten(i)

    return(flattened_list)

planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))