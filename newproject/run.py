import subprocess
import os
import subprocess
import threading
import time

def excute_commands_from_run_txt_file(file_path):
    try:   
        commands = None
        with open(file_path, 'r') as file:
            commands = file.readlines()

        for command in commands:
            command = command.strip() #Removes leading and trailing whitespace
            if command:
                if "runserver" in command:
                    server_thread = threading.Thread(target=subprocess.run, args=(command,), kwargs={"shell": True})
                    server_thread.start()
                  
                    time.sleep(10)
        
                    print("Stopping the server...")
                 
                
                    server_thread.join(timeout=1)
                    break
                else:
                    print(f'executing command: {command}')
                    subprocess.run(command, shell=True)
    except FileExistsError:
        print(f'file does not exist in this path: {file_path}') 
    except Exception as e:
        print(f'Error: {e}')               

# file_path = '/home/michael/Desktop/X_projects/django_react_auth/django/djangovenv/newproject/run.txt'
file_path = os.path.join(os.getcwd(), 'run.txt') 
excute_commands_from_run_txt_file(file_path)



