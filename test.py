import numpy as np

import random
from Levenshtein import distance as levenshtein_distance

import colorama
from colorama import Fore, Style

# Initialize Colorama
colorama.init(autoreset=True)

verbi = np.array([['accendere', 'acceso', 'allumer'],
 ['aggiungere', 'aggiunto', 'ajouter'],
 ['aprire', 'aperto', 'ouvrir'],
 ['attendere', 'atteso', 'attendre'],
 ['chiedere', 'chiesto', 'demander'],
 ['chiudere', 'chiuso', 'fermer'],
 ['connettersi', 'connesso', 'se connecter'],
 ['correggere', 'corretto', 'corriger'],
 ['cuocere', 'cotto', 'cuire'],
 ['decidere', 'deciso', 'décider'],
 ['descrivere', 'descritto', 'décrire'],
 ['dire', 'detto', 'dire'],
 ['esprimere', 'espresso', 'exprimer'],
 ['essere', 'stato', 'être'],
 ['fare', 'fatto', 'faire'],
 ['friggere', 'fritto', 'frire'],
 ['leggere', 'letto', 'lire'],
 ['mettere', 'messo', 'mettre'],
 ['morire', 'morto', 'mourir'],
 ['muovere', 'mosso', 'mouvoir'],
 ['nascere', 'nato', 'naître'],
 ['nascondere', 'nascosto', 'cacher'],
 ['offrire', 'offerto', 'offrir'],
 ['perdere', 'perso', 'perdre'],
 ['piangere', 'pianto', 'pleurer'],
 ['prendere', 'preso', 'prendre'],
 ['promettere', 'promesso', 'promettre'],
 ['proporre', 'proposto', 'proposer'],
 ['raccogliere', 'raccolto', 'recueillir'],
 ['ridere', 'riso', 'rire'],
 ['rimanere', 'rimasto', 'rester'],
 ['rispondere', 'risposto', 'répondre'],
 ['rompere', 'rotto', 'casser'],
 ['scegliere', 'scelto', 'choisir'],
 ['scoprire', 'scoperto', 'découvrir'],
 ['scrivere', 'scritto', 'écrire'],
 ['smettere', 'smesso', 'cesser'],
 ['sorridere', 'sorriso', 'sourire'],
 ['spegnere', 'spento', 'éteindre'],
 ['spendere', 'speso', 'dépenser'],
 ['succedere', 'successo', 'arriver'],
 ['togliere', 'tolto', 'enlever'],
 ['tradurre', 'tradotto', 'traduire'],
 ['trascorrere', 'trascorso', 'passer'],
 ['vedere', 'visto', 'voir'],
 ['venire', 'venuto', 'venir'],
 ['vincere', 'vinto', 'gagner'],
 ['vivere', 'vissuto', 'vivre']])

verbi_T = verbi.transpose()

print(verbi_T)

def find_similar_words(words_list, target_word, randomness=0):
    """
    Find the most similar words to the target word in the given list.
    Similarity is based on Levenshtein distance.

    :param words_list: List of words to search through.
    :param target_word: The word to find similarities to.
    :param randomness: Parameter to add randomness to the selection.
    :return: List of words most similar to the target word.
    """
    # Calculate the distance of each word from the target word
    distances = [(word, levenshtein_distance(word, target_word) + random.uniform(0, randomness))
                 for word in words_list]

    # Sort the words based on the calculated distance
    distances.sort(key=lambda x: x[1])

    # Extract only the words from the sorted list
    similar_words = [word for word, _ in distances]

    # Ensure the target word is always included in the result
    if target_word not in similar_words:
        similar_words.insert(0, target_word)

    return similar_words

# Example usage
target_word = "chiudere"
res = find_similar_words(verbi_T[0], target_word, randomness=1)  # Example with randomness



def run_quiz_rounds(rounds, n_similar):
    score = 0
    np.random.shuffle(verbi)

    for k in range(rounds):
        # Randomly choose a verb combination
        chosen_verb = verbi[k]

        # Randomly decide which form to present (0: Italian Infinitive, 1: Italian Past Participle, 2: French Infinitive)
        present_form_index = random.randint(0, 2)
        present_form = chosen_verb[present_form_index]

        # Present the chosen form to the user
        # Colorful output
        print(f"{Fore.YELLOW}Round {k+1}:")
        
        lookup_type = ["Presente", "Participio Passato","Tradductione"]


        # Generate similar options for the remaining forms
        options = []
        for i in range(3):
            if i != present_form_index:
                similar_words = find_similar_words(verbi_T[i], chosen_verb[i], randomness=1)[:n_similar]
                options.append((i, similar_words))

        discovered = ["","",""]
        discovered[present_form_index] = present_form

        # Show options to the user and get the answer
        for index, (form_type, words) in enumerate(options):
            discovered[form_type] = "?"
            
            print(f"{discovered[0]} | {discovered[1]} | {discovered[2]}")

            correct = words[0]
            
            random.shuffle(words)

            for i,word in enumerate(words):
                print(f"{Fore.RED}{i+1}{Fore.WHITE}: {word}")
            while True:

            

                user_answer = int(input("Choose the correct option : ")) - 1
                if user_answer >= 0 and user_answer < len(words):
                    break

            print()
            print()
            print()
            print()

            # Check the answer and update the score
            if words[user_answer] == correct:
                print(f"{Fore.GREEN}Correct!")
                score += 1
            else:
                print(f"{Fore.RED}Incorrect. The correct answer was: {correct}")

            discovered[form_type] = correct


            


    print(f"{Fore.CYAN}Your final score is: {score}/{rounds}{Style.RESET_ALL}")

def run_written_quiz_rounds(rounds):
    score = 0
    np.random.shuffle(verbi)

    for k in range(rounds):
        # Randomly choose a verb combination
        chosen_verb = verbi[k]

        # Randomly decide which form to present (0: Italian Infinitive, 1: Italian Past Participle, 2: French Infinitive)
        present_form_index = random.randint(0, 2)
        present_form = chosen_verb[present_form_index]

        # Present the chosen form to the user
        print(f"{Fore.YELLOW}Round {k+1}:")

        lookup_type = ["Presente", "Participio Passato", "Tradductione"]
        
        # The remaining forms that the user needs to guess
        remaining_forms = [i for i in range(3) if i != present_form_index]
        
        # Display the prompt to the user
        discovered = ["", "", ""]
        discovered[present_form_index] = present_form
        print(f"{discovered[0]} | {discovered[1]} | {discovered[2]}")

        for form_type in remaining_forms:
            user_answer = input(f"Enter the {lookup_type[form_type]} form: ").strip()

            # Check the answer and update the score
            if user_answer.lower() == chosen_verb[form_type].lower():
                print(f"{Fore.GREEN}Correct!")
                score += 1
            else:
                print(f"{Fore.RED}Incorrect. The correct answer was: {chosen_verb[form_type]}")

            discovered[form_type] = chosen_verb[form_type]

    print(f"{Fore.CYAN}Your final score is: {score}/{rounds*2} | {score/(rounds*2)}{Style.RESET_ALL}")




# Example usage
rounds = 30
n_similar = 5
#run_quiz_rounds(len(verbi), n_similar)
run_written_quiz_rounds(len(verbi))