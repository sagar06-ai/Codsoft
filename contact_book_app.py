import tkinter as tk
from tkinter import messagebox
import json
import os


CONTACT_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x550")

        self.contacts = load_contacts()

       
        self.name_entry = self.create_labeled_entry("Name")
        self.phone_entry = self.create_labeled_entry("Phone")
        self.email_entry = self.create_labeled_entry("Email")
        self.address_entry = self.create_labeled_entry("Address")

       
        tk.Button(root, text="Add Contact", command=self.add_contact).pack(pady=5)
        tk.Button(root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", command=self.delete_contact).pack(pady=5)
        tk.Button(root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(root, text="Show All Contacts", command=self.show_contacts).pack(pady=5)

        
        self.contact_listbox = tk.Listbox(root, width=60, height=10)
        self.contact_listbox.pack(pady=10)
        self.contact_listbox.bind('<<ListboxSelect>>', self.fill_form_from_selection)

        self.show_contacts()

    def create_labeled_entry(self, label_text):
        tk.Label(self.root, text=label_text).pack()
        entry = tk.Entry(self.root, width=40)
        entry.pack(pady=3)
        return entry

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def fill_form_from_selection(self, event):
        try:
            index = self.contact_listbox.curselection()[0]
            contact = self.contacts[index]
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
            self.address_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.insert(0, contact["email"])
            self.address_entry.insert(0, contact["address"])
        except IndexError:
            pass

    def add_contact(self):
        contact = {
            "name": self.name_entry.get().strip(),
            "phone": self.phone_entry.get().strip(),
            "email": self.email_entry.get().strip(),
            "address": self.address_entry.get().strip()
        }
        if not contact["name"] or not contact["phone"]:
            messagebox.showwarning("Missing Info", "Name and phone are required.")
            return
        self.contacts.append(contact)
        self.clear_form()
        self.show_contacts()

    def update_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.contacts[index] = {
                "name": self.name_entry.get().strip(),
                "phone": self.phone_entry.get().strip(),
                "email": self.email_entry.get().strip(),
                "address": self.address_entry.get().strip()
            }
            self.clear_form()
            self.show_contacts()
        except IndexError:
            messagebox.showwarning("Update Error", "Select a contact to update.")

    def delete_contact(self):
        try:
            index = self.contact_listbox.curselection()[0]
            self.contacts.pop(index)
            self.clear_form()
            self.show_contacts()
        except IndexError:
            messagebox.showwarning("Delete Error", "Select a contact to delete.")

    def search_contact(self):
        keyword = self.name_entry.get().strip().lower()
        filtered = [c for c in self.contacts if keyword in c["name"].lower() or keyword in c["phone"]]
        self.show_contacts(filtered)

    def show_contacts(self, contact_list=None):
        self.contact_listbox.delete(0, tk.END)
        if contact_list is None:
            contact_list = self.contacts
        for contact in contact_list:
            display = f"{contact['name']} | {contact['phone']}"
            self.contact_listbox.insert(tk.END, display)

    def on_close(self):
        save_contacts(self.contacts)
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
