import threading
import time
import os
import sys
import keyboard


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
            return instances[class_]
    return getinstance

@singleton
class Human:
    # constructor initializing normal count of blood components
    def __init__(self):
        self.wbc = 0.03
        self.rbc = 0.4
        self.plat = 0.2
        self.plasma = 0.5
        self.t1 = None
        self.t2 = None
        self.answer = None
        print('The normal percentage of Red Blood Cells in blood is ', self.rbc)
        print('The normal percentage of White Blood Cells in blood is', self.wbc)
        print('The normal percentage of Platelets is', self.plat)
        print('The normal plasma content percentage is', self.plasma)

    def user_input(self):
        choice = int(input())
        t3 = threading.Thread(target=self.userchoice())
        if choice == 1:
            self.t1 = threading.Thread(target=self.start_infection())
            self.t1.start()
            t3.start()
        elif choice == 2:
            self.t2 = threading.Thread(target=self.apply_antidote())
            self.t2.start()
        else:
            self.exitprogram()

    # method to start infection


    def start_infection(self):
        print('The infection has started')
        for i in range(0, 5):
            self.wbc += 0.05
            self.rbc -= 0.02
            self.plat -= 0.04
            print('The infection details after :', i*10, 'seconds')
            print('The wbc count after infection is', self.wbc)
            print('The rbc count after infection is', self.rbc)
            print('The platelet count after infection is', self.plat)
            print('The plasma level remains', self.plasma)
            print('..............................................')
            time.sleep(10)
            #os.system('cls')

        print('The infection has spread too much! Sorry :/')


    # method to start effect of antidote
    def apply_antidote(self):
        print('Antidote effect in action')
        self.t1.stop()

    def exitprogram(self):
        os.system('cls')
        sys.exit()
        return

    def userchoice(self):
        print("Enter '2' to apply antidote. \n Enter '3' to exit.")
        answer = input()
        if answer == '2':
            self.apply_antidote()
        if answer == '3':
            self.exitprogram()
        #if keyboard.is_pressed("3"):
        #    self.exitprogram()
        time.sleep(3)
        if answer != None:
            return
# main program starts here
h1 = Human()

print("Enter '1' to start infection. \n Enter '2' to apply antidote. \n Enter '3' to exit.")
h1.user_input()


