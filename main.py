import subprocess
import sys
import os

def run_script(script_name):
    # Points to the scripts inside the 'folder' directory
    script_path = os.path.join('src', script_name)
    
    print(f"\n--- Running {script_path} ---")
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except FileNotFoundError:
        print(f"Error: {script_path} not found.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Script failed with code {e.returncode}")

if __name__ == "__main__":
    while True:
        print("\nMenu:\n1. Generate Data\n2. Run SQL\n3. Run Visuals\n4. Exit")
        choice = input("Select (1-4): ")
        
        if choice == '1': 
            run_script('generate_logistics_data.py')
        elif choice == '2': 
            run_script('sql_pipeline.py')
        elif choice == '3': 
            run_script('visual_variance.py')
        elif choice == '4': 
            break