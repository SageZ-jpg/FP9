import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Function to handle completion
def get_completion():
    prompt = prompt_box.get("1.0", tk.END).strip()
    if not prompt:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a prompt.")
        return

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-4"
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        output = response.choices[0].message.content.strip()
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, output)

    except Exception as e:
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, f"Error: {str(e)}")

# GUI Setup
window = tk.Tk()
window.title("Prompt Completion App")

tk.Label(window, text="Enter Prompt:").pack(pady=(10, 0))

prompt_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, width=60)
prompt_box.pack(padx=10, pady=(0, 10))

submit_button = tk.Button(window, text="Submit", command=get_completion)
submit_button.pack(pady=(0, 10))

tk.Label(window, text="Output:").pack()

output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, height=10, width=60)
output_box.pack(padx=10, pady=(0, 10))

window.mainloop()