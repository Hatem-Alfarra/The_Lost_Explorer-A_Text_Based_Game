import time

def timed_interaction(prompt, passed_message, failed_messaged, time_given):
    start = time.time()
    lapsed = 0
    yet_to_interact = True
    while lapsed < time_given and yet_to_interact:
        word = (input("Quick! Type '" + prompt + "'\n")).strip().lower()
        end = time.time()
        lapsed = end - start
        if word == prompt and lapsed < yet_to_interact:
            yet_to_interact = False
            print(passed_message) # Change to special typing
        else:
            print(failed_messaged) # Change to special typing

message_1 = "You grabbed something in time!"
message_2 = "Your hand slipped and you fell!"

timed_interaction('grab', message_1, message_2, 4)


# while True:
#     now = time.time()
#     time = now - start
#     if time > 10:
#         break