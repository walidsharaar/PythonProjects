#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PALCEHOLDER="[name]"
# todo create a list of name

with open("./input/names/invited_names.txt") as names_files:
    names= names_files.readlines()
    print(names)

# todo read the letter
with open("./input/letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter= letter_contents.replace(PALCEHOLDER,stripped_name)
        with open(f"./output/readytosend/letter_for_{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)

        print(new_letter)

