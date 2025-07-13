import time
import random
import sys
from colorama import init, Fore, Style
import os

init(autoreset=True)

def format_eta(seconds):
    mins, secs = divmod(int(seconds), 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs:02}:{mins:02}:{secs:02}"

def hack_simulator_loop(machine_count_max):
    machine_count = 0

    while machine_count < machine_count_max:
        machine_count += 1
        correct_pin = str(random.randint(1000, 9999))
        attempts = 0
        total_time = 0

        print(Fore.GREEN + f"\nCracking phone: {machine_count}/{machine_count_max}\n")
        time.sleep(0.3)

        while True:
            pin = f"{random.randint(1000, 9999)}"
            attempts += 1

            start_try = time.time()
            time.sleep(0.001)
            end_try = time.time()

            elapsed = end_try - start_try
            total_time += elapsed

            avg_time = total_time / attempts
            max_attempts = 10000
            remaining = max_attempts - attempts
            eta = format_eta(remaining * avg_time)

            print(Fore.GREEN + f"{pin} ({attempts}) — {elapsed:.4f}s — ETA: {eta}")

            if pin == correct_pin:
                break

        print(Fore.GREEN + f"\nCrack success: {correct_pin}")
        print(Fore.GREEN + "Cracking...")
        time.sleep(0.5)
        print(Fore.GREEN + "MISSION SUCCESS\n")
        time.sleep(1)

    print(Fore.GREEN + "\nAll devices cracked. Simulation ended.\n")

def main():
    while True:
        print("==== CRACKING PHONE ====")
        print("1. Crack one phone")
        print("2. Crack multiple phones")
        print("3. Exit")
        choice = input("Your choice: ")

        if choice == "1":
            hack_simulator_loop(1)
        elif choice == "2":
            try:
                n = int(input("Chosen any phone you want crack: "))
                hack_simulator_loop(n)
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
