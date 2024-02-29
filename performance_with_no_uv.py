import time
import subprocess


command = ["pip", "install", "-r", "requirements.txt"] 
start_time = time.time()

# Package installation command
subprocess.call(command)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Requirements.txt loading time: {elapsed_time} seconds")
