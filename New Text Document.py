import json
import random
import os
import tkinter as tk
from tkinter import messagebox

# Change working directory to script's location
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati (KBC)")
        self.root.geometry("600x400")
        
        self.questions = self.load_questions("Questions.json")
        self.selected_category = None
        self.current_question = None
        self.previous_questions = []  # Stores asked questions to avoid repetition
        self.used_lifelines = set()
        self.score = 0
        self.question_count = 0

        self.setup_home_screen()

    def load_questions(self, filename):
        """Load questions from a JSON file."""
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "Questions file not found!")
            exit()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format in the file!")
            exit()
    
    def setup_home_screen(self):
        """Display the category selection screen."""
        self.clear_screen()
        tk.Label(self.root, text="Choose a Category", font=("Arial", 16, "bold")).pack(pady=20)
        
        for category in self.questions.keys():
            tk.Button(self.root, width=30, text=category.capitalize(), font=("Arial", 14), 
                      command=lambda c=category: self.start_game(c)).pack(pady=5)
    
    def start_game(self, category):
        """Start the quiz by selecting a category."""
        self.selected_category = category
        self.question_count = 0
        self.score = 0
        self.previous_questions = []  # Reset previous questions
        self.used_lifelines = set()
        
        self.display_question()

    def display_question(self):
        """Display a new question ensuring no repeats."""
        available_questions = [q for q in self.questions[self.selected_category] if q not in self.previous_questions]
        
        if not available_questions or self.question_count >= 15:
            self.show_final_result()
            return
        
        self.current_question = random.choice(available_questions)
        self.previous_questions.append(self.current_question)  # Store asked question
        self.question_count += 1

        self.clear_screen()
        
        tk.Label(self.root, text=f"Question {self.question_count}", font=("Arial", 14, "bold")).pack(pady=10)
        tk.Label(self.root, text=self.current_question["question"], font=("Arial", 12), wraplength=500).pack(pady=10)
        
        self.option_buttons = []
        random.shuffle(self.current_question["options"])
        
        for option in self.current_question["options"]:
            btn = tk.Button(self.root, text=option, width=30, font=("Arial", 12),
                            command=lambda opt=option: self.check_answer(opt))
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        # Lifeline Buttons
        tk.Button(self.root, text="50-50", font=("Arial", 12), command=self.use_5050).pack(side=tk.LEFT, padx=20, pady=10)
        tk.Button(self.root, text="Hint", font=("Arial", 12), command=self.use_hint).pack(side=tk.RIGHT, padx=20, pady=10)

        # Score label (always visible)
        self.score_label = tk.Label(self.root, text=f"Score: Rs.{self.score}", font=("Arial", 14, "bold"))
        self.score_label.pack(side=tk.BOTTOM, pady=10)  # Always at the bottom

    def check_answer(self, selected_option):
        """Check if the selected answer is correct."""
        if selected_option == self.current_question["answer"]:
            self.score += 1000 * self.question_count  # Increasing rewards
            self.display_question()
        else:
            self.show_final_result()

    def use_5050(self):
        """50-50 Lifeline: Remove two incorrect options."""
        if "50-50" in self.used_lifelines:
            messagebox.showwarning("Lifeline Used", "You have already used this lifeline.")
            return
        
        self.used_lifelines.add("50-50")
        correct_answer = self.current_question["answer"]
        wrong_options = [opt for opt in self.current_question["options"] if opt != correct_answer]
        removed_options = random.sample(wrong_options, 2)

        for btn in self.option_buttons:
            if btn.cget("text") in removed_options:
                btn.config(state=tk.DISABLED)  # Disable the wrong options

    def use_hint(self):
        """Hint Lifeline: Show the first letter of the correct answer."""
        if "Hint" in self.used_lifelines:
            messagebox.showwarning("Lifeline Used", "You have already used this lifeline.")
            return
        
        self.used_lifelines.add("Hint")
        hint_text = f"Hint: The correct answer starts with '{self.current_question['answer'][0]}'"
        messagebox.showinfo("Hint", hint_text)

    def show_final_result(self):
        """Show final result in a single window and quit the game."""
        self.clear_screen()
        tk.Label(self.root, text="Game Over!", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text=f"You won ₹{self.score}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Exit", font=("Arial", 14), command=self.root.quit).pack(pady=20)

    def clear_screen(self):
        """Remove all widgets from the window."""
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()
