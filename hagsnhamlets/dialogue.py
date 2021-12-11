from prints import printr
from prints import prints
#from npcs import trade

def dialogue(dialogue_options, dialogue_outcome):
    global choice_made
    global dialogue_option_chosen

    def choose():
        global dialogue_option_chosen
        prints("Choose an option by # below....." ,.3)
        prints("",.3)
        for i in range(len(dialogue_options)):
            prints(f"   {i + 1}. {dialogue_options[i]}", .3)
        

        dialogue_option_chosen = input("> s")
        return dialogue_option_chosen
        
    choose()

    valid_response = []
    for i in range(len(dialogue_options)):
        valid_response.append(f"{i + 1}")
    

    for i in range(len(valid_response)):
        if dialogue_option_chosen != valid_response[i]:
            failed = True 
            
        else:
            for i in range(len(valid_response)):
                if dialogue_option_chosen == valid_response[i]:
                    choice_made = dialogue_option_chosen

            for i in range(len(dialogue_outcome)):
                if choice_made == valid_response[i]:
                    prints(f"{dialogue_outcome[i]}")
                    print("")
    
    dialogue_option_chosen = int(dialogue_option_chosen)

    for i in range(1, len(dialogue_options)):
            
        if dialogue_option_chosen != len(dialogue_options):
            dialogue(dialogue_options,dialogue_outcome)
        


                        






