#!/usr/bin/env python3
import subprocess
from datetime import datetime
import os

# Change this to your actual directory where your git repository is
os.chdir('/home/ubuntu/margin')

def run_command(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process.stdout

def git_operations():
    # Get the current date in YYYY-MM-DD format
    date = datetime.now().strftime('%Y-%m-%d')
    try:
        # Staging changes
        run_command('git add .')
        
        # Committing changes
        run_command(f'git commit -m "Updated {date} changes"')
        
        # Pushing changes
        run_command('git push')
        
        print(f"Changes pushed successfully on {date}.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing changes: {e.stderr.decode()}")

if __name__ == "__main__":
    git_operations()

