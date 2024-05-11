'''Simulation of one day of student life using FSM'''
import random
from queue import Queue

class StudentFSM:
    '''
    Simulation of student day(s)
    The algorithm is based on Finite State Machine
    '''
    def __init__(self):
        self.states = ["EAT", "SLEEP", "STUDY", "EXERCISE", "RELAX", "DEAD"]
        self.current_state = "SLEEP"
        self.hunger = 2
        self.energy = 1
        self.stress = 0
        self.hour = 0
        self.events = ["deadline", "feeling bad", "meet a friend", \
        "good weather", "bad weather"] #added two undefined
        #events for random events to have smaller probability

    def print_state(self):
        '''Print the information about current state and the hour'''
        print(f"CURRENT STATE: {self.current_state}\nHOUR: {self.hour%24}:00")

    def print_vital_signs(self):
        '''Print information about vital signs of the student'''
        print(f"VITAL SIGNS: hunger: {self.hunger}, stress: {self.stress}, \
energy: {self.energy}\n")

    def print_unexpected_event(self, event):
        '''Print the information about an unexpected event'''
        print(f"***** Unexpected event: {event} *****")

    def transition(self):
        '''The method, which decides, what state will be next'''
        self.print_state()
        event = random.choice(self.events)

        if self.current_state == "EAT":
            self.hunger = max(0, self.hunger - 6)
            self.stress = max(0, self.stress - 0.5)
            self.energy = max(0, self.energy - 0.5)

            if self.hour%24 in list(range(0, 7)) + [23]:
                self.current_state = "SLEEP"
                print("Ohh, it's very late, time to go to bed!")
            elif self.energy <= 2:
                self.current_state = "SLEEP"
                print("I am very tired, time to take a nap.")
            elif event == "meet a friend":
                self.print_unexpected_event(event)
                self.current_state = "WALK"
                print("I met a friend in the dining room, so \
it's time to go for a walk in the park")
            elif event == "deadline":
                self.print_unexpected_event(event)
                self.current_state = "STUDY"
                print("I have a deadline, I have to go study now")
            else:
                self.current_state = random.choice(["WALK", "STUDY"])
                if self.current_state == "WALK":
                    print("I don't have any tasks to do, so I can have a walk now")
                else:
                    print("I am full now and I can go studying")

        elif self.current_state == "SLEEP":
            self.energy = min(10, self.energy + 1.5)
            self.hunger = min(10, self.hunger + 0.5)
            self.stress = max(0, self.stress - 1)

            if self.hour%24 in list(range(0, 7)) + [23]:
                print("zzz.....")
            elif self.hunger >= 7 and self.hour%24 == 7:
                self.current_state = "EAT"
                print("Oh, it's 7 am, time to have breakfast!")
            else:
                self.current_state = "STUDY"
                print("After a good sleep, I can start studying right away!")

        elif self.current_state == "STUDY":
            self.stress = min(10, self.stress + 2)
            self.energy = max(0, self.energy - 0.5)
            self.hunger = min(10, self.hunger + 1.5)

            if event == "deadline":
                self.print_unexpected_event(event)
                print("Oh no, I must finish the task, the dedline is very soon.")
            elif self.hour%24 in list(range(0, 7)) + [23]:
                self.current_state = "SLEEP"
                print("Ohh, it's very late, time to go to bed!")
            elif self.stress >= 7:
                print("Time to take a break, because I am too stressed")
                self.current_state = "RELAX"
            elif self.energy <= 2:
                print("I am very exhausted, it's time to take a nap.")
                self.current_state = "SLEEP"
            elif event == "feeling bad":
                self.print_unexpected_event(event)
                print("Oh no, I am feeling really bad, maybe I should take a rest")
                self.current_state = "RELAX"
            elif self.hunger >= 7:
                print("My stomach is grumbling, time to go eat!")
                self.current_state = "EAT"
            else:
                print("I love learning new things, I'm going to continue studying")
                self.current_state = "STUDY"

        elif self.current_state == "WALK":
            self.stress = max(0, self.stress - 2)
            self.energy = max(0, self.energy - 1)
            self.hunger = min(10, self.hunger + 1.5)

            if self.hunger >= 7:
                print("The walk was nice and now I am hungry.")
                self.current_state = "EAT"
            elif self.hour%24 in list(range(0, 7)) + [24]:
                self.current_state = "SLEEP"
                print("Ohh, it's very late, time to go to bed!")
            elif self.energy <= 2:
                print("The walk was nice and now I am very tired, time to take a nap.")
                self.current_state = "SLEEP"
            elif event == "deadline":
                self.current_state = "STUDY"
                self.print_unexpected_event(event)
                print("I have a deadline, I have to go study now")
            elif event == "meet a friend":
                self.print_unexpected_event(event)
                print("I saw my friend and we decided to continue our walk")
            elif event == "feeling bad":
                self.print_unexpected_event(event)
                print("I am not feeling good, I should take a rest")
                self.current_state = "SLEEP"
            else:
                print("The walk was perfect and now I am ready to continue studying!")
                self.current_state = "STUDY"

        elif self.current_state == "RELAX":
            self.stress = max(0, self.stress - 3)
            self.hunger = min(10, self.hunger + 0.5)

            if self.hunger >= 7:
                print("My stomach is grumbling, time to go eat!")
                self.current_state = "EAT"
            elif self.energy <= 1:
                print("I am exhausted, time to take a nap")
                self.current_state = "SLEEP"
            elif event == "deadline":
                self.print_unexpected_event(event)
                print("I have an important task to do, time to go study!")
                self.current_state = "STUDY"
            else:
                print("Well, now I feel much better and I can go study!")
                self.current_state = "STUDY"
        self.print_vital_signs()

    def run_simulation(self, hours=24):
        '''Main loop of the simulation'''
        while self.hour != hours:

            self.transition()

            if self.current_state == "DEAD":
                return

            if self.stress >= 10:
                print("Stress level is too high. Unfortunately, you died of stress.\n")
                self.current_state = "DEAD"
            elif self.hunger >= 10:
                print("Hunger level is too high. Unfortunately, you died of hunger.\n")
                self.current_state = "DEAD"
            elif self.energy <= 0:
                print("Energy level is too low. Unfortunately, you died of exhaustion.\n")
                self.current_state = "DEAD"

            self.hour += 1

student = StudentFSM()
student.run_simulation()
