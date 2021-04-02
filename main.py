# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import Union, List
import readme_block
import os


def split(file_name: str) -> List[str]:
    blocks = []
    text = get_text(file_name)

    prev_c = ''
    block = ''
    for c in text:
        if c == '\n':
            if prev_c == '\n':
                blocks.append(block)
                block = ''
                prev_c = ''
            else:
                prev_c = c
        else:
            if prev_c == '\n' and block != '':
                block += prev_c
            block += c
            prev_c = c
    if block != '':
        blocks.append(block)
    return blocks


def create_readme(questions: List[str], assignment: str) -> str:
    result = ""

    # Create the beginning of the readme
    result += "Programming Assignment: "
    result += assignment
    result += '\n\n'

    result += "PLEASE REMEMBER NOT TO INCLUDE YOUR NAME " \
              "(OR LATER IN THE COURSE, YOUR PARTNER'S NAME)" \
              "\nANYWHERE IN THIS SUBMISSION."
    result += '\n\n'

    next_question = "Approximate number of hours to complete this assignment"
    result += create_block(next_question)
    result += '\n\n'

    result += "Number of hours:"
    result += '\n\n'

    # Add in custom questions
    for question in questions:
        if question[0] == '>':
            for c in question[1:]:
                if c == '\n':
                    result += '\n'
                if c != '  ':
                    result += c
            result += '\n'
        else:
            result += '\n'
            result += create_block(question)
        result += '\n\n'

    next_question = "Did you receive help from classmates, past students," \
                    " or anyone else? If so, please list their names.  " \
                    "(\"A Sunday lab TA\" or \"Office hours on Thursday\" " \
                    "is ok if you don't know their name.)"
    result += create_block(next_question)
    result += '\n\n'

    result += "Yes or No?"
    result += '\n\n\n'

    next_question = "Did you encounter any serious problems? If so, please describe."
    result += create_block(next_question)
    result += '\n\n'

    result += "Yes or No?"
    result += '\n\n\n'

    next_question = "List any other comments here."
    result += create_block(next_question)

    result += '\n'

    return result


# Read all of the text from the file with the given file_name. Returns a string.
def get_text(file_name: str) -> str:
    file = open(file_name, "r")
    return file.read()


# Overwrite the file file_name with the contents of text.
def put_text(file_name: str, text: str):
    file = open(file_name, "w")
    file.write(text)
    file.close()
    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    create_block = readme_block.create_block

    input_dir = "questions"
    output_dir = "readmes"
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            assignment = filename[:-4]
        else: assignment = ""

        input_path_name = input_dir + "/" + filename
        output_path_name = output_dir + "/" + assignment + "Readme.txt"

        blocks = split(input_path_name)
        readme = create_readme(blocks, assignment)
        put_text(output_path_name, readme)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
