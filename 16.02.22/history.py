import os
import subprocess


def piece(prompt):
    cat_everything = subprocess.getoutput("cat ~/.bash_history")
    list_creator = []
    splitter = cat_everything.split("\n")
    list_creator.append(splitter[::-1])
    remove_outer_list = [val for sublist in list_creator for val in sublist]
    for command in remove_outer_list:
        if prompt in command:
            search = input(f"Start the following command:\n '{command}'?\n")
            if search == "q":
                print("It's not like I like you or anything... ~baka!")
                quit()
            if search != "y":
                continue
            else:
                os.system(command)
                return
    print("End of the list, master!")


piece('docker')
