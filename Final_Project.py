import tkinter as tk  # Base module for GUI.
from tkinter import ttk, messagebox  # ttk for enhanced widgets, messagebox for dialogs.

# Define a class to encapsulate the logistic management system's functionalities.
class LogisticManagementSystem:
    def __init__(self, root):
        # Initialize the main application window.
        self.root = root # To assign a root parameter
        self.root.title("Logistic Management System")  # To set the window title.
        self.root.geometry("1200x800")  # Defines the size of the window.

        # Initialize an empty list to store logistics data records.
        self.logistics_data = []    

        self.setup_ui()    # To set up a GUI of the application

    def setup_ui(self):
        # Create and display the title of the application.
        title = tk.Label(
            self.root, text="Logistic Management System", font=("Arial", 18, "bold")
        )
        title.pack(pady=15) # Used to setup the lable and pady=15 means spacing in pixels.

        # Create a frame to hold input fields for entering logistics details.
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Create labels and entry widgets for user input.
        tk.Label(input_frame, text="Product Id").grid(row=0, column=0, padx=5, pady=5)
        self.product_id_entry = tk.Entry(input_frame)
        self.product_id_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Product Name").grid(row=1, column=0, padx=5, pady=5)
        self.product_name_entry = tk.Entry(input_frame)
        self.product_name_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Quantity").grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Rate Per Quantity").grid(row=3, column=0, padx=5, pady=5)
        self.rate_entry = tk.Entry(input_frame)
        self.rate_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Total Price").grid(row=4, column=0, padx=5, pady=5)
        self.total_price_entry = tk.Entry(input_frame)
        self.total_price_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Rack Number").grid(row=5, column=0, padx=5, pady=5)
        self.rack_number_entry = tk.Entry(input_frame)
        self.rack_number_entry.grid(row=5, column=1, padx=5, pady=5)

        # Create a frame to hold buttons for adding and deleting records.
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=15)

        # Create the "Add Record" button and link it to the `add_record` method.
        add_btn = tk.Button(
            button_frame,
            text="Add Record",
            command=self.add_record,
            bg="lightblue",
            font=("Arial", 12),
        )
        add_btn.grid(row=0, column=0, padx=10)

        # Create the "Delete Record" button and link it to the `delete_record` method.
        delete_btn = tk.Button(
            button_frame,
            text="Delete Record",
            command=self.delete_record,
            bg="lightcoral",
            font=("Arial", 12),
        )
        delete_btn.grid(row=0, column=1, padx=10)

        # Create a table using Treeview to display logistics records.
        self.records_table = ttk.Treeview(
            self.root,
            columns=("Id", "Name", "Quantity", "Rate_Per_Quantity", "Total_Price", "Rack_Number"),
            show="headings",
        )
        # Define the headings for each column in the table.
        self.records_table.heading("Id", text="Product Id")
        self.records_table.heading("Name", text="Product Name")
        self.records_table.heading("Quantity", text="Quantity")
        self.records_table.heading("Rate_Per_Quantity", text="Rate Per Quantity")
        self.records_table.heading("Total_Price", text="Total Price")
        self.records_table.heading("Rack_Number", text="Rack Number")

        # Display the table with padding and expansion settings.
        self.records_table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def add_record(self):
        # Fetch input values from the entry fields.
        product_id = self.product_id_entry.get().strip()
        product_name = self.product_name_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        rate = self.rate_entry.get().strip()
        total_price = self.total_price_entry.get().strip()
        rack_number = self.rack_number_entry.get().strip()

        # Validate inputs to ensure all fields are filled and contain correct data types.
        if product_id and product_name and quantity.isdigit() and rate.isdigit() and total_price.isdigit() and rack_number.isdigit():
            # Create a record tuple with validated inputs.
            record = (
                product_id,
                product_name,
                int(quantity),
                float(rate),
                float(total_price),
                float(rack_number),
            )
            # Add the record to the logistics data list.
            self.logistics_data.append(record)
            self.update_table()  # Update the table with the new record.
            self.clear_entries()  # Clear input fields for new data entry.
        else:
            # Show an error message if inputs are invalid.
            messagebox.showerror("Input Error", "Please fill all fields correctly!")

    def delete_record(self):
        # Get the selected record(s) from the table.
        selected_item = self.records_table.selection()
        if selected_item:
            for item in selected_item:
                # Retrieve values of the selected row.
                values = self.records_table.item(item, "values")
                # Convert values back to appropriate types and remove from the data list.
                record_to_delete = (
                    values[0],  # Product Id
                    values[1],  # Product Name
                    int(values[2]),  # Quantity
                    float(values[3]),  # Rate Per Quantity
                    float(values[4]),  # Total Price
                    float(values[5]),
                )
                if record_to_delete in self.logistics_data:
                    self.logistics_data.remove(record_to_delete)
                self.records_table.delete(item)  # Remove from the table.
        else:
            # Show a warning if no record is selected for deletion.
            messagebox.showwarning("Selection Error", "No record selected!")

    def update_table(self):
        # Clear the table to refresh its data.
        for item in self.records_table.get_children():
            self.records_table.delete(item)

        # Insert all current records into the table.
        for record in self.logistics_data:
            self.records_table.insert("", "end", values=record)

    def clear_entries(self):
        # Clear all input fields to prepare for new data entry.
        self.product_id_entry.delete(0, tk.END)
        self.product_name_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.total_price_entry.delete(0, tk.END)
        self.rack_number_entry.delete(0, tk.END)

# Main entry point for the application.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window.
    app = LogisticManagementSystem(root)  # Initialize the application.
    root.mainloop()  # Start the Tkinter event loop.
