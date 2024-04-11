def main():
    #Speichern der Daten aus der Textfile
    #A B C 349
    #A B c 128
    #A b C 5
    name_file = input("Please enter the name of your textfile: ")
    my_gametes = extract_data(name_file);
    gametes_and_counts = save_into_dict(my_gametes)
    print(gametes_and_counts)


#And save it into dict
def save_into_dict(gametes_list):
    gametes_dict = {}
    for gamete in gametes_list:
        gamete_count = separate_data(gamete)
        gametes_dict[gamete_count[0]] = gamete_count[1]

    return gametes_dict


#Read the file
#Return the list with each line
def extract_data(filename):
    gametes = []
    with open(filename, "r") as file:
        for line in file:
            gametes.append(line.strip())

    return gametes


def separate_data(some_string):
    g_c = []
    for i in range(0, len(some_string)):
        if some_string[i].isnumeric():
            g_c.append(some_string[0:i].strip())
            g_c.append(int(some_string[i:len(some_string)].strip()))
            return g_c;


if __name__ == "__main__":
    main()