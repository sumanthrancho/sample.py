# !pip install streamlit

import streamlit as st
import random
st.title("Rancho Labs")
st.title('Welcome to Rock , Paper, Sicssors !\n')
player_win=0
computer_win=0
choices=['R','P','S']
computer=random.choice(choices)

# print(computer)



player = st.text_input("Enter a choice (Rock (R), Paper (P), Scissors(S)) only capital case :\n")





if(st.button('Submit')):
  st.write("You chose {0} and computer chose {1} \n".format(player,computer))
  if(player==computer):
    st.error("Both players selected {}. It is a tie!".format(player))

  elif player =="R":
    if computer =='S':
      st.success("Hurray ! , You win")
      player_win+=1
    else:
      st.error('Opps! , You lose')
      computer_win+=1

  elif player=='P':
    if computer =='R':
      st.success("Hurray ! , You win")
      player_win+=1
    else:
      st.error('Opps! , You lose')
      computer_win+=1

  elif player =="S":
    if computer =='P':
      st.success("Hurray ! , You win")
      player_win+=1
    else:
      st.error('Opps! , You lose')
      computer_win+=1
  else:
    st.success('Please enter Stone ,paper, scissors')


  st.write("Your Score is : "+str(player_win)+"\n")
  st.write("Computer Score is : "+str(computer_win))


# if(st.button('Submit')):
#     result = name.title()
#     st.success(result)
