import tkinter as tk
from tkinter import scrolledtext

def find_weird_divisibility(divisor, limit=30):
	results = [f"Checking divisibility patterns for {divisor}...\n"]
	for n in range(1, limit + 1):
		num_minus = 10**n - 1
		num_plus = 10**n + 1

		if num_minus % divisor == 0:
			results.append(f"10^{n} - 1 = {num_minus:,}  ÷ {divisor} = {num_minus // divisor:,}")
		if num_plus % divisor == 0:
			results.append(f"10^{n} + 1 = {num_plus:,}  ÷ {divisor} = {num_plus // divisor:,}")
	results.append("\nDone.")
	return "\n".join(results)

def run_check():
	try:
		divisor = int(divisor_entry.get())
		limit = int(limit_entry.get())
		output_box.delete(1.0, tk.END)
		output_box.insert(tk.END, find_weird_divisibility(divisor, limit))
	except ValueError:
		output_box.delete(1.0, tk.END)
		output_box.insert(tk.END, "Please enter valid integers.")

# --- GUI setup ---
root = tk.Tk()
root.title("Weird Divisibility Checker")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Divisor:").grid(row=0, column=0, padx=5)
divisor_entry = tk.Entry(frame, width=10)
divisor_entry.insert(0, "93")
divisor_entry.grid(row=0, column=1, padx=5)

tk.Label(frame, text="Limit:").grid(row=0, column=2, padx=5)
limit_entry = tk.Entry(frame, width=10)
limit_entry.insert(0, "30")
limit_entry.grid(row=0, column=3, padx=5)

run_button = tk.Button(frame, text="Check", command=run_check)
run_button.grid(row=0, column=4, padx=10)

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
output_box.pack(pady=10)

root.mainloop()