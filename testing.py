import json
import random
import os
import time

# # Change working directory to the script's folder
# script_directory = os.path.dirname(os.path.abspath(__file__))
# os.chdir(script_directory)

def load_questions(filename):
    """Load questions from a JSON file."""
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: Questions file not found!")
        exit()
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
        exit()

def select_category(questions):
    """Let the player choose a category."""
    while True:
        try:
            print("Choose a category:")
            categories = list(questions.keys())
            for i, category in enumerate(categories, start=1):
                print(f"{i}. {category.capitalize()}")
            
            choice = int(input("Enter category number: ")) - 1
            if 0 <= choice < len(categories):
                return categories[choice]
            else:
                print("Invalid choice. Please select a valid category number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def use_lifeline(question_data, used_lifelines):
    """Handle lifeline usage."""
    lifeline_options = {"1": "50-50", "2": "Hint"}
    available_lifelines = [key for key, value in lifeline_options.items() if value not in used_lifelines]
    
    if not available_lifelines:
        print("No lifelines left.")
        return None
    
    print("Available Lifelines:")
    for key in available_lifelines:
        print(f"{key}. {lifeline_options[key]}")
    
    choice = input("Choose a lifeline (1/2) or press Enter to skip: ")
    if choice in available_lifelines:
        used_lifelines.add(lifeline_options[choice])
        
        if choice == "1":  # 50-50 lifeline
            correct_answer = question_data["answer"]
            wrong_options = [opt for opt in question_data["options"] if opt != correct_answer]
            removed_options = random.sample(wrong_options, 2)
            return [opt for opt in question_data["options"] if opt not in removed_options]
        elif choice == "2":  # Hint lifeline
            print("Hint: The correct answer starts with", question_data["answer"][0])
    
    return None

def ask_question(question_data, used_lifelines):
    """Display a question and get user input with lifelines and timer."""
    print("\n" + question_data["question"])
    
    options = question_data["options"]
    random.shuffle(options)
    option_labels = ["a", "b", "c", "d"]
    option_map = {label: opt for label, opt in zip(option_labels, options)}
    
    for label, option in option_map.items():
        print(f"{label}. {option}")
    
    lifeline_used = use_lifeline(question_data, used_lifelines)
    if lifeline_used:
        print("Updated options after lifeline:")
        option_map = {label: opt for label, opt in zip(option_labels, lifeline_used)}
        for label, option in option_map.items():
            print(f"{label}. {option}")
    
    start_time = time.time()
    while True:
        try:
            answer = input("Your answer (a/b/c/d) or lifeline (1/2): ").strip().lower()
            if time.time() - start_time > 30:
                print("Time's up! You took too long.")
                return False
            if answer in option_map:
                return option_map[answer] == question_data["answer"]
            elif answer in {"1", "2"}:
                print("Lifeline already used or invalid input.")
            else:
                print("Invalid choice. Please enter a/b/c/d for options or 1/2 for lifelines.")
        except ValueError:
            print("Invalid input. Try again.")

def play_game():
    """Main function to run the game."""
    questions = load_questions("Questions.json")
    category = select_category(questions)
    
    levels = ["easy", "medium", "hard"]
    score_levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
    master_levels = {4, 9, 14}  # 5th, 10th, and 15th questions as checkpoints
    
    score = 0
    master_score = 0
    question_count = 0
    used_lifelines = set()
    
    for level in levels:
        level_questions = [q for q in questions[category] if q["difficulty"] == level]
        random.shuffle(level_questions)
        
        for question in level_questions:
            if question_count >= len(score_levels):
                break
            
            print(f"\nQuestion for ₹{score_levels[question_count]}")
            if ask_question(question, used_lifelines):
                score = score_levels[question_count]
                print("Correct! Your score:", score)
                
                if question_count in master_levels:
                    master_score = score  # Update master level score
            else:
                print("Wrong answer! Game Over.")
                print(f"You have secured Rs.{master_score} as your final reward.")
                return
            
            question_count += 1
    
    print("Congratulations! You have won ₹1 Crore!")

if __name__ == "__main__":
    play_game()