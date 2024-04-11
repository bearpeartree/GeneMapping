def main():
    #Speichern der Daten aus der Textfile
    #A B C 349
    #A B c 128
    #A b C 5
    name_file = input("Please enter the name of your textfile: ")
    my_gametes = extract_data(name_file);


    gametes_and_counts = {}


#And save it into dict
def save_into_dict(gametes_list):
    return None

#Read the file
#Return the list with each line
def extract_data(filename):
    gametes = []
    with open(filename, "r") as file:
        for line in file:
            gametes.append(line.strip())

    return gametes


if __name__ == "__main__":
    main()