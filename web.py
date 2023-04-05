import streamlit as st 
from plot import *
from cursor_chat import *
col1, col2 = st.columns(2)
with col1: 
    st.markdown( """<h1>The Lost Key by Chan Chak Hang</h1>
        <p>You are an investigator with a reputation for solving the toughest cases. One day, your phone is buzzing.
        <br> What do you do?<br>
        A. Ignore it.
        <br>B. Pick up your phone</p>""", unsafe_allow_html=True)
    decision = st.text_input("Enter A or B: ", key="key1")

with col2:
    st.image("investigator.jpeg")
s = -1
i = -1

decision2 = ""

    
def decision_2():
    
    if decision.lower() == "a":
        with col1:
            st.write("Your colleague from the local police department finds you 15 minutes later and takes you to the crime scene.",
                        )
            arrive_crime_scene()
        with col2:
            st.image("crimescene.jpeg")
        return True
        
    elif decision.lower() == "b":
        with col1:
            st.write("You received a call from the local police department requesting your immediate assistance on a case.",
                 )
            arrive_crime_scene() 
        with col2:
            st.image("crimescene.jpeg")
        return True 
    
    elif decision == "":
        pass
    else:
        return st.write("Invalid input, only A or B")


if decision_2()==True:
    with col1:
        decision2 = st.text_input("What would you like to examine? \nEnter: Piano, Victim, Sheet music, Surrounding, Door, Bookshelf \n or Exit the scene: ", key="key2")
with col2:
    if decision2.lower() == "piano":
        st.write("The piano is a Fazioli F278, valued at $250,000. It has a glossy finish and appears to be well-maintained. Upon closer inspection, you notice that one of the keys, an A4, is broken. There are also bloodstains on the keyboard. ")   
    elif decision2.lower() == "victim":
        st.write("The victim, Emily, appears to have been stabbed to death. There are multiple wounds on her body, and signs of a struggle can be seen throughout the room. It is likely that she fought with the murderer before ultimately succumbing to her injuries.")
    elif decision2.lower() == "sheet music":
        st.write("""You find the pages of sheet music are scattered and disorganized, with some of them covered in bloodstains. The piece is Frederic Rzewski's "Marriage (The Road: Mile 58)." The blood has dyed the paper and it is difficult to make out some of the passages.""")
    elif decision2.lower() == "surrounding":
        st.write("As you look around the room, you notice that there is very little furniture. Some of the furniture that is present appears to have been overturned, and there are broken knick-knacks scattered on the ground. Upon closer inspection, you find the missing piano key under a table.")
    elif decision2.lower() == "door":
        st.write("There is no sign of a forced entry.")
    elif decision2.lower() == "bookshelf":
        st.write("The scores on the bookshelf are well-organized, and that there are Beethoven’s violin sonatas No. 1 through 10, except for No 9, which is missing. Upon further investigation, you find the missing score under the bookshelf.")
    elif decision2.lower() == "exit the scene":
        st.write("You left.")
        s = 0
    elif decision2 == "":
        pass    
    else:
        st.write ("Invalid input!")
if s == 0:
    state = st.session_state.get('state', {'s': 0})
    
    with col1:
        for i in range(0, len(dialog)):
            if st.button(f"Show Dialog {i}", key=f"{i}"):
                st.write(dialog[i])
                state['s'] = i + 1
            elif state['s'] > 12:
                s = 2
                i = 0 
        st.session_state['state'] = state
    with col2:
        st.write("You knock on the door of Emily's neighbor, Mrs. Jones. She answers the door and invites you in. She is a 30-year-old housewife who is currently playing some hip-hop music in the background.")
        st.image("note.jpeg")
        st.image("sad.jpeg")
if s == 2:
    st.image("suspect.jpeg")
    st.write("In the next hour, you track down Emily's ex-husband, Sebastian. He is a 42-year-old man who works as a producer in the film industry. You bring him to the police station, but he remains silent when you ask him about Emily. You need to make him confess, otherwise, you have a feeling he will escape since we do not have solid evidence to prove his guilt.")
    inp = st.text_input("Interrogate Sebastian to make him confess:")
    st.write(chat(inp))
