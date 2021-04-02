"""
readme_block.py
Creates a block around the given text.

Dependencies:
- typing
"""

from typing import Union, List


def create_block(text: Union[str, List[str]], stars: int = 87) -> str:
    """Creates a block around the given text.

    Args:
        text (Union[str, List[str]]): The text as a str or a list of strs.
        stars (int): The number of stars for the border.
            Each line of text will fit in (stars - 4) characters.
            Default is 87.

    Raises:
        TypeError:
            If `text` is not a str or a list of strs.
            If `stars` is not an int.

    Returns:
        str: The block of text.
    """

    input_lines = list()
    if type(text) is str:
        input_lines = text.split('\n')
    elif type(text) is list:
        for line in text:
            if type(line) is not str:
                raise TypeError('text is not a str or a list of strs')
            input_lines += line.split('\n')
    else:
        raise TypeError('text is not a str or a list of strs')

    if type(stars) in (int, float):
        stars = int(stars)
    else:
        raise TypeError('stars is not an int')

    # subtract 4 for border and spaces on each side
    line_len = stars - 4

    final_lines = list()

    for input_line in input_lines:

        line = input_line
        while len(line) > line_len:

            # find last space that will fit on a line
            last_space = line.rfind(' ', 0, line_len)

            # words all fit perfectly
            if line[line_len] == ' ' or line[line_len - 1] == ' ':
                this_line = line[:line_len]
                next_line = line[line_len:].lstrip()

            # space not found; assume entire line is one word
            # break word? might be awkward
            elif last_space == -1:
                this_line = line[:line_len - 1] + '-'
                next_line = line[line_len - 1:]

            # otherwise, break line so that words fit
            else:
                this_line = line[:last_space]
                next_line = line[last_space:].lstrip()

            # add line and move to next line
            final_lines.append(this_line)
            line = next_line

        # add last bit (or original line if it fits already)
        final_lines.append(line)

    final = ('/' + '*' * stars + '\n' +
             '\n'.join(f' * {line:<{line_len}} * ' for line in final_lines) + '\n' +
             ' ' + '*' * stars + '/'
             )

    return final


if __name__ == '__main__':
    msg = 'Input lines one by one. Press enter (blank input) to end.'

    print(msg)
    print('=' * len(msg))

    inputted = list()
    while True:
        next_in = input()
        if next_in == '':
            break
        inputted.append(next_in)

    print('=' * len(msg))

    block = create_block('\n'.join(inputted))

    print(block)
