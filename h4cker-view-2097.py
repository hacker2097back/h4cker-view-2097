import time
import os
import random
import sys

# ANSI escape codes for colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_title():
    title = f"""
        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/

{MAGENTA}                 H4CKE_2097{RESET}
{YELLOW}=================================================={RESET}
{CYAN}             Welcome to  H4CKE_2097 TOOL !{RESET}
"""
    print(title)

def stylized_count(action, count):
    return f"{GREEN}[H4CKER] {action} {count} completed! {RESET}"

def loading_animation():
    print(f"{CYAN}[*] Initializing process", end='')
    for _ in range(3):
        time.sleep(0.5)
        print(".", end='', flush=True)
    print(f"{RESET}")

def progress_bar(current, total):
    bar_length = 30
    filled_length = int(bar_length * current // total)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    sys.stdout.write(f"\r{GREEN}[H4CKER] Progress: |{bar}| {current}/{total} completed.")
    sys.stdout.flush()

def perform_action(action, count, post_link=None, vote_name=None):
    print(f"{GREEN}[*] H4CKER is initiating {action} for: {post_link if post_link else vote_name}...{RESET}")
    loading_animation()
    
    for i in range(1, count + 1):
        time.sleep(random.uniform(0.5, 1.5))  # Increased sleep time
        print(stylized_count(action, i))
        progress_bar(i, count)
        
    print(f"\n{GREEN}[!] H4CKER has finished {action} for {count} {action.lower()} for {post_link if post_link else vote_name}.{RESET}")

def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"{RED}Invalid input! Please enter a number between {min_value} and {max_value}.{RESET}")
        except ValueError:
            print(f"{RED}Invalid input! Please enter a valid number.{RESET}")

def display_menu():
    menu_border = "=" * 52
    print(f"{CYAN}{menu_border}{RESET}")
    print(f"{GREEN}Select the action you want to perform:{RESET}")
    print(f"{RED}1: View 2097{RESET}")
    print(f"{RED}2: Reaction 2097{RESET}")
    print(f"{RED}3: Vote 2097{RESET}")
    print(f"{RED}4: Help{RESET}")
    print(f"{RED}5: Exit{RESET}")
    print(f"{CYAN}{menu_border}{RESET}")

def main():
    clear_screen()
    print_title()
    
    print(f"{MAGENTA}Welcome to the H4CKER_2097 TOOL !{RESET}\n")
    
    while True:
        display_menu()
        
        choice = input(f"{YELLOW}Enter your choice (1, 2, 3, 4, or 5): {RESET}")
        
        if choice == '1':
            views = get_valid_input("Enter number of views (between 100 and 2000): ", 100, 2000)
            post_link = input("Enter your Telegram post link: ")
            if post_link.startswith("https://t.me/"):
                perform_action("View", views, post_link)
            else:
                print(f"{RED}Invalid link!{RESET}")

        elif choice == '2':
            reactions = get_valid_input("Enter number of reactions (between 50 and 1000): ", 50, 1000)
            post_link = input("Enter your Telegram post link: ")
            if post_link.startswith("https://t.me/"):
                perform_action("Reaction", reactions, post_link)
            else:
                print(f"{RED}Invalid link!{RESET}")

        elif choice == '3':
            votes = get_valid_input("Enter number of votes (between 10 and 500): ", 10, 500)
            post_link = input("Enter your Telegram post link: ")
            if post_link.startswith("https://t.me/"):
                vote_name = input("Enter the name for the vote: ")
                perform_action("Vote", votes, post_link, vote_name)
            else:
                print(f"{RED}Invalid link!{RESET}")

        elif choice == '4':
            print(f"{BLUE}Help Menu:{RESET}")
            print("1: View 2097 - Increase views on a Telegram post.")
            print("2: Reaction 2097 - Increase reactions on a Telegram post.")
            print("3: Vote 2097 - Cast votes on a Telegram post.")
            print("5: Exit - Close the program.")
            print(f"{YELLOW}For assistance, contact me on Telegram: @H4CKER_2097{RESET}")

        elif choice == '5':
            print(f"{BLUE}Exiting the program. Goodbye!{RESET}")
            break
        
        else:
            print(f"{RED}Invalid choice. Please try again.{RESET}")

if __name__ == "__main__":
    main()
