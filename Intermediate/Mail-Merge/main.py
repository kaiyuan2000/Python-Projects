#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#method readlines(), replace(), strip()

#record down name first
with open ("/Users/kaiyuan/PycharmProjects/day24_file_path/Input/Names/invited_names.txt", mode = "r") as f:
    name_list = f.readlines()


#replace name
with open("/Users/kaiyuan/PycharmProjects/day24_file_path/Input/Letters/starting_letter.txt", mode = "r") as g:
    letter = g.read()

#write new file
for name in name_list:
    with open(f"/Users/kaiyuan/PycharmProjects/day24_file_path/Output/ReadyToSend/letter_for_{name}", mode = "w") as w:
        w.write(letter.replace("[name]",name.strip()))