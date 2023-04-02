
import streamlit as st 
def begin ():
    t = """<h1>The Lost Key by Chan Chak Hang</h1>
    <p>You are an investigator with a reputation for solving the toughest cases. One day, your phone is buzzing.
    <br> What do you do?<br>
    A. Ignore it.
    <br>B. Pick up your phone</p>"""
    return t

def decision_2(a,b):
    decision = input("Enter A or B: ")
    if decision == "A":
        return a
    elif decision == "B":
        return b
    else:
        print ("Invalid input, only A or B")
        return decision_2(a,b)

d_6 = "What would you like to examine?"
def decision_6():
    decision = input("What would you like to examine? \nEnter: Piano, Victim, Sheet music, Surrounding, Door, Bookshelf or Exit the scene:\n ")
    if decision == "Piano":
        print("The piano is a Fazioli F278, valued at $250,000. It has a glossy finish and appears to be well-maintained. Upon closer inspection, you notice that one of the keys, an A4, is missing. There are also bloodstains on the keyboard. ")
        return decision_6()
    elif decision == "Victim":
        print("The victim, Emily, appears to have been stabbed to death. There are multiple wounds on her body, and signs of a struggle can be seen throughout the room. It is likely that she fought with the murderer before ultimately succumbing to her injuries.")
        return decision_6()
    elif decision == "Sheet music":
        print("""You find the pages of sheet music are scattered and disorganized, with some of them covered in bloodstains. The piece is Frederic Rzewski's "Marriage (The Road: Mile 58)." The blood has dyed the paper and it is difficult to make out some of the passages.""")
        return decision_6()
    elif decision == "Surrounding":
        print("As you look around the room, you notice that there is very little furniture. Some of the furniture that is present appears to have been overturned, and there are broken knick-knacks scattered on the ground. Upon closer inspection, you find the missing piano key under a table.")
        return decision_6()
    elif decision == "Door":
        print("There is no sign of a forced entry.")
        return decision_6()
    elif decision == "Bookshelf":
        print("The scores on the bookshelf are well-organized, and that there are Beethoven’s violin sonatas No. 1 through 10, except for No 9, which is missing. Upon further investigation, you find the missing score under the bookshelf.")
        return decision_6()
    elif decision == "Exit the scene":
        print("You left")
    else:
        print ("Invalid input, only A or B")
        return decision_6()
def arrive_crime_scene():   
    return st.markdown("When you arrive at the crime scene, you come across a luxurious apartment with a grand piano at its center. The room is spacious, with high ceilings and large windows that let in plenty of natural light. The piano is a magnificent instrument with a glossy finish. It's obvious that no expenses were spared in the decoration of this room. The victim, a young woman named Emily, is found death right in front of you.<br> What would you like to examine?",unsafe_allow_html=True)

dialog = [

"""You: Hi, Mrs. Jones. I'm here to ask you a few questions about Emily, next door.""",

"""Mrs Jones: Sure, what would you like to know?""",

"""You: Did you know Emily well?""",

"""Mrs Jones: Oh yeah, she was a really cool lady. We'd catch up in the hallway every now and then, and she'd even play some sweet tunes on the piano when I'd come by for tea. She was seriously talented.""",

"""You: Have you recently come across anything that caught your attention?""",

"""Mrs Jones: So, like, I don't know for sure or anything, but I did hear some arguing coming from her apartment about a week ago. I heard a dude's voice. I'm not sure who he is, but I'm thinking it's her husband. Honestly, it's freaking me out that something happened next door. It's way too close for comfort, you know?
""",
"""You: I understand how you feel. Did she ever mention anything about having a husband?""",

"Mrs Jones: Um, she did say that she had an ex-husband. They split up a few years back.",

"You: Do you know if they had any particular issues during their marriage?",

"Mrs Jones: I was just chatting with Emily the other day, and she mentioned that she had a husband. From what she told me, it sounded like things weren't all sunshine and rainbows in their relationship. In fact, she even said that he wasn't a great guy and didn't treat her well.",

"Of course, I'm not entirely sure if he was involved in what happened to her, but I thought it might be worth mentioning. I mean, it's just a hunch, but it's definitely something to consider, right?",

"You: We're doing everything we can to find out who did this. Thank you for your time, Mrs. Jones. This information is helpful.",

"Mrs Jones: If you need anything else to help with the investigation, just give me a holler. I can't help but feel like the person who did this is still out there somewhere."]
