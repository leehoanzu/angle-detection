import subprocess
import argparse

def run_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {script_name}: {e}")

def main():
    # Choose your main script
    default_script = 'pysence'  # Set 'pysence' or 'cv'

    # Set argparse 
    parser = argparse.ArgumentParser(description="Choose a script to run.")
    parser.add_argument('script', nargs='?', choices=['pysence', 'cv'], help="The script to run: 'pysence' or 'cv'")
    args = parser.parse_args()

    # If dont have agr in command line, it will use default script
    chosen_script = args.script if args.script else default_script

    script_map = {
        'pysence': 'pysence_processing.py',
        'cv': 'opencv_processing.py'
    }

    if chosen_script in script_map:
        run_script(script_map[chosen_script])
    else:
        print(f"Invalid choice: {chosen_script}. Please choose 'pysence' or 'cv'.")

if __name__ == "__main__":
    main()
