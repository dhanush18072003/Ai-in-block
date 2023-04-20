import tkinter as tk 
 from tkinter import messagebox 
  
 class TransactionGUI: 
     def _init_(self, master): 
         self.master = master 
         master.title("Online Transaction") 
  
         
         self.amount_label = tk.Label(master, text="Amount:") 
         self.amount_entry = tk.Entry(master) 
         self.card_label = tk.Label(master, text="Card Number(16-digit):") 
         self.card_entry = tk.Entry(master) 
         self.cvv_label = tk.Label(master, text="CVV(3-digit):") 
         self.cvv_entry = tk.Entry(master, show="*") 
         self.submit_button = tk.Button(master, text="Submit", command=self.submit_transaction) 
         self.message_label = tk.Label(master, text="") 
  
          
         self.amount_label.grid(row=0, column=0) 
         self.amount_entry.grid(row=0, column=1) 
         self.card_label.grid(row=1, column=0) 
         self.card_entry.grid(row=1, column=1) 
         self.cvv_label.grid(row=2, column=0) 
         self.cvv_entry.grid(row=2, column=1) 
         self.submit_button.grid(row=3, column=0, columnspan=2) 
         self.message_label.grid(row=4, column=0, columnspan=2) 
  
     def submit_transaction(self): 
         amount = self.amount_entry.get() 
         card_number = self.card_entry.get() 
         cvv = self.cvv_entry.get() 
  
         # Check if input fields are empty 
         if not amount or not card_number or not cvv: 
             self.message_label.config(text="Please fill in all fields.") 
             return 
  
         # Check if card number is valid 
         if len(card_number) != 16: 
             self.message_label.config(text="Invalid card number.") 
             return 
  
         # Check if CVV is valid 
         if len(cvv) != 3: 
             self.message_label.config(text="Invalid CVV.") 
             return 
  
         # Process transaction 
         # If transaction is successful, display success message in a pop-up window 
         messagebox.showinfo("Transaction Successful", "Transaction for $" + amount + " was successful.") 
  
 root = tk.Tk() 
 gui = TransactionGUI(root) 
 root.mainloop()
