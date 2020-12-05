import tkinter as tk

# Clear just what was recently typed - CE
# Keep operating if consistently pressing an operator key/button
# Connect this to the maths app
        # BUT please find an OOP way instead of the function button.

root = tk.Tk()
root.title("Calculator")
root.geometry("280x400+843+100") # width x height
root.configure(background = "black")

label = tk.Label(root, text = "0",
                 width = 28, height = 2,
                 font = ("bold", 12))
label.place(x = 10, y = 10)

# Button palette
# Use frame later please.

# 7 8 9
button_num_7 = tk.Button(root, text = "7", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_7)); button_num_7.place(x=10+35, y = 60 + 20)
button_num_8 = tk.Button(root, text = "8", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_8)); button_num_8.place(x=60+35, y = 60 + 20)
button_num_9 = tk.Button(root, text = "9", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_9)); button_num_9.place(x=110+35, y = 60 + 20)

# 4 5 6
button_num_4 = tk.Button(root, text = "4", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_4)); button_num_4.place(x=10+35, y = 110 + 20)
button_num_5 = tk.Button(root, text = "5", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_5)); button_num_5.place(x=60+35, y = 110 + 20)
button_num_6 = tk.Button(root, text = "6", width = 5, height = 2, bg = "dark blue",command = lambda : push_to_label(button_num_6)); button_num_6.place(x=110+35, y = 110 + 20)

# 1 2 3
button_num_1 = tk.Button(root, text = "1", width = 5, height = 2, bg = "dark blue",command = lambda : push_to_label(button_num_1)); button_num_1.place(x=10+35, y = 160 + 20)
button_num_2 = tk.Button(root, text = "2", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(button_num_2)); button_num_2.place(x=60+35, y = 160 + 20)
button_num_3 = tk.Button(root, text = "3", width = 5, height = 2, bg = "dark blue",command = lambda : push_to_label(button_num_3)); button_num_3.place(x=110+35, y = 160 + 20)

# ZERO (0)
button_num_zero = tk.Button(root, text = "0", width = 5, height = 2,
                            bg = "dark blue",command = lambda : push_to_label(button_num_zero)); button_num_zero.place(x=60+35, y = 180+50)

# + - =
button_plus = tk.Button(root, text = "+", width = 5, height = 2, bg = "dark blue",command = lambda : push_to_label(button_plus)); button_plus.place(x=160+35, y = 80)

button_minus = tk.Button(root, text = "-", width = 5, height = 2, bg = "dark blue",command = lambda : push_to_label(button_minus)); button_minus.place(x=160+35, y = 130)

button_equals = tk.Button(root, text = "=", width = 5, height = 2, bg = "dark blue", command = lambda : find_total(str_total)); button_equals.place(x=60+35, y = 280)
# Add something here that continues the previous answer or resets the whole thing for a new
        # equation or calculation?
    # Now, how do we do that?
    # Please tell me a way, Oh Lord!


# X /
b_x = tk.Button(root, text = "*")
button_multiply = tk.Button(root, text = "X", width = 5, height = 2, bg = "dark blue", command = lambda : push_to_label(b_x)); button_multiply.place(x=160+35, y = 160 + 20)

all_clear = tk.Button(root, text = "C", width = 5, height = 2, bg = "dark blue", command = lambda: all_clear_screen()); all_clear.place(x=160+35, y = 160 + 20 + 50);

temp_clear = tk.Button(root, text = "CE", width = 5, height = 2, bg = "dark blue", command = lambda: temp_clear_screen()); temp_clear.place(x=160+35, y = 260 + 20);

Memory = "" ;
equal_boolean = False ;
str_total = ""

