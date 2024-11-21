import tkinter as tk
from tkinter import messagebox
import requests

# Base URL of your GraphQL API
BASE_URL = "http://localhost:8091/api_mutation"  # Update with your actual API endpoint

def perform_request(query, variables):
    try:
        response = requests.post(
            BASE_URL,
            json={"query": query, "variables": variables}
        )
        response_data = response.json()
        if "errors" in response_data:
            raise Exception(response_data["errors"][0]["message"])
        return response_data["data"]
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return None

# Function to clear the main content area
def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Functions for each menu item
def show_enrol_user():
    clear_frame()
    tk.Label(main_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
    email_entry = tk.Entry(main_frame, width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(main_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=5)
    confirm_password_entry = tk.Entry(main_frame, width=30, show="*")
    confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

    def enrol_user():
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        query = """
        mutation($enrolmentappuserinput: enrolmentAppUserInput!) {
          enrolAppUser(enrolmentappuserinput: $enrolmentappuserinput) {
            error
            successMsg
            message
          }
        }
        """
        variables = {
            "enrolmentappuserinput": {
                "email": email,
                "password": password,
                "passwordConfirm": confirm_password
            }
        }

        result = perform_request(query, variables)
        if result:
            enrolment_data = result["enrolAppUser"]
            if enrolment_data["error"]:
                messagebox.showerror("Error", enrolment_data["message"])
            else:
                messagebox.showinfo("Success", enrolment_data["message"])

    tk.Button(main_frame, text="Submit", command=enrol_user).grid(row=3, column=0, columnspan=2, pady=10)

def show_authenticate_user():
    clear_frame()
    tk.Label(main_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
    email_entry = tk.Entry(main_frame, width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(main_frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
    password_entry = tk.Entry(main_frame, width=30, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    def authenticate_user():
        email = email_entry.get()
        password = password_entry.get()

        query = """
        mutation($email: String!, $password: String!) {
          authenticateAppUser(email: $email, password: $password) {
            error
            successMsg
            message
            accessToken
            refreshToken
          }
        }
        """
        variables = {"email": email, "password": password}

        result = perform_request(query, variables)
        if result:
            auth_data = result["authenticateAppUser"]
            if auth_data["error"]:
                messagebox.showerror("Error", auth_data["message"])
            else:
                messagebox.showinfo("Success", f"Access Token: {auth_data['accessToken']}")

    tk.Button(main_frame, text="Submit", command=authenticate_user).grid(row=2, column=0, columnspan=2, pady=10)

def show_activate_user():
    clear_frame()
    tk.Label(main_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
    email_entry = tk.Entry(main_frame, width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    def activate_user():
        email = email_entry.get()

        query = """
        mutation($email: String!) {
          activateAppUser(email: $email) {
            error
            successMsg
            message
          }
        }
        """
        variables = {"email": email}

        result = perform_request(query, variables)
        if result:
            activation_data = result["activateAppUser"]
            if activation_data["error"]:
                messagebox.showerror("Error", activation_data["message"])
            else:
                messagebox.showinfo("Success", activation_data["message"])

    tk.Button(main_frame, text="Submit", command=activate_user).grid(row=1, column=0, columnspan=2, pady=10)

def show_deactivate_user():
    clear_frame()
    tk.Label(main_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
    email_entry = tk.Entry(main_frame, width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    def deactivate_user():
        email = email_entry.get()

        query = """
        mutation($email: String!) {
          deactivateAppUser(email: $email) {
            error
            successMsg
            message
          }
        }
        """
        variables = {"email": email}

        result = perform_request(query, variables)
        if result:
            deactivation_data = result["deactivateAppUser"]
            if deactivation_data["error"]:
                messagebox.showerror("Error", deactivation_data["message"])
            else:
                messagebox.showinfo("Success", deactivation_data["message"])

    tk.Button(main_frame, text="Submit", command=deactivate_user).grid(row=1, column=0, columnspan=2, pady=10)

def show_validate_user():
    clear_frame()
    tk.Label(main_frame, text="Email:").grid(row=0, column=0, padx=10, pady=5)
    email_entry = tk.Entry(main_frame, width=30)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    def validate_user():
        email = email_entry.get()

        query = """
        mutation($email: String!) {
          validateAppUser(email: $email) {
            error
            success_msg
            message
          }
        }
        """
        variables = {"email": email}

        result = perform_request(query, variables)
        if result:
            validation_data = result["validateAppUser"]
            if validation_data["error"]:
                messagebox.showerror("Error", validation_data["message"])
            else:
                messagebox.showinfo("Success", validation_data["message"])

    tk.Button(main_frame, text="Submit", command=validate_user).grid(row=1, column=0, columnspan=2, pady=10)

#
# Create the main window
root = tk.Tk()
root.title("GraphQL API Client")

# Create a menu
menu = tk.Menu(root)
root.config(menu=menu)

# Add menu items
actions_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Actions", menu=actions_menu)
actions_menu.add_command(label="Enrol User", command=show_enrol_user)
actions_menu.add_command(label="Authenticate User", command=show_authenticate_user)
actions_menu.add_command(label="Activate User", command=show_activate_user)
actions_menu.add_command(label="Deactivate User", command=show_deactivate_user)
actions_menu.add_command(label="Validate User", command=show_validate_user)


# Create a frame for dynamic content
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Default view
show_enrol_user()

# Run the application
root.mainloop()
