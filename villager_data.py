"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    species = set()
    data = open("villagers.csv")
    for line in data:
        line = line.split("|")
        species.add(line[1])

    

    # TODO: replace this with your code

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """
    
    
    data = open(filename)
    villagers = []
    for line in data:
        line = line.split("|")
        if line[1] == search_string:
            villagers.append(line[0])
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    data = open(filename)
    villager_list = [[],[],[],[],[],[]]
    #set = {"this","is","set"}
    #dictt = {"name": "chris", "name": "Joann"}
    for line in data:
        line = line.split("|")
        if line[3] == "Education":
            villager_list[0].append(line[0])
        elif line[3] == "Fashion":
            villager_list[1].append(line[0])
        elif line[3] == "Fitness":
            villager_list[2].append(line[0])
        elif line[3] == "Nature":
            villager_list[3].append(line[0])
        elif line[3] == "Music":
            villager_list[4].append(line[0])
        elif line[3] == "Play":
            villager_list[5].append(line[0])
        
        
                

    return villager_list
    

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    data = open(filename)
    all_data = []
    

    villagers = []
    for line in data:
        line = line.split("|")
        new_tuple = tuple(line)
        all_data.append(new_tuple)
    

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    motto = ""
    data = open(filename)    
    for line in data:
        line = line.split("|")
        if line[0] == villager_name:
            motto = line[4]
    return motto
    
    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded = set()
    persons_mind = ""
    data = open(filename)    
    for line in data:
        line = line.split("|")
        if line[0] == villager_name:
            persons_mind = line[2]
    print(persons_mind)
    data.close()

    data = open(filename)
    for line in data:
        line = line.split("|")
        #print(line[2])
        if line[2] == persons_mind:
            print(line[0])
            likeminded.add(line[0])
    

    # TODO: replace this with your code
    return likeminded


#print(all_species("villagers.csv"))
#print(get_villagers_by_species("villagers.csv", "Bear"))
#print(all_names_by_hobby("villagers.csv"))
#print(all_data("villagers.csv"))
#print(find_motto("villagers.csv","Jay"))
print(find_likeminded_villagers("villagers.csv", "Jay"))