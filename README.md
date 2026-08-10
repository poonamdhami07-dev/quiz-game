# 🎯 Quiz Game

A command-line based **Quiz Game** developed using Python. The game allows users to select a quiz category and difficulty level, answer randomly selected questions, and receive a score based on their performance.

## 📌 Project Overview

The Quiz Game contains questions from different categories and difficulty levels.

The user can:

- Select a quiz category
- Select a difficulty level
- Answer 10 questions
- Get **10 marks for every correct answer**
- View the final score and percentage
- Receive performance feedback
- Play the quiz again

## 📂 Categories

The quiz contains three categories:

1. **Science**
2. **History**
3. **General Knowledge**

## 🎚️ Difficulty Levels

Each category contains three difficulty levels:

- **Easy** – 10 questions
- **Medium** – 10 questions
- **Hard** – 10 questions

### Total Questions

```text
3 Categories × 3 Levels × 10 Questions
= 90 Questions
```

## ⭐ Scoring System

Each correct answer is worth **10 marks**.

| Correct Answers | Score |
| --------------: | ----: |
|              10 |   100 |
|               9 |    90 |
|               8 |    80 |
|               7 |    70 |
|               6 |    60 |
|               5 |    50 |
|               4 |    40 |
|               3 |    30 |
|               2 |    20 |
|               1 |    10 |
|               0 |     0 |

## 🏆 Performance Feedback

| Percentage | Feedback              |
| ---------: | --------------------- |
|    80–100% | Excellent!            |
|     60–79% | Very Good!            |
|     40–59% | Good! Keep Practicing |
|  Below 40% | Needs Improvement     |

## 🛠️ Technologies Used

- **Python**
- `random` module
- Lists
- Dictionaries
- Loops
- Conditional statements
- User input
- String methods

## 📁 Project Structure

```text
Day7/
│
├── quiz_game.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the terminal in the project folder and run:

```bash
python quiz_game.py
```

## 🎮 How to Play

### Step 1: Select Category

```text
Choose a category:

1. Science
2. History
3. General Knowledge
```

### Step 2: Select Difficulty

```text
Choose a level:

1. Easy
2. Medium
3. Hard
```

### Step 3: Answer Questions

The game displays 10 questions from the selected category and difficulty level.

```text
Question 1

What is the chemical symbol for water?

A. CO2
B. H2O
C. O2
D. NaCl

Your answer (A/B/C/D): B

Correct!
+10 Marks
```

### Step 4: View Result

At the end of the quiz:

```text
========================================
              RESULT
========================================

Category   : Science
Level      : Easy
Questions  : 10
Score      : 80 / 100
Percentage : 80%

Performance: Excellent!
```

### Step 5: Play Again

The game asks:

```text
Do you want to play again? (Y/N):
```

Enter **Y** to play again or **N** to exit.

## 📚 Concepts Practiced

This project helped practice:

- Variables
- Lists
- Dictionaries
- Functions/logic
- `for` loops
- `while` loops
- `if-elif-else`
- User input
- String manipulation
- Randomization using `random.shuffle()`
- Filtering data using conditions
- Score calculation
- Percentage calculation

## 🚀 Future Improvements

The project can be extended with:

- ⏱️ 10-second timer for each question
- 💾 Save high scores
- 👤 Player name
- 📊 Score history
- 🔊 Sound effects
- 🎨 Improved interface
- 🏅 Leaderboard
- ➕ More categories
- 📈 Difficulty-based scoring

## 👩‍💻 Author

**Poonam Dhami**

B.Tech Computer Science (Data Science) Student

---

⭐ This project is part of my Python learning journey and is created to practice programming concepts through hands-on projects.
