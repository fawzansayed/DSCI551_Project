import re
import sys
import datetime
import pandas as pd
from lxml import etree

def ls(tree, type_):
    """ Finds the path names and isolates based on user """
    path_names = []
    path_list = []
    count = 0
    for element in tree.xpath("//name"):
        if element.text != '/':
            if type_[count - 1] == 'FILE':

                new_string = "".join(path_list[1] + "/{}".format(element.text))
                path_list.append(new_string)
                path_names.clear()
                path_names.append(new_string)
                count = count + 1
            else:
                path_names.append('/{}'.format(element.text))
                new_string = "".join(path_names)
                path_list.append(new_string)
                count = count + 1
        else:
            # path_names.append(element.text)
            new_string = "".join(path_names)
            path_list.append(new_string)
            count = count + 1

    df['Path'] = path_list

if __name__ == '__main__':
    # Making the dataframe for the tsv file later on
    df = pd.DataFrame()
    file_path = sys.argv[1]
    tsv_name = sys.argv[2]

    # Establishing tree and sub-elements
    tree = etree.parse(file_path)
    type_ = [element.text for element in tree.xpath("//type")]

    # Getting the path names
    ls(tree, type_)
