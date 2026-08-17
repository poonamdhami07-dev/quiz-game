"""Project 3: Quiz Game 
Develop a quiz game that asks users a series of questions from different 
categories (e.g., science, history, general knowledge). The game should 
keep track of the user's score and provide feedback on their performance. 
Requirements: 
1. Store quiz questions in a data structure (e.g., list of dictionaries). 
2. Randomly select questions for each quiz session. 
3. Keep track of the user's score and display it at the end of the quiz. 
4. Allow users to choose the quiz category before starting. 
5. Implement a timer for each question."""

import random

questions = [

    # SCIENCE - EASY

    {
        "category": "Science",
        "level": "Easy",
        "question": "What is the chemical symbol for water?",
        "options": ["A. CO2", "B. H2O", "C. O2", "D. NaCl"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "Which gas do humans need to breathe?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Hydrogen", "D. Carbon Dioxide"],
        "answer": "A"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "How many legs does a spider have?",
        "options": ["A. 6", "B. 8", "C. 10", "D. 12"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "Which organ helps us to see?",
        "options": ["A. Ear", "B. Nose", "C. Eye", "D. Tongue"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "What is the natural satellite of Earth?",
        "options": ["A. Sun", "B. Mars", "C. Moon", "D. Venus"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "Which part of a plant absorbs water?",
        "options": ["A. Flower", "B. Root", "C. Leaf", "D. Stem"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "How many planets are in our solar system?",
        "options": ["A. 7", "B. 8", "C. 9", "D. 10"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "Which sense organ is used for hearing?",
        "options": ["A. Eye", "B. Nose", "C. Ear", "D. Skin"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Easy",
        "question": "What force pulls objects toward Earth?",
        "options": ["A. Friction", "B. Gravity", "C. Magnetism", "D. Electricity"],
        "answer": "B"
    },



    # SCIENCE - MEDIUM

    {
        "category": "Science",
        "level": "Medium",
        "question": "How many bones are there in an adult human body?",
        "options": ["A. 206", "B. 208", "C. 210", "D. 212"],
        "answer": "A"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "What is the boiling point of water at sea level?",
        "options": ["A. 50°C", "B. 75°C", "C. 100°C", "D. 150°C"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "Which organ pumps blood throughout the body?",
        "options": ["A. Brain", "B. Heart", "C. Liver", "D. Kidney"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "Which vitamin is produced by the body when exposed to sunlight?",
        "options": ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
        "answer": "D"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "What is the process by which plants make their food?",
        "options": ["A. Respiration", "B. Photosynthesis", "C. Digestion", "D. Transpiration"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "Which blood cells fight infections?",
        "options": ["A. Red blood cells", "B. White blood cells", "C. Platelets", "D. Plasma"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Ag", "B. Au", "C. Gd", "D. Go"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "Which planet has the most prominent ring system?",
        "options": ["A. Mars", "B. Saturn", "C. Venus", "D. Mercury"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "What is the largest organ in the human body?",
        "options": ["A. Heart", "B. Liver", "C. Skin", "D. Brain"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Medium",
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "B"
    },

    # SCIENCE - HARD
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Cytoplasm"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the SI unit of electrical resistance?",
        "options": ["A. Volt", "B. Ampere", "C. Ohm", "D. Watt"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "Which particle has a negative electric charge?",
        "options": ["A. Proton", "B. Neutron", "C. Electron", "D. Photon"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the approximate speed of light?",
        "options": [
            "A. 3 × 10⁸ m/s",
            "B. 3 × 10⁶ m/s",
            "C. 3 × 10⁵ m/s",
            "D. 3 × 10⁴ m/s"
        ],
        "answer": "A"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the pH of pure water at 25°C?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "Which law states that pressure and volume are inversely proportional at constant temperature?",
        "options": ["A. Boyle's Law", "B. Newton's Law", "C. Ohm's Law", "D. Faraday's Law"],
        "answer": "A"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the atomic number of carbon?",
        "options": ["A. 4", "B. 6", "C. 8", "D. 12"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "Which scientist proposed the theory of relativity?",
        "options": ["A. Newton", "B. Einstein", "C. Darwin", "D. Bohr"],
        "answer": "B"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "What is the SI unit of frequency?",
        "options": ["A. Hertz", "B. Joule", "C. Newton", "D. Pascal"],
        "answer": "A"
    },
    {
        "category": "Science",
        "level": "Hard",
        "question": "Which particle has no electric charge?",
        "options": ["A. Proton", "B. Electron", "C. Neutron", "D. Ion"],
        "answer": "C"
    },


   
    # HISTORY - EASY
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was the first President of India?",
        "options": ["A. Jawaharlal Nehru", "B. Rajendra Prasad", "C. Sardar Patel", "D. B. R. Ambedkar"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "In which year did India become independent?",
        "options": ["A. 1945", "B. 1946", "C. 1947", "D. 1950"],
        "answer": "C"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was known as the Iron Man of India?",
        "options": ["A. Gandhi", "B. Nehru", "C. Sardar Patel", "D. Bhagat Singh"],
        "answer": "C"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was the first Prime Minister of India?",
        "options": ["A. Rajendra Prasad", "B. Jawaharlal Nehru", "C. Sardar Patel", "D. Lal Bahadur Shastri"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A. Mahatma Gandhi", "B. Nehru", "C. Patel", "D. Bose"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was the queen of Jhansi?",
        "options": ["A. Rani Lakshmibai", "B. Rani Durgavati", "C. Noor Jahan", "D. Razia Sultan"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who built the Taj Mahal?",
        "options": ["A. Akbar", "B. Shah Jahan", "C. Babur", "D. Aurangzeb"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who discovered the sea route to India from Europe?",
        "options": ["A. Columbus", "B. Vasco da Gama", "C. Magellan", "D. Cook"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was the founder of Buddhism?",
        "options": ["A. Mahavira", "B. Gautama Buddha", "C. Ashoka", "D. Chanakya"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Easy",
        "question": "Who was the founder of the Sikh religion?",
        "options": ["A. Guru Nanak", "B. Guru Gobind Singh", "C. Guru Arjan", "D. Guru Tegh Bahadur"],
        "answer": "A"
    },


    # HISTORY - MEDIUM
    {
        "category": "History",
        "level": "Medium",
        "question": "Who led the Dandi March?",
        "options": ["A. Mahatma Gandhi", "B. Bhagat Singh", "C. Subhash Bose", "D. Patel"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who founded the Maurya Empire?",
        "options": ["A. Ashoka", "B. Chandragupta Maurya", "C. Akbar", "D. Harsha"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who was the founder of the Gupta Empire?",
        "options": ["A. Sri Gupta", "B. Chandragupta II", "C. Samudragupta", "D. Ashoka"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who gave the slogan 'Do or Die'?",
        "options": ["A. Nehru", "B. Gandhi", "C. Bose", "D. Patel"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "When did the Quit India Movement begin?",
        "options": ["A. 1930", "B. 1935", "C. 1942", "D. 1947"],
        "answer": "C"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who was known as the Napoleon of India?",
        "options": ["A. Samudragupta", "B. Ashoka", "C. Akbar", "D. Harsha"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who was the last Mughal emperor?",
        "options": ["A. Akbar", "B. Shah Jahan", "C. Bahadur Shah Zafar", "D. Aurangzeb"],
        "answer": "C"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who founded the Indian National Congress?",
        "options": ["A. A.O. Hume", "B. Gandhi", "C. Nehru", "D. Tilak"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Who was the first woman ruler of the Delhi Sultanate?",
        "options": ["A. Razia Sultan", "B. Nur Jahan", "C. Rani Lakshmibai", "D. Chand Bibi"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Medium",
        "question": "Which movement was launched in 1930 by Gandhi?",
        "options": ["A. Quit India", "B. Civil Disobedience", "C. Non-Cooperation", "D. Swadeshi"],
        "answer": "B"
    },


    # HISTORY - HARD

    {
        "category": "History",
        "level": "Hard",
        "question": "Who wrote the Arthashastra?",
        "options": ["A. Kalidasa", "B. Chanakya", "C. Tulsidas", "D. Banabhatta"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who founded the Mughal Empire in India?",
        "options": ["A. Akbar", "B. Humayun", "C. Babur", "D. Shah Jahan"],
        "answer": "C"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "In which year did the Battle of Plassey take place?",
        "options": ["A. 1757", "B. 1764", "C. 1857", "D. 1947"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who was the founder of the Maratha Empire?",
        "options": ["A. Shivaji Maharaj", "B. Bajirao I", "C. Balaji Vishwanath", "D. Sambhaji"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who introduced the Permanent Settlement in Bengal?",
        "options": ["A. Lord Dalhousie", "B. Lord Cornwallis", "C. Lord Curzon", "D. Lord Wellesley"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who wrote 'Discovery of India'?",
        "options": ["A. Gandhi", "B. Nehru", "C. Patel", "D. Ambedkar"],
        "answer": "B"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who was the first Governor-General of independent India?",
        "options": ["A. Lord Mountbatten", "B. Rajagopalachari", "C. Nehru", "D. Wavell"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Which treaty ended the First Anglo-Maratha War?",
        "options": ["A. Treaty of Salbai", "B. Treaty of Lahore", "C. Treaty of Seringapatam", "D. Treaty of Bassein"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who was the founder of the Slave Dynasty?",
        "options": ["A. Qutb-ud-din Aibak", "B. Iltutmish", "C. Balban", "D. Alauddin Khilji"],
        "answer": "A"
    },
    {
        "category": "History",
        "level": "Hard",
        "question": "Who was the first Indian woman president of the Indian National Congress?",
        "options": ["A. Sarojini Naidu", "B. Annie Besant", "C. Sucheta Kriplani", "D. Vijayalakshmi Pandit"],
        "answer": "B"
    },


    # GENERAL KNOWLEDGE - EASY
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "What is the national animal of India?",
        "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Peacock"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "Which is the largest ocean?",
        "options": ["A. Indian", "B. Atlantic", "C. Pacific", "D. Arctic"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "How many colors are there in a rainbow?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "What is the currency of India?",
        "options": ["A. Dollar", "B. Rupee", "C. Pound", "D. Yen"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "Which is the fastest land animal?",
        "options": ["A. Lion", "B. Tiger", "C. Cheetah", "D. Horse"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "How many months are there in a year?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Easy",
        "question": "Which is the largest continent?",
        "options": ["A. Africa", "B. Europe", "C. Asia", "D. Australia"],
        "answer": "C"
    },


    # GENERAL KNOWLEDGE - MEDIUM

    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["A. China", "B. Japan", "C. Korea", "D. Thailand"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "How many players are there in a cricket team?",
        "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which is the largest desert in the world?",
        "options": ["A. Sahara", "B. Gobi", "C. Antarctic Desert", "D. Thar"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which is the longest river in India?",
        "options": ["A. Yamuna", "B. Ganga", "C. Godavari", "D. Narmada"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Who invented the telephone?",
        "options": ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. James Watt"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which country hosted the first modern Olympic Games?",
        "options": ["A. France", "B. Greece", "C. Italy", "D. Germany"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which is the largest mammal?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Shark"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which country has the largest population?",
        "options": ["A. India", "B. USA", "C. China", "D. Russia"],
        "answer": "A"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which instrument is used to measure temperature?",
        "options": ["A. Barometer", "B. Thermometer", "C. Hygrometer", "D. Ammeter"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Medium",
        "question": "Which sport is associated with Wimbledon?",
        "options": ["A. Cricket", "B. Football", "C. Tennis", "D. Hockey"],
        "answer": "C"
    },


    # GENERAL KNOWLEDGE - HARD

    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which is the smallest country in the world?",
        "options": ["A. Monaco", "B. Vatican City", "C. Maldives", "D. Singapore"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "What is the currency of Japan?",
        "options": ["A. Yuan", "B. Won", "C. Yen", "D. Dollar"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which is the longest river in the world?",
        "options": ["A. Amazon", "B. Nile", "C. Ganges", "D. Yangtze"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which country has the most time zones?",
        "options": ["A. Russia", "B. USA", "C. France", "D. China"],
        "answer": "C"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Who was the first person to reach the South Pole?",
        "options": ["A. Roald Amundsen", "B. Robert Scott", "C. Edmund Hillary", "D. James Cook"],
        "answer": "A"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which is the deepest ocean trench?",
        "options": ["A. Tonga Trench", "B. Mariana Trench", "C. Java Trench", "D. Puerto Rico Trench"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "options": ["A. France", "B. Germany", "C. Spain", "D. Italy"],
        "answer": "A"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which is the world's largest island?",
        "options": ["A. Greenland", "B. Australia", "C. Borneo", "D. Madagascar"],
        "answer": "A"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which country is known as the Land of a Thousand Lakes?",
        "options": ["A. Sweden", "B. Finland", "C. Norway", "D. Iceland"],
        "answer": "B"
    },
    {
        "category": "General Knowledge",
        "level": "Hard",
        "question": "Which is the largest internal organ in the human body?",
        "options": ["A. Heart", "B. Brain", "C. Liver", "D. Kidney"],
        "answer": "C"
    }
]

print("=" * 50)
print("       WELCOME TO QUIZ GAME")
print("=" * 50)

while True:

    print("\nChoose a category:")
    print("1. Science")
    print("2. History")
    print("3. General Knowledge")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        category = "Science"

    elif choice == "2":
        category = "History"

    elif choice == "3":
        category = "General Knowledge"

    elif choice.lower() == "exit":
        print("Exiting the quiz game. Goodbye!")
        break

    else:
        print("Invalid category!")
        continue

    print("\nChoose a level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    level_choice = input("\nEnter your level: ").strip()

    if level_choice == "1":
        level = "Easy"

    elif level_choice == "2":
        level = "Medium"

    elif level_choice == "3":
        level = "Hard"

    else:
        print("Invalid level!")
        continue

    selected_questions = []

    for question in questions:

        if question["category"] == category and question["level"] == level:
            selected_questions.append(question)


    # Randomize question order
    random.shuffle(selected_questions)

    print("\n" + "=" * 40)
    print("Category:", category)
    print("Level:", level)
    print("Total Questions:", len(selected_questions))
    print("Marks per correct answer: 10")
    print("=" * 40)


    score = 0


    for number, question in enumerate(selected_questions, start=1):

        print("\n------------------------------")
        print("Question", number)
        print("------------------------------")

        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            user_answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")


        if user_answer == question["answer"]:

            print("Correct!")
            print("+10 Marks")

            score += 10

        else:

            print("Wrong!")
            print("Correct answer:", question["answer"])

        total_marks = len(selected_questions) * 10

    percentage = (score / total_marks) * 100


    print("\n" + "=" * 40)
    print("              RESULT")
    print("=" * 40)

    print("Category   :", category)
    print("Level      :", level)
    print("Questions  :", len(selected_questions))
    print("Score      :", score, "/", total_marks)
    print("Percentage :", f"{percentage:.0f}%")

    if percentage >= 80:
        print("Excellent!")

    elif percentage >= 60:
        print("Very Good!")

    elif percentage >= 40:
        print("Good! Keep Practicing.")

    else:
        print("Keep Practicing! You can do better.")

    again = input("\nDo you want to play again? (Yes/No): ").strip().upper()

    if again != "YES" and again != "Y":

        print("\n" + "=" * 40)
        print("       THANK YOU FOR PLAYING!")
        print("=" * 40)
        print("Goodbye!")

        break
