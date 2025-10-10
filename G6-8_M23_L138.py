# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Define the RestaurantOrderManagement class
class RestaurantOrderManagement:
    # Initialize the application
    def __init__(self, root):
        self.root = root  # The main window of the app
        self.root.title("Restaurant Management App")  # Set the title of the window

        # A dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # Exchange rate for currency conversion

        self.setup_background(root)  # Set up the background image

        # Create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame

        # Heading label
        ttk.Label(frame,text="Restaurant Order Management",font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        # Dictionaries to store labels and entry references
        self.menu_labels = {}
        self.menu_quantities = {}

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(frame,text=f"{item} (${price}):",font=("Arial", 12)
            )
            label.grid(row=i, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar()
        ttk.Label(frame,text="Currency:",font=("Arial", 12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)

        # Dropdown for currency selection
        currency_dropdown = ttk.Combobox(frame,textvariable=self.currency_var,state="readonly", width=18,values=('USD', 'INR'))
        currency_dropdown.grid(row=len(self.menu_items) + 1,column=1,padx=10,pady=5)
        currency_dropdown.current(0)  # Set default currency

        # Update prices when currency changes
        self.currency_var.trace('w', self.update_menu_prices)

        # Button to place the order
        order_button = ttk.Button(frame,text="Place Order",command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2,columnspan=3,padx=10,pady=10)

    # Method to set up the background image
    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack(fill="both", expand=True)

        # ✅ Load and resize image using PIL
        img = Image.open(r"C:\Users\sanvi\OneDrive\Desktop\Codingal\code\G_6-8\images\aaa.jpg")
        img = img.resize((bg_width, bg_height))  # Resize to window size
        background_image = ImageTk.PhotoImage(img)

        # ✅ Place image on canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image  # Keep a reference to avoid garbage collection


    # Method to update the menu prices based on the selected currency
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    # Method to place an order
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            # Show error if no items are ordered
            messagebox.showerror("Error", "Please order at least one item.")


# Block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")  # Set window size
    root.mainloop()  # Start GUI loop
