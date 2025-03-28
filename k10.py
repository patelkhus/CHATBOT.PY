import random

responses = {
    "who won the last world cup": "Australia won the ICC Cricket World Cup 2023.",
    "who is the best batsman": "There are many great batsmen like Virat Kohli, Babar Azam, and Steve Smith.",
    "who is the best bowler": "There are many great bowlers like Jasprit Bumrah",
    "who is the best team": "There are many great teams like India, Australia, and South Affrica",
    "who is the best player": "There are many great players like Virat Kohli,Sachin Tendulkar, and Rohit Sharma",
    "who is the best captain": "There are many great captains like Virat Kohli,Rohit sharma",
    "who is the best all rounder": "There are many great all rounders like Hardik Pandya, Kapil Dev and Ravindra Jadeja",
    "what is the highest score in t20": "The highest individual T20 score is 175* by Chris Gayle.",
    "who has the most wickets in test cricket": "Muttiah Muralitharan holds the record with 800 wickets."
}

def chatbot():
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print("Khush:", responses[user_input])
        else:
            if user_input == "quit":
                break

            else:
                print("Khush: I don't understand that")

chatbot()