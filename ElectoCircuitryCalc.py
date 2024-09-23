import tkinter as tk
from tkinter import ttk, messagebox
import math

class ElectronicsCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ElectroCalc")
        self.geometry("600x600")

        # Formula Selection
        self.formula_label = tk.Label(self, text="Select Formula:")
        self.formula_label.pack(pady=10)

        self.formula_var = tk.StringVar()
        self.formula_dropdown = ttk.Combobox(self, textvariable=self.formula_var)
        self.formula_dropdown['values'] = ['Ohm\'s Law', 'Capacitance', 'Energy in Capacitor','Power','Frequency and Time','Angular Frequency','RC Time Constant','RL Time Constant']
        self.formula_dropdown.bind("<<ComboboxSelected>>", self.update_inputs)
        self.formula_dropdown.pack(pady=10)

        # Input Fields
        self.input_frame = tk.Frame(self)
        self.input_frame.pack(pady=10)

        self.input_labels = []
        self.input_entries = []

        self.calculate_button = tk.Button(self, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self, text="Result:")
        self.result_label.pack(pady=10)

        self.result_display = tk.Label(self, text="")
        self.result_display.pack(pady=10)

    def update_inputs(self, event):
        # Clear previous inputs
        for label in self.input_labels:
            label.destroy()
        for entry in self.input_entries:
            entry.destroy()

        self.input_labels.clear()
        self.input_entries.clear()

        selected_formula = self.formula_var.get()

        if selected_formula == "Ohm's Law":
            self.add_input("Insert voltage (V) in Volts:")
            self.add_input("Insert current (I) in Amperes:")
            self.add_input("Insert resistance (R) in Ohm:")

        elif selected_formula == "Power":
            self.add_input("Insert voltage (V) in Volts:")
            self.add_input("Insert current (I) in Amperes:")
            self.add_input("Insert power (W) in Whatt:")

        elif selected_formula == "Frequency and Time":
            self.add_input("Insert frequency (f) in Hz:")
            self.add_input("Insert time (T) in sec:")
            
        elif selected_formula == "Angular Frequency":
            self.add_input("Insert frequency (f) in Hz:")
            self.add_input("Insert time (w) in rad/s:")


        elif selected_formula == "Capacitance":
            self.add_input(" Insert Charge (Q) in Coulombs (C):")
            self.add_input("Insert voltage (V) in Volts:")

        elif selected_formula == "RC Time Constant":
            self.add_input("Insert Resistance (R) in Ohm:")
            self.add_input("Insert Capacitance (C) in Farads:")
            self.add_input("Insert time constant (τ):")
        
        elif selected_formula == "RL Time Constant":
            self.add_input("Insert Resistance (R) in Ohm:")
            self.add_input("Insert Inductance (L) in Henry:")
            self.add_input("Insert time constant (τ):")


        elif selected_formula == "RC Time Constant":
            self.add_input("Insert voltage (V) in Volts:")
            self.add_input("Insert current (I) in Amperes:")
            self.add_input("Insert power (W) in Whatt:")

        elif selected_formula == "Energy in Capacitor":
            self.add_input("Insert Capacitance (C) in Farads:")
            self.add_input("Insert voltage (V) in Volts:")

    def add_input(self, label_text):
        label = tk.Label(self.input_frame, text=label_text)
        label.pack()
        entry = tk.Entry(self.input_frame)
        entry.pack()
        self.input_labels.append(label)
        self.input_entries.append(entry)

    def calculate(self):
        selected_formula = self.formula_var.get()
        try:
            if selected_formula == "Ohm's Law":
                V = self.get_value(0)  # Voltage
                I = self.get_value(1)  # Current
                R = self.get_value(2)  # Resistance

                # Calculate missing value
                if V == None and I is not None and R is not None:
                    V = I * R
                    self.result_display.config(text=f"Voltage (V): {V:.2f} V")
                elif I == None and V is not None and R is not None:
                    I = V / R
                    self.result_display.config(text=f"Current (I): {I:.2f} A")
                elif R == None and V is not None and I is not None:
                    R = V / I
                    self.result_display.config(text=f"Resistance (R): {R:.2f} Ω")
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")

            elif selected_formula == "Capacitance":
                Q = self.get_value(0)  # Charge
                V = self.get_value(1)  # Voltage
                if Q is not None and V is not None:
                    C = Q / V
                    self.result_display.config(text=f"Capacitance (C): {C:.2f} F")
                else:
                    messagebox.showinfo("Info", "Please enter valid values for Charge and Voltage.")

            elif selected_formula == "Power":
                V = self.get_value(0)  # Voltage
                I = self.get_value(1)  # Current
                P = self.get_value(2)  # Power

                    
                if P == None and I is not None and V is not None:
                    P =  V * I
                    self.result_display.config(text=f"Power (P): {P:.2f} W")
                elif I == None and V is not None and P is not None:
                    I = P/ V
                    self.result_display.config(text=f"Current (I): {I:.2f} A")
                elif V == None and P is not None and I is not None:
                    V = P/ I
                    self.result_display.config(text=f"Voltage (V): {V:.2f} V")
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")

            elif selected_formula == "RC Time Constant":
                R = self.get_value(0)  # Resistance
                C = self.get_value(1)  # Capacitance
                t = self.get_value(2)  # Time constant

                    
                if t == None and R is not None and C is not None:
                    t =  C * R
                    self.result_display.config(text=f"Time Constant (τ): {t:.2f} ")
                elif R == None and t is not None and C is not None:
                    R = t/ C
                    self.result_display.config(text=f"Resistance (R): {R:.2f} Ω")
                elif C == None and R is not None and t is not None:
                    C = t/ R
                    self.result_display.config(text=f"Capacitance (C): {C:.2f} F")
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")
                
            elif selected_formula == "RL Time Constant":
                R = self.get_value(0)  # Resistance
                L = self.get_value(1)  # Inductance
                t = self.get_value(2)  # Time constant

                    
                if t == None and R is not None and L is not None:
                    t =  L/ R
                    self.result_display.config(text=f"Time Constant (τ): {t:.2f} ")
                elif R == None and t is not None and L is not None:
                    R = L/ t
                    self.result_display.config(text=f"Resistance (R): {R:.2f} Ω")
                elif L == None and R is not None and t is not None:
                    L = t * R
                    self.result_display.config(text=f"Inductance (L): {C:.2f} H")
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")


            elif selected_formula == "Frequency":
                f = self.get_value(0)  # Frequency
                T = self.get_value(1)  # Time
   
                if f == None and T is not None :
                    f =  1/ T
                    self.result_display.config(text=f"Frequency (f): {f:.2f} Hz")
                elif T == None and f is not None :
                    f = 1/ f
                    self.result_display.config(text=f"Time (T): {T:.2f} sec")
                
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")
            
            elif selected_formula == "Angular Frequency":
                f = self.get_value(0)  # Frequency
                w = self.get_value(1)  # Angular frequency
   
                if w == None and f is not None :
                    w =  2* math.pi * f
                    self.result_display.config(text=f"Angular Frequencyy (w): {w:.2f} rad/s")
                elif f == None and w is not None :
                    f =  w / (2* math.pi )
                    self.result_display.config(text=f"Frequency (f): {f:.2f} Hz")
                
                else:
                    messagebox.showinfo("Info", "Please leave one value blank to calculate.")


            elif selected_formula == "Energy in Capacitor":
                C = self.get_value(0)  # Capacitance
                V = self.get_value(1)  # Voltage
                if C is not None and V is not None:
                    E = 0.5 * C * V**2
                    self.result_display.config(text=f"Energy (E): {E:.2f} J")
                else:
                    messagebox.showinfo("Info", "Please enter valid values for Capacitance and Voltage.")
                    
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")

    def get_value(self, index):
        try:
            value = self.input_entries[index].get()
            return float(value) if value else None
        except ValueError:
            return None

if __name__ == "__main__":
    app = ElectronicsCalculator()
    app.mainloop()
