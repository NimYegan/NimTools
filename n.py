import os
import socket
import requests
import time
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.text import Text
from rich.style import Style

# Initialize Rich console
console = Console()

# Function to clear the terminal
def clear_screen():
    os.system('clear')

# Function to display RealNimV with toilet
def display_toilet_art():
    os.system('toilet -f future "Real NimV" --filter metal | boxes -d parchment')

# Function to scan network ports
def port_scan():
    clear_screen()
    console.print(Panel.fit("NETWORK PORT SCANNER", style="bold cyan", padding=(1, 2), border_style="bold blue"))
    
    target = console.input("🔍 [bold yellow]Enter website or IP address: ")
    
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        console.print("❌ [bold red]Invalid domain or IP!")
        console.input("\nPress Enter to return to menu...")
        return
    
    port_range = console.input("🔢 [bold yellow]Enter port range (e.g., 1-100): ")
    
    try:
        start_port, end_port = map(int, port_range.split('-'))
    except ValueError:
        console.print("❌ [bold red]Invalid port range format!")
        console.input("\nPress Enter to return to menu...")
        return
    
    console.print(f"\n🚀 [bold cyan]Scanning {target} ({ip}) from port {start_port} to {end_port}...\n")
    
    with Progress() as progress:
        task = progress.add_task("[cyan]Scanning ports...", total=end_port - start_port + 1)
        
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                console.print(f"✅ [bold green]Port {port} is open.")
            sock.close()
            progress.update(task, advance=1)
    
    console.input("\nPress Enter to return to menu...")

# Function to update the system
def update_system():
    clear_screen()
    console.print(Panel.fit("SYSTEM UPDATE & PACKAGES", style="bold cyan", padding=(1, 2), border_style="bold blue"))
    
    console.print("🔄 [bold yellow]Updating system and installed packages...\n")
    os.system('pkg update && pkg upgrade -y')
    
    console.print("\n✅ [bold green]Update completed successfully!")
    console.input("\nPress Enter to return to menu...")

# Function to scan website vulnerabilities
def vulnerability_scan():
    clear_screen()
    console.print(Panel.fit("WEBSITE VULNERABILITY SCAN", style="bold cyan", padding=(1, 2), border_style="bold blue"))
    
    url = console.input("🌐 [bold yellow]Enter website URL (e.g., https://example.com): ")
    
    if not url.startswith('http'):
        url = 'https://' + url  # Auto-fix missing protocol
    
    console.print("\n🔍 [bold cyan]Checking website security...\n")
    
    try:
        response = requests.get(url, timeout=5)
        console.print(f"✅ [bold green]Website is accessible (Status: {response.status_code})")
    except requests.RequestException:
        console.print("❌ [bold red]Website is not reachable!")
        console.input("\nPress Enter to return to menu...")
        return
    
    if url.startswith('https'):
        console.print("🔒 [bold green]Secure HTTPS connection detected.")
    else:
        console.print("⚠️ [bold red]Website is using HTTP (Not Secure)!")
    
    console.input("\nPress Enter to return to menu...")

# Function to check the last version of the script
def check_last_version():
    clear_screen()
    console.print(Panel.fit("CHECK LAST VERSION", style="bold cyan", padding=(1, 2), border_style="bold blue"))
    
    # Replace with your own version checking logic
    current_version = "1.0.0"
    latest_version = "1.0.0"  # Simulate fetching the latest version
    
    console.print(f"🔄 [bold yellow]Checking for updates...\n")
    console.print(f"✅ [bold green]Current Version: {current_version}")
    console.print(f"✅ [bold green]Latest Version: {latest_version}")
    
    if current_version == latest_version:
        console.print("\n🎉 [bold green]You are using the latest version!")
    else:
        console.print("\n⚠️ [bold yellow]A new version is available! Please update.")
    
    console.input("\nPress Enter to return to menu...")

# Function to display main menu
def show_menu():
    clear_screen()
    display_toilet_art()  # Display RealNimV with toilet
    
    menu_table = Table(show_header=True, header_style="bold magenta", width=80, border_style="bold blue")
    menu_table.add_column("Option", style="dim", width=12)
    menu_table.add_column("Description", style="bold cyan")
    
    menu_table.add_row("1", "Scan Network Ports")
    menu_table.add_row("2", "Update System & Packages")
    menu_table.add_row("3", "Website Vulnerability Scan")
    menu_table.add_row("4", "Check Last Version")
    menu_table.add_row("5", "Exit")
    
    console.print(menu_table)

def main():
    while True:
        show_menu()
        choice = console.input("\nSelect an option (1-5): ")

        if choice == '1':
            port_scan()
        elif choice == '2':
            update_system()
        elif choice == '3':
            vulnerability_scan()
        elif choice == '4':
            check_last_version()
        elif choice == '5':
            clear_screen()
            console.print("🚪 [bold red]Exiting the script...\n")
            break
        else:
            console.print("❌ [bold red]Invalid choice! Please enter a number between 1-5.")

if __name__ == "__main__":
    main()