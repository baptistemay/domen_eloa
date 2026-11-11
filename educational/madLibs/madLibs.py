import re
import os

#TODO Set env
os.chdir("C:/Users/BTsubaki/Desktop/dev/prog/vs_projects/madLibs")
_target = input("""
Enter the name of the file.txt you want to work with.
For the purpose of this program, which is an exercice,
it should be refered as 'panda.txt'. : """)
_result = input("""
Enter the name of the file.txt you want to print the result in : """)

def _convert():
    with open(_target, "r", encoding = "utf-8") as converter:
        old_text = converter.read()

#TODO set the readers

    _target_ADJECTIVE = re.compile("ADJECTIVE")
    _target_NOUN = re.compile("NOUN")
    _target_ADVERB = re.compile("ADVERB")
    _target_VERB = re.compile("VERB")

#TODO set the converters

    _change_ADJECTIVE = input("""
Set the sentence/word you want to replace ADJECTIVE with : """)
    _change_NOUN = input("""
Set the sentence/word you want to replace NOUN with : """)
    _change_ADVERB = input("""
Set the sentence/word you want to replace ADVERB with : """)
    _change_VERB = input("""
Set the sentence/word you want to replace VERB with : """)

#TODO convert

    new_text = re.sub("ADJECTIVE", _change_ADJECTIVE, old_text)
    new_text = re.sub("NOUN", _change_NOUN, new_text)
    new_text = re.sub("ADVERB", _change_ADVERB, new_text)
    new_text = re.sub("VERB", _change_VERB, new_text)

    with open(_result, "w", encoding = "utf-8") as final_result:
        final_result.write(new_text)
    with open(_result, "r", encoding = "utf-8") as result_reader:
       print_result = result_reader.read()
       print("""
       
Displaying the result as in the file you registered :

""")
       print(print_result)
       print("End of the program")


_convert()