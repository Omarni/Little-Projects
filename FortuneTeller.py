'''
Created on Dec 27, 2018

@author: user
'''
#The Really Bad Fortune Teller
import random

def SoulCareer(cc):
    if cc==1:
        Job_Ops=['Space Lawyer', 'Struggling Musician', 'Historian', 'Intergalactic Smuggler']
        return random.choice(Job_Ops)
    elif cc==2:
        Job_Ops=['Bartender', 'Realtor', 'Secret Agent', 'Unicorn Enthusiast']
        return random.choice(Job_Ops)
    elif cc==3:
        Job_Ops=['Reporter', 'Ghostbuster', 'Super Hero Costume Designer', 'Doctor']
        return random.choice(Job_Ops)
    elif cc==4:
        Job_Ops=['Peanut Pusher', 'Nail Biter', 'Dentist', 'Farmer']
        return random.choice(Job_Ops)
    elif cc==5:
        Job_Ops=['Fashion Designer', 'Professional Jellyfish Catcher', 'Dreamer', 'Police Officer']
        return random.choice(Job_Ops)
    elif cc==6:
        Job_Ops=['CEO', 'Architect', 'Toothfairy', 'Gamemaker']
        return random.choice(Job_Ops)
    elif cc==7:
        Job_Ops=['Data Scientist', 'Accountant','Wizard', 'Pillow Fluffer']
        return random.choice(Job_Ops)
    elif cc==8:
        Job_Ops=['Software Engineer', 'Chemist', 'Diving Instructor', 'Professional Binge Watcher']
        return random.choice(Job_Ops)
    elif cc==9:
        Job_Ops=['Actor', 'Cat Behavior Consultant', 'Shredded Cheese Authoritarian', 'Museum Security Guard']
        return random.choice(Job_Ops)
               
name=input("What's your name?")
ent= None 
ent=int(input("Hello, {} would you like to know you future? Enter 1 for ""Yes"" or 2 for ""Exit"".".format(name)))
print("Good choice. Here are some colors: \n1.Green \n2.Purple \n3.Black \n4.Grey \n5.Blue \n6.Red \n7.White \n8.Brown \n9.Yellow ")

while ent !=2:    
    if ent == 1:
        cc=int(input("What color matches you? (Pick a number: 1-9)"))
    
        if cc not in range (1,10):
            print('Invalid option.')
            break
        print("Well, according to nothing at all {}, it looks like you'll be a {}.".format(name,SoulCareer(cc)))   
        print("Would you like to try for something else?")
        if ent ==1:
            ent=int(input("1 for 'Yes' and 2 for 'No'.")) 
        if ent ==2:
            print("Thanks for playing.")
            break
    elif ent ==2:
        print("You don't want to know your future? I guess that's cool too.")
    else:
        print('Invalid option.Goodbye')
        break