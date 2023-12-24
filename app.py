import tkinter as tk
from tkinter import messagebox

class SbiDepositForm:
    def __init__(self, master):
        self.master = master
        master.title("SBI Deposit Form")

        # Labels
        self.label_account_number = tk.Label(master, text="Account Number:")
        self.label_amount = tk.Label(master, text="Deposit Amount:")

        # Entry widgets
        self.entry_account_number = tk.Entry(master)
        self.entry_amount = tk.Entry(master)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)

        # Grid layout
        self.label_account_number.grid(row=0, column=0, padx=10, pady=10)
        self.label_amount.grid(row=1, column=0, padx=10, pady=10)
        self.entry_account_number.grid(row=0, column=1, padx=10, pady=10)
        self.entry_amount.grid(row=1, column=1, padx=10, pady=10)
        self.submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    def submit_form(self):
        account_number = self.entry_account_number.get()
        amount = self.entry_amount.get()

        # Perform validation (you may want to add more validation logic)
        if not account_number or not amount:
            messagebox.showerror("Error", "Please fill in all fields.")
        else:
            # Perform the deposit operation (in a real application, you would interact with a banking API)
            messagebox.showinfo("Success", f"Deposit of {amount} successfully processed for account {account_number}.")

if __name__ == "__main__":
    root = tk.Tk()
    sbi_deposit_form = SbiDepositForm(root)
    root.mainloop()

