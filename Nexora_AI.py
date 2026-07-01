import random
from datetime import datetime

#Welcome screen
print("~" *50)
print("             Welcome to the Nexora AI            ")
print("~" *50)

name = input("\nBefore we begin, May I know your name please???")


# Asking User Name
print(f"\nHello {name}!!!!")
print("\nI'm a Nexora AI.")
print("\nAsk me anything and let's explore the answers together .")
print("\nType 'help' to see the help menu.")
print("\nType 'exit' to end the conversation.")

# Chat Loops
while True:
    user = input("\n You : ").lower()
    if user == "exit":
        print(f"\nGoodbye, {name}!")
        print("\nIt's always a pleasure talking to you. \n See you next time!")
        break
#HELP MENU
    elif user == "help":
        print("\n" +"="*50)
        print("              NEXORA AI HELP MENU💁🏻‍♀️")
        print("\n" +"="*50)

        print("👋 Greetings")
        print("   ➜ hi | hello | hey")
        print("   ➜ good morning | good afternoon")
        print("   ➜ good evening | good night")

        print("\n💪 Motivation")
        print("   ➜ motivate me")

        print("\n🧮 Smart Calculator")
        print("   ➜ calculator")

        print("\n📅 Date & Time")
        print("   ➜ date")
        print("   ➜ time")

        print("\n🤖 AI Corner")
        print("   ➜ ai fact")

        print("\n😂 Entertainment")
        print("   ➜ joke")

        print("\nℹ️ About Nexora AI")
        print("   ➜ what is your name")
        print("   ➜ about")

        print("\n🙏 Courtesy")
        print("   ➜ thank you")

        print("\n🚪 Exit")
        print("   ➜ exit")


        print("\n 💡More exciting features are coming soon.....Stay connected!!☺️")

        print("\n" + "=" * 50)

#GREETINGS

    elif user == "hi" or user == "hello" or user == "hey":
        print(f"\nHello {name}!")
        print("\n It's wonderful to have you here")
        print("\n How can I help you today?")

    elif user == "how are you?":
        print("\n I am doing great!")
        print("\n Thank you for asking.😊")

    elif user == "what is your name?":
        print(f"\n I am Nexora AI.")
        print("\n I have been created by Shruti using Python.💙")

    elif user == "good morning":
        print(f"Good Morning {name}!")
        print("Hope your day is filled with success.")

    elif user == "good evening":
        print(f"Good Evening {name}!")
        print("Hope you enjoyed your tea☕")

    elif user == "good afternoon":
        print(f"Good Afternoon {name}!")
        print("Hope your day is going well so far☺️")

    elif user == "good night":
        print(f"Good Night {name}!")
        print("Sleep well and recharge yourself🛌")

    elif user == "thank you":
        print(f"You're always welcome {name}!😊")

#MOTIVATION
    elif user == "motivate me":
        quotes = [ "🌟 Believe in yourself. Every expert was once a beginner.",
        "🚀 Success comes from consistent effort, not perfection.",
        "💪 You are stronger than you think.",
        "📚 Learn something new every day.",
        "🎯 Small progress is still progress.",
        "🔥 Stay focused. Stay determined. Success will follow.",
        "🌱 Keep growing, one step at a time.",
        "🧊Trust on the process"]

        print("\n 🤖Here is your motivational quote:")
        print(random.choice(quotes))


#CALCULATOR
    elif user == "calculator":

        print("\n🧮 Welcome to Nexora Calculator!")

        num1 = float(input("Enter first number : "))

        operator = input("Choose (+, -, *, /): ")

        num2 = float(input("Enter second number : "))

        if operator == "+":
            print(f"\n🤖 Answer = {num1 + num2}")

        elif operator == "-":
            print(f"\n🤖 Answer = {num1 - num2}")

        elif operator == "*":
            print(f"\n🤖 Answer = {num1 * num2}")

        elif operator == "/":

            if num2 == 0:
                print("❌ Division by zero is not possible.")

            else:
                print(f"\n🤖 Answer = {num1 / num2}")

        else:
            print("❌Invalid operator!")

        print("Calculation Completed Successfully!")


# Date and Time
    elif user =="time":
        current_time = datetime.now().strftime("%I:%M:%S %p")

        print("\n🕒 Current Time")
        print(f"🤖 {current_time}")

    elif user == "date":

        current_date = datetime.now().strftime("%d-%m-%Y")

        print("\n📅 Today's Date")
        print(f"🤖 {current_date}")

    elif user == "ai fact":

        facts = [
            "🤖 AI stands for Artificial Intelligence.",
            "🌍 AI is used in Google Maps, Netflix, and voice assistants.",
            "🚗 Self-driving cars use AI to understand roads and traffic.",
            "🎵 Music and movie recommendations often use AI.",
            "💬 Chatbots like Nexora AI are examples of conversational AI.",
            "📷 AI can recognize faces, objects, and even handwriting."
        ]

        print("\n🤖 AI Fact of the Moment:")
        print(random.choice(facts))

    elif user == "joke":

        jokes = [
            "😂 Why do programmers prefer dark mode? Because light attracts bugs!",
            "🤣 Why did Python break up with Java? Because it found someone less complicated!",
            "😆 There are only 10 kinds of people: those who understand binary and those who don't.",
            "😂 Debugging: Being the detective in a crime movie where you're also the criminal."
        ]

        print("\n🎭 Joke Time!")
        print(random.choice(jokes))

    elif user == "about":

        print("\n" + "=" * 50)
        print("🤖 NEXORA AI")
        print("=" * 50)

        print("Creator : Shruti Sinha")
        print("Language : Python")
        print("Version : 1.0")
        print("Type : Rule-Based Chatbot")
        print("Project : AI Internship")
        print("Made with ❤️ and lots of learning!")

        print("=" * 50)
    else:
        print("\n 🤖Sorry! I can't understand that.")