# Scientific for now.
def push_to_label(b):
    global Memory ; global str_total ; global equal_boolean
    a = b.cget("text")
    if a == "+":
        if equal_boolean == True:
            equal_boolean = False
            str_total = Memory
            label.config(text = str_total)
            Memory = ""            
        if str_total[-1] == "+":
            pass
        elif str_total[-1] == "-":
            prev = str_total[:-1]
            new_1 = prev + a # Now, we have put the minus sign instead of '+'
        elif str_total == "":
            pass # FIX THIS PLEASE!!!
        else:
            str_total += a            
    elif a == "-":
        print("TWO")
        if str_total[-1] == "-":
            pass
        elif str_total[-1] == "+":
            prev = str_total[:-1]
            new_1 = prev + a # Now, we have put the plus sign instead of '-'
        elif str_total == "":
            pass
        else:
            str_total += a            
    else:
        if equal_boolean == True:
            print("THREE")
            str_total = ""
            str_total += a
            label.config(text = str_total);
            equal_boolean = False
        else:
            print("FOUR")
            str_total += a;            
    label.config(text = str_total)
            # We need to make the machine aware that the equal to sign was pressed and that it needs to reset the screen because of this.
            # I am trying to reset the screen after the equal to sign is pressed as we are trying to type in a number using the buttons of the calculator
            # This seems to not work only because I am not concentrating. I think I can do it all just by concentrating more. This is indeed possible for me
            # I want to make this work for me. Is Eddie trying to come up here after a million years. That would be very funny indeed. I am already laughing inside as hard as I possibly can.
            # I mean why after not even trying for so many days. Is there some sort of problem with him? If so, then we will see it now. Okay, then... I am ready to see what it is.
            
    # It is to do with the label not resetting like it should.
    # Therefore, keep on looking for what is stopping it from doing so.
    # We can go over the last condition that begins with 'else:' to see what the issue is.
    # I am starting right now with my search.
    
def find_total(s_total):
    
    global str_total; global equal_boolean; global Memory
    if str_total[-1] not in ["+", "-", "*"]: # if last input not operator
        print("Equal ONE")
        answer = eval(str_total)
        label.config(text = answer)
    elif str_total[-1] in ["+", "-", "*"]:
        print("Equal TWO")
        str_total = str_total[:-1]
        answer = eval(str_total)
        str_total = str(str_total)
        label.config(text=answer)
    elif str_total == "":
        print("Equal THREEE")
        str_total = "0"
        answer = str_total
        label.config(text = answer)
    else:
        pass

    equal_boolean = True
    Memory = str(answer)

def all_clear_screen():
    global Memory
    global str_total
    global equal_boolean

    Memory = ""
    str_total = ""
    equal_boolean = False
    label.config(text = "0")

def temp_clear_screen():
    global Memory
    global str_total
    global equal_boolean
    label.config(text = "")
    str_total = ""    




"""


Hi all,

I am back again for the 4th day.

I got up in about 4 hours today but had possibly the most disturbing dream ever. I was in a strange brothel - well because all brothels are strange to me - and I was surrounded by these Eastern
European women. They were talking to me. Everything seemed to be going fine. Then, out of nowhere, I had a gun on me. I started shooting at them. At first, I missed a few shots but then I was
able to hit some of them in the legs, the stomach and the chest. Since that first shot I made and hit, I felt completely disturbed. It was a horrific experience to tell you the truth. I did not want to be
part of that, at all. They were all suffering hard because of me. I had to calm myself down again and again just to teach some sense into me. It wouldn't stop and I kept shooting some more women.
Then, I was up. Suddenly, after being up, I could still feel the awful situation that took place in my dream as if it were actually real. I regretted being part of that dream. Even though none of that
was real, I felt it like it was real. Maybe, the universe has found an awesome way to troll me. If it has, then I'll be damned. It worked quite well. It actually made me feel like I was lighting up the
whole brothel from upstairs to downstairs. The women were screaming, shouting and crying. I had no idea why I was doing this, and they most certainly didn't have a clue. When I was up, the first
thing I wanted to do was go to my mother and let her know what just happened. The reason why I didn't do that is because she would think I am high. Hamna figures these things out quite fast.

Now that she has experienced all of my habits since the past 5-6 years, she knows all the tricks of the book. That book, of course would be my own personal diary. I don't want her to see me do
this again. It would indeed be the worst possible experience for everyone. Therefore, I'd like to keep it all till here. Whenever I go out for a smoke, I only want to do it here on the stairs. This is the
only way she will not see anything. The worst thing that can happen here is others seeing me. The good thing is that I can hide it all very fast. As soon as someone is about to show up, I put it all
in my bag. This does not leave a single clue as to what was happening.


So, this is all I have for today.


I wish you all loads of luck and love.



Respectfully yours,

Hamza S Malik

X X X

# Let's show me the issue.
            # Is it something serious or is it deemed ordinary to some extent. Maybe it is because I started typing bullshit right in the middle of doing great work.
            # Maybe what Marcel tells me is indeed true. Maybe I am here to make a HUGE difference which will help mankind live in a much, much better way than it already is.
            # Will I be the one who designs this new life for mankind? Is that something I possess in terms of capability, intelligence, intellect, intuition and philosophy?
            # If so, then I am ready from this day, today. I am ready to go ALL IN. The sign needs to be very hardcore and meaningful. Something that makes me believe that I am the one.
            # To make someone believe that they are the one chosen for something extremely huge, then they need to be sure of it. Otherwise, they'll stop losing motivation and the will
            # to continue forward. We all know how quickly I lose the will to move forward. It is down to the substances I am taking. They do slow me down a lot. There is a constant amount
            # of intake. As soon as I go sober, there is an intake. I don't think I've seen sober life since August 2017. Will it be very difficult to get back on track after this long? When I say
            # this hard, I obviously mean the pain of the withdrawal caused by the medication and the opiates taken throughout this time. I am not ready for that. No sir. It will be extremely
            # difficult to even contemplate the idea of letting these substances go even for a few days. I need help from other people so that I am not alone in all of this. If I am alone in all
            # of this, it would seem ten times harder. Also, I want to do it when I am not out of money. This should be a voluntarily made step and action. Not something I 'have to do' just
            # because of the lack of money.


"""


