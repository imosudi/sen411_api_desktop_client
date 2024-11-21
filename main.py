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

# Create GUI
root = tk.Tk()
root.title("GraphQL API Client")

tk.Label(root, text="Email:").grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Confirm Password:").grid(row=2, column=0, padx=10, pady=5)
confirm_password_entry = tk.Entry(root, width=30, show="*")
confirm_password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Enrol User", command=enrol_user).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="Authenticate User", command=authenticate_user).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Activate User", command=activate_user).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Deactivate User", command=deactivate_user).grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
