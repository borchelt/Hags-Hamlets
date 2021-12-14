from prints import printr
from prints import prints
#from npcs import trade

def dialogue(dialogue_options, dialogue_outcome, npc, player):
    global choice_made
    global dialogue_option_chosen

    def choose():
        global dialogue_option_chosen
        prints("Choose an option by # below....." ,.3)
        prints("",.3)
        for i in range(len(dialogue_options)):
            prints(f"   {i + 1}. {dialogue_options[i]}", .3)
        

        dialogue_option_chosen = input(printr("> "))
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
                    prints("")
                    if(i == npc.tradeNum):
                        npc.trade(player)
                    if(i == npc.questNum):
                        print("questcalled")
                        npc.questFunc(npc)
                    elif(i == npc.questEndNum):
                        print("questEnd")
                        for i in player.inventory:
                            if i.name == npc.questTrades[npc.questIndex][1]:
                                npc.questTrades[npc.questIndex][2](npc)
                                player.inventory.remove(i)
                                player.inventory.append(npc.questTrades[npc.questIndex][0])
                                npc.options.remove(npc.options[npc.questEndNum])
                                npc.outcomes.remove(npc.outcomes[npc.questEndNum])
                                npc.options.remove(npc.options[npc.questTrades[npc.questIndex][3]])
                                npc.outcomes.remove(npc.outcomes[npc.questTrades[npc.questIndex][3]])
                                npc.questNum = -1
                                break

    
    dialogue_option_chosen = int(dialogue_option_chosen)

    for i in range(1, len(dialogue_options)):
            
        if dialogue_option_chosen != len(dialogue_options):
            dialogue(dialogue_options,dialogue_outcome, npc, player)
        


                        






