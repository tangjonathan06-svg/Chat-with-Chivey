from random import randint

def action(r):
    if r.lower()=="walk walk":
        return("ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF ARF")
    elif r.lower()=="greenie":
        return("woof woof woof woof woof woof woof woof woof")
    elif r.lower()=="no more greenies":
        return("grrrrrr grrrrrr grrrrrr grrrrrr grrrrrr grrrrrr")
    else:
        return response()

def response():
    rand = randint(1,3)
    if rand==1:
        return("woof")
    if rand==2:
        return("arf arf")
    if rand==3:
        return("grrrrrr")
        
def kg():
    x1=True
    while(x1):
            r1=input("Do you want to keep interacting? ")
            if r1.lower()=="yes":
                action()
                kg()
            elif r1.lower()=="no":
                x1=False
            else: 
                print("that's not a reponse ")
                kg()
# x=True
# while(x):
#     r=input("Do you want to interact with Chive ")
#     if r.lower()=="yes":
#         action()
#         kg()
#         x=False
#     elif r.lower()=="no":
#         print("Don't be mean, talk to chive ")
#     else:
#         print("that's not a reponse ")

