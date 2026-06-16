import re
import datetime

def get_time():
    return f"Current time is: {datetime.datetime.now().strftime('%I:%M %p')}"

def get_date():
    return f"Today is: {datetime.datetime.now().strftime('%A, %B %d, %Y')}"

patterns = [

    ("hello|hi|hey|hy|howdy|what's up|wassup",
     "Hey there! 😊 How can I help you today?"),

    ("bye|exit|quit|goodbye|see you|cya",
     "Bye! Have a wonderful day! 👋"),

    ("how are you|hru|how r u|are you okay|you good",
     "I'm doing great, thanks for asking! How about you? 😄"),

    ("what is your name|who are you|your name",
     "I'm ChatBot, your virtual assistant! 🤖"),

    ("what is ai|define ai|explain ai",
     "AI stands for Artificial Intelligence — technology that enables machines to simulate human thinking and problem-solving!"),

    ("what is machine learning|what is ml",
     "Machine Learning is a subset of AI where machines learn from data to improve their performance over time!"),

    ("what is deep learning|what is dl",
     "Deep Learning is a subset of Machine Learning that uses neural networks with many layers to learn complex patterns!"),

    ("what is python|tell me about python",
     "Python is a popular, easy-to-learn programming language widely used in AI, data science, and web development!"),

    ("how old are you|your age|when were you created",
     "I was just created recently! I'm brand new and ready to help. 🚀"),

    ("help|what can you do|your features|commands",
     "I can answer questions about AI, ML, Python, tell jokes, show time, and more! Just ask me anything 😊"),

    ("tell me a joke|joke|make me laugh|say something funny",
     "Why do programmers prefer dark mode? Because light attracts bugs! 😂"),

    ("who created you|who made you|your creator|who built you",
     "I was created by a passionate AI & DS student! 💡"),

    ("motivate me|give me motivation|inspire me|i am sad|feeling low",
     "You're doing amazing! Every expert was once a beginner. Keep going! 💪🔥"),

    ("favorite programming language|best language",
     "Python all the way! It's simple, powerful, and perfect for AI. 🐍"),

    ("thank you|thanks|thx|thank u",
     "You're welcome! Happy to help anytime 😊"),

    ("weather|how is the weather",
     "I don't have live weather access, but you can check weather.com! 🌤️"),
]

total_messages   = 0
matched_messages = 0
unknown_inputs   = []


def get_response(user_input):
    global matched_messages

    if re.search("what time is it|current time|time now", user_input, re.IGNORECASE):
        matched_messages += 1
        return get_time()
    
    if re.search("what is today|today's date|current date|what day is it", user_input, re.IGNORECASE):
        matched_messages += 1
        return get_date()
    
    for pattern, response in patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            matched_messages += 1
            return response
    unknown_inputs.append(user_input)
    return "Hmm, I didn't understand that. Type 'help' to see what I can do!"

def show_stats():
    print(f"  Total messages    : {total_messages}")
    print(f"  Matched responses : {matched_messages}")
    print(f"  Unknown inputs    : {len(unknown_inputs)}")
    if unknown_inputs:
        print(f"  Unrecognized      : {unknown_inputs}")
    print("────────────────────────────────────────\n")

print("=" * 45)
print("       Welcome to ChatBot 🤖")
print("  Type 'help' to see what I can do")
print("  Type 'stats' to see session stats")
print("  Type 'bye' to exit")
print("=" * 45)

while True:
    user_input = input("\nYou: ").strip()
    if not user_input:
        print("Bot: Please type something!")
        continue
    total_messages += 1
    if user_input.lower() in ["bye", "exit", "quit", "goodbye"]:
        print("Bot: Bye! Have a nice day! 👋")
        show_stats()
        break
    elif user_input.lower() == "stats":
        show_stats()
    else:
        print(f"Bot: {get_response(user_input)}")
