import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from ttkthemes import ThemedTk

class WebsiteBlocker:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Blocker")
        self.root.geometry("600x400")

        # Set a professional background color
        self.professional_bg_color = "#86A3C3"

        # Variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.blocked_websites = set()

        # Welcome Page
        self.welcome_frame = ttk.Frame(root, padding=(30, 50, 30, 10), style='Professional.TFrame')
        self.welcome_frame.pack()

        ttk.Label(self.welcome_frame, text="Welcome to Web Blocker", font=('Arial', 20, 'bold'), style='Professional.TLabel').grid(row=0, column=0, columnspan=2, pady=20)
        ttk.Button(self.welcome_frame, text="Login", command=self.show_login_frame, style='Professional.TButton').grid(row=1, column=0, columnspan=2, pady=20)

        # Style configuration for professional look
        style = ttk.Style()

        # Create a new style for the frames and labels
        style.configure('Professional.TFrame', background=self.professional_bg_color)
        style.configure('Professional.TLabel', background=self.professional_bg_color, font=('Arial', 16))
        style.configure('Professional.TButton', font=('Arial', 14), padding=(10, 5))

    def show_login_frame(self):
        # Destroy welcome frame
        self.welcome_frame.destroy()

        # Login Frame
        self.login_frame = ttk.Frame(self.root, padding=(50, 50, 50, 30), style='Professional.TFrame')
        self.login_frame.pack()

        ttk.Label(self.login_frame, text="Username:", font=('Arial', 16), style='Professional.TLabel').grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.login_frame, textvariable=self.username, font=('Arial', 14)).grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(self.login_frame, text="Password:", font=('Arial', 16), style='Professional.TLabel').grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.login_frame, textvariable=self.password, show="*", font=('Arial', 14)).grid(row=1, column=1, padx=10, pady=10)
        ttk.Button(self.login_frame, text="Login", command=self.login, style='Professional.TButton').grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        # Simple login logic for demonstration
        if self.username.get() == "madhu" and self.password.get() == "password":
            self.show_main_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def show_main_frame(self):
        # Destroy login frame
        self.login_frame.destroy()

        # Main Frame
        self.main_frame = ttk.Frame(self.root, padding=(50, 50, 50, 30), style='Professional.TFrame')
        self.main_frame.pack()

        ttk.Label(self.main_frame, text="Blocked Websites:", font=('Arial', 16), style='Professional.TLabel').grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(self.main_frame, text="Block Website", command=self.block_website, style='Professional.TButton').grid(row=1, column=0, padx=10, pady=10)
        ttk.Button(self.main_frame, text="Unblock Website", command=self.unblock_website, style='Professional.TButton').grid(row=2, column=0, padx=10, pady=10)
        ttk.Button(self.main_frame, text="Show Blocked Websites", command=self.show_blocked_websites, style='Professional.TButton').grid(row=3, column=0, padx=10, pady=10)

    def block_website(self):
        website = simpledialog.askstring("Block Website", "Enter the website to block:")
        if website:
            self.modify_hosts_file(website, block=True)
            self.blocked_websites.add(website)
            messagebox.showinfo("Blocked", f"{website} is blocked.")

    def unblock_website(self):
        website = simpledialog.askstring("Unblock Website", "Enter the website to unblock:")
        if website in self.blocked_websites:
            self.modify_hosts_file(website, block=False)
            self.blocked_websites.remove(website)
            messagebox.showinfo("Unblocked", f"{website} is unblocked.")
        else:
            messagebox.showwarning("Not Found", f"{website} is not in the blocked list.")

    def show_blocked_websites(self):
        blocked_list = "\n".join(self.blocked_websites)
        if blocked_list:
            messagebox.showinfo("Blocked Websites", blocked_list)
        else:
            messagebox.showinfo("Blocked Websites", "No websites are currently blocked.")

    @staticmethod
    def modify_hosts_file(website, block=True):
        hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
        redirect_ip = "127.0.0.1"
        try:
            with open(hosts_path, "r+") as hosts_file:
                content = hosts_file.read()
                if block and website not in content:
                    hosts_file.write(f"{redirect_ip} {website}\n")
                elif not block:
                    updated_content = "\n".join(line for line in content.splitlines() if website not in line)
                    hosts_file.seek(0)
                    hosts_file.truncate()
                    hosts_file.write(updated_content)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to modify hosts file: {str(e)}")

if __name__ == "__main__":
    root = ThemedTk(theme="aquativo")  # Choose a theme: "aquativo", "arc", "black", "blue", "radiance", etc.
    app = WebsiteBlocker(root)
    root.mainloop()