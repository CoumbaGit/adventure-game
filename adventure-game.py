

from cgitb import reset
import time
import random
import sys

friend1 = random.choice(["John", "Larry", "Paul"])
friend2 = random.choice(["Lala", "Ami", "Nancy"])


def print_pause(str, pause=3):
    time.sleep(pause)
    print(str)


def house():

    print_pause(
        """You find yourself standing in front of your door 
        after a night out with friends.""")
    print_pause(
        """As you reach in your right pocket for your housekeys, 
        you realize they are empty.""")
    print_pause(
        """You check your left pocket 
        and the keys aren't there either.""")
    print_pause(
        """Perplexed, you go back to your car to look 
        and still cannot find your keys.""")
    print_pause(f"Enter 1 to call your friend {friend1}.")
    print_pause(f"Enter 2 to call your friend {friend2}.")

    while True:
        option = input("Who do you call?")
        wingman()
        if option == "1":
            wingman()
        elif option == "2":
            wingwoman()
        else:
            print("""You may have had too many Shirley Temples!!
            Please try again.""")


def wingman():
    print_pause(
        """You place the call 
    and unfortunately it goes to voicemail.""")
    print_pause(f"Enter 1 to reach out to {friend2}.")
    print_pause(f"Enter 2 to call {friend1} back.")

    option = input("What do you do now?")
    if option == "1":
        wingwoman()
    elif option == "2":

        print(

            f"""I call {friend1} back. 
                His phone didn't even ring this time and 
                went straight to voicemail.
                He turned off his phone!!!GAME OVER!""")
        restart()

    else:
        print("You are out of luck. Try again!")


def wingwoman():

    print_pause(
        f"""You call {friend2} and she picks up!! 
        Her and {friend1} went their separate 
        ways when you left.""")
    print_pause(
        f"""She is with a different group of friends 
        at another lounge. 
        You tell her about your keys 
        and she thinks {friend1} 
        may have them but is not sure.""")
    print_pause("You tell her you have not been able to reach him.")
    print_pause("Enter 1 to wait in your car.")
    print_pause("Enter 2 to go back to the club.")

    option = input("What do you do next?")
    if option == "1":
        print_pause(
            """You decide to spend the rest 
            of the night in your car. 
            You are beyond exhausted at this point. 
            GAME OVER!""")
        restart()
    elif option == "2":
        club()
    else:
        print("You are out of luck")


def club():
    print_pause(
        f"""You get back in your car 
        and the 20 minutes drive feels like an hour. 
        As you are about to arrive at the venue,
        {friend1} finally calls you back.""")
    print_pause("""He had left the club and 
    was having a late night snack at a diner. 
    He does have your keys and forgot to gave them back 
    when you asked him to hold onto them 
    while looking for your ID.""")
    print_pause(f" Enter 1 to join {friend1} at the diner.")
    print_pause(
        f"""Enter 2 to ask {friend1} to come meet you 
        where you are. 
        You are running out of gas.""")

    option = input("What do you do now?")
    if option == "1":
        print(
            f"""You meet with {friend1} and decide to stay
                and have a snack before returning home. 
                You got your keys back! 
                All's  well that ends well! :-) """)
        # restart()
    elif option == "2":
        print(f"""{friend1} agrees to come back to the venue 
            and return the keys. 
            You make it home safely 
            and ready to get some well deserved rest.
            You have your keys back!""")
        # restart()
    else:
        print("Not quite! ")


def restart():
    while True:
        option = input("Would you like to play again? Yes or No?")
        if option == "Yes":
            house()
        elif option == "No":
            print("Thank you!")
            sys.exit()
        else:
            print("Incorrect input. Please enter Yes or No!")


house()
