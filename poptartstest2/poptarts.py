#!/usr/bin/env python3

"""Derek Jan Beerhorst Labs | Dr. Jan Beerhorst
   Poptarts - Which Poptart is best for you?"""


#Moods are linked to a Poptart flavor. 

def get_poptart_flavor(mood):
    poptart_flavors = {
        'happy'      : 'Strawberry',
        'relaxed'    : 'Blueberry',
        'excited'    : 'Chocolate Fudge',
        'cozy'       : 'Brown Sugar Cinnamon',
        'hungry'     : 'Cookies and Cream',
        'energetic'  : 'Wild Berry',
        'romantic'   : 'Cherry',
        'nostalgic'  : 'Cinnamon Roll',
        'refreshed'  : 'Frosted Raspberry',
        'adventurous': 'Smores',
        'sad'        : 'a boat load of'
    }

# Return Poptart flavors corresponding to the mood provided. If the mood is not found, return 'Unknown Mood'. 
    return poptart_flavors.get(mood.lower(), 'Unknown Mood')

if __name__ == "__main__":
    while True:
        #Ask user to provide their mood. 
        mood_input = input("How are you feeling today? (Type 'I hate Poptarts' to quit): ").strip().lower()

        #See if the user wants to exit the program.
        if mood_input == 'i hate poptarts':
            print("Exiting the program. Go have a Poptart!")
            break # this will end the loop which will end the program
            
        #Get the flavor based on the user's mood. 
        poptart_flavor = get_poptart_flavor(mood_input)
        
        #Check to see if the mood is valid and has a corresponding flavor. 
        if poptart_flavor != 'Unknown Mood':
            #Print the suggested flavor
            print(f"Hmmm.. I think you might enjoy a {poptart_flavor} Pop-Tarts!")
            break # this will end the loop which will end the program
        else:
            #Let the user know they do not deserve a Poptart if it doesn't match.
            print("Sorry, feeling that way does not earn you a Poptart.")
            break
