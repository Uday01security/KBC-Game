#KAUN BANEGA KARODPATI
import time
import random
import colorama
from colorama import Fore,Style

name=str(input( Fore.BLUE+Style.BRIGHT+"kya shubh naam hai aapka:"))
print("KON BANEGA KARODPATI ME AAPKA SWAGAT HAI",name,"JI!!!\n")
num=int(input(Fore.RED+Style.NORMAL+"if you want to play, please enter 1 otherwise 0:"))
if num==1:
    print(Fore.GREEN+Style.BRIGHT+"thank you for confirmation ",name,"ji"+Style.RESET_ALL)
else:
    print(Fore.RED+Style.BRIGHT+"as you wish sir,GOODBYE"+Style.RESET_ALL)
    exit()

questions=[
            "international literacy day is observed on?",
            "The language of Lakshdweep the Union Territory of india is?",
            "In which group of place the Kumbh mela is held every 12 years",
            "Bahubali festival is related to?",
             "Which day is observed as a world standards daya?"
]

options = [
     ["1. sep 8", "2. nov 28", "3. may 2", "4. sept 2"],
     ["1. Tamil", "2. Hindi", "3. Malayalam", "4. Telugu"],
     ["1. Ujjain, Puri, Prayag, Haridwar", "2. Prayag, Haridwar, Ujjain, Nashik",
      "3. Rameshwaram, Puri, Badrinath, Dwarika", "4. Chittakoot, Prag, Haridwar, Ujjain"],
    ["1. Islam", "2. Hinduism", "3. Buddhism", "4. Jainism"],
    ["1. June 26", "2. Oct 14", "3. Nov 15", "4. Dec 2"]
]


answers=[1,3,2,4,2]

prizes=[10,20,30,40,50]# price in lakhs
total_winnings=0
lifeline_used=False

options = [
     ["1. sep 8", "2. nov 28", "3. may 2", "4. sept 2"],
     ["1. Tamil", "2. Hindi", "3. Malayalam", "4. Telugu"],
     ["1. Ujjain, Puri, Prayag, Haridwar", "2. Prayag, Haridwar, Ujjain, Nashik",
      "3. Rameshwaram, Puri, Badrinath, Dwarika", "4. Chittakoot, Prag, Haridwar, Ujjain"],
    ["1. Islam", "2. Hinduism", "3. Buddhism", "4. Jainism"],
    ["1. June 26", "2. Oct 14", "3. Nov 15", "4. Dec 2"]
]

def fifty_fifty(question_index):
    correct_option = answers[question_index]  # Get correct answer (1-4)
    all_options = [1, 2, 3, 4]  # List of all options

    # Remove the correct answer temporarily
    incorrect_options = [opt for opt in all_options if opt != correct_option]

    # Randomly remove two incorrect options
    removed_options = random.sample(incorrect_options, 2)

    # Remaining options = Correct answer + 1 random incorrect answer
    remaining_options = [opt for opt in all_options if opt not in removed_options]

    # Display remaining options correctly
    print(Fore.MAGENTA + "\n💡 Lifeline 50-50 Activated! Here are your remaining options:" + Style.RESET_ALL)
    for opt in remaining_options:
        print(Fore.GREEN + options[question_index][opt - 1] + Style.RESET_ALL)  # FIX: Safe Indexing

    return remaining_options  # Return two valid options


for i in range(len(questions)):
    time.sleep(4)
    print(Fore.YELLOW+Style.NORMAL+"\n Question ",(i+1),"for",(prizes[i]),"lakh rupees."+Style.RESET_ALL)
    print(Fore.BLUE+Style.BRIGHT+questions[i]+Style.RESET_ALL)
    print("\n".join(options[i]))

    if not lifeline_used:
        use_lifeline=input(Fore.BLUE+"do you want to use lifeline? (yes/no):"+Style.RESET_ALL).strip().lower()
        if use_lifeline== "yes":
            lifeline_used=True
            valid_options=fifty_fifty(i)
    else:
        valid_options=[1,2,3,4]

    choice=int(input(Fore.YELLOW+"enter your answer: "+Style.RESET_ALL))
    time.sleep(2)

    if choice==(answers[i]):
        total_winnings+=prizes[i]
        print(Fore.GREEN+Style.BRIGHT+"correct answer!!!,you have won",total_winnings,"lakh rupees"+Style.RESET_ALL)
    else:
        print(Fore.RED+Style.BRIGHT+"YEH GALAT HO GAYA MAHASHAY...., DUKH KE SATH KEHNA PAD RAHA HAI KI AAP AAGE "
              "NAHI KHEL SAKTE..."+Style.RESET_ALL)
        exit()
print(Fore.MAGENTA+Style.BRIGHT+"congratulations....you won the total winning prize of",total_winnings,"lakhs")
