"""
Reads the contents of a file and processes the data to extract animal names.
Parameter
    - fileName: the name of the file
Return
    - list: all the extracted animal names 
"""


def readFile(fileName):
    f = open(fileName, 'r')
    list = f.read().splitlines()
    return list


"""
Removing uppercase letters, white space, and punctuation within any animal name,
and convert the names to lowercase.
Parameters:
    - list: the list of string
Returns:
    - list: the list of extracted string
"""


def refineData(list):
    import string
    # disregard blank spaces and punctuation marks, and converting all letters to lowercase
    list = [animal.strip()
            .lower()
            .translate(str.maketrans('', '', string.punctuation)) for animal in list]
    return list


"""
Find the alphabetical-ordered string in the list and return them in the new list.
Parameters:
    -list: the list of words
Return:
    -count: the number of alphabetical-ordered string
"""


def findAlphabeticalWords(fileName):
    # read file
    animal_list = readFile(fileName)
    # refind the data
    animal_list = refineData(animal_list)

    count = 0
    for animal in animal_list:
        temp = ''.join(sorted(animal))
        if temp != animal:
            continue
        else:
            count += 1

    return count


# print("# of word with alphabeical letter =",findAlphabeticalWords("animals.txt"))
