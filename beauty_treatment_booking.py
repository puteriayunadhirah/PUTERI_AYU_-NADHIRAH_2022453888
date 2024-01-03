import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="beauty_package"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Function to handle the calculation and database saving
def collect_data():
    treatment_type = treatment_var.get()
    packs = int(packs_entry.get())
    cust_name = cust_name_entry.get()
    cust_age = cust_age_entry.get()
    cust_contact = cust_contact_entry.get()
    

    #  the price below is to defined the value from your selections
    price = {
        "Treatment A": 90,
        "Treatment B": 150,
        "Combo Treatment": 240, 
    }
    
    # Calculate the total price. This will be derived from your selection (Package, Pack).
    total_price = (price[treatment_type]*packs)
    

    # To insert your Data to your database
    sql = "INSERT INTO `beauty package` (treatment_type, price, packs, cust_name, cust_age, cust_contact) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (treatment_type, total_price, packs, cust_name, cust_age, cust_contact)
    mycursor.execute(sql, val)
    mydb.commit()

    # To Print back The output. It will happen in the function collect_data(). The f before the string indicates an f-string in Python. 
    output_label.config(text=f"Treatment: {treatment_type}, Packs: {packs}, Total Price: RM{total_price}")


# Your Main window, You need to have the title, geometry (MUST)
root = tk.Tk()
root.title("Bright & Beauty Management")
root.geometry('500x950')


# Page Title
label = tk.Label(root, text='Beauty Treatment Booking', font=("Times New Romans",18, "bold", "italic"))
label.pack(ipadx=10, ipady=10)

# Prices List by using textbox
prices_text = tk.Text(root, height=10, width=60, font= ("book antiqua", 12))
prices_text.pack(pady=20)

# The defined list by using pricebox
prices_text.insert(tk.END, "Package & Prices:\n\n")
prices_text.insert(tk.END, "Treatment A : Body Massage \nPrice: RM90\n\n")
prices_text.insert(tk.END, "Treatment B : Facial Treatment \nPrice: RM150\n\n")
prices_text.insert(tk.END, "Combo Treatment : Treatment A + Treatment B + Hair Care \nPrice: RM240 \n\n")
prices_text.configure(state='disabled')

#Save Customer Info
cust_name_label = tk.Label(root, text="Name")
cust_name_label.pack()
cust_name_entry = tk.Entry(root)
cust_name_entry.pack()

cust_age_label = tk.Label(root, text="Age")
cust_age_label.pack()
cust_age_entry = tk.Entry(root)
cust_age_entry.pack()

cust_contact_label = tk.Label(root, text="Contact Number")
cust_contact_label.pack()
cust_contact_entry = tk.Entry(root)
cust_contact_entry.pack()


# Treatment Type Dropdown (Label)
treatment_label = tk.Label(root, text="Choose Your Desired Beauty Package:")
treatment_label.pack()

# Treatment Type Dropdown
treatment_var = tk.StringVar(root)
treatment_var.set("Select Your Treatment")  # Default value before your selection
treatment_dropdown = tk.OptionMenu(root, treatment_var, "Treatment A", "Treatment B", "Combo Treatment")
treatment_dropdown.pack(pady=10)

# Packs Entry. Label and user can insert data thru entry
packs_label = tk.Label(root, text="Packs:")
packs_label.pack()
packs_entry = tk.Entry(root)
packs_entry.pack()

# Save Button
save_button = tk.Button(root, text="Calculate", command=collect_data)
save_button.pack(pady=10)

# Output Label & result
label = tk.Label(root, text='Price Package', font=("Times New Romans",16))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