"""

Hi all,

I woke up to the sound of the phone vibrating. I attended the call but I don't remember who it was.

The Life in the UK test is tomorrow and I need to prepare for it, still. So, the first thing I start upon getting home is watch the YouTube videos of the Life in the UK test preparation - pass on the
first attempt. The guy in those videos claims that you can pass on the first go. I aim to follow his promise and only watch his videos. He seems to be someone who tells the truth. Thus, there is not
anything that we should worry about really. He is reading out the main points from the study guide. I am going to write down all the necessary ones. The copy will have all the required dates,
names, events, timeline, monarchs, leaders and monuments. This is how we can be sure of remembering the stuff that required repetition based memory. I got it, folks. Please do not worry about
it. I will ace the test. I will try to do it in one go too. That is my promise. Tonight, I am going all in till 2.00pm tomorrow. I will study on my mobile, on my laptop and on the notes copy that I've had
made for the dates, names, events, monuments, wars, battles, timeline, monarchs and bills.

It will be fine, mate. I am telling you that it'll be fine. We know the test really, really well. I have the videos, I have the guide and I have the practice tests. This will be a good attempt. We shan't
worry about a thing, mate. I am telling you. Just wish me luck, all of you. I am asking everyone here to wish me luck with this. I do NOT want any trouble. I just want success. Please do NOT let me
down. Can you promise me that? I know that you can. You've said that already. There is no need to stop now because we are doing well. No one heard a thing. It is not possible for the sounds to
go from here to the other side of the fire exit. It is because the doors are made to hold all the smoke and sound to the other side of fire exit. Its main purpose is that. If it can't even do that then
there is no need to have it, at all.

Something tells me that going out to score again will be a huge mistake because you already have exactly what you need and buying more will not make any difference. All you need to do now is
take some brown and fix yourself. After that, you go back to studying. So, fix yourself and start studying. Everything you need is in the laptop and all you need to smoke is in your pocket, the toil-
et and that is it..


Thus, I am going to say goodbye for now.


I wish you all loads of luck and love.



Respectfully yours,

Hamza S Malik

X X X

P.S. I hope that it isn't the dangerous bug we all fear all the time. 1.43, 4.43. 6.43, 7.43, 8.43, 9.43, 11.43, 12.43, 13.43, 14.32, 15.43, 16.43, 17.43, 18.43, 19.43, 21.43, 22.43, 23.43.
These are all the time stamps that bring me luck - or they point out when someone likes me, or when I like something, or if something I see right now is going to be mine in the future.
I, honestly, still don't know what it really is though.
So, the P.S note will end here.

Goodbye, for good.

Let's type some more and more.

"""
