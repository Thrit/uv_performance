import time
import subprocess


command = ["pip", "install", "-r", "requirements.txt"] 
start_time = time.time()

# Package installation command
subprocess.call(command)

end_time = time.time()

elapsed_time = end_time - start_time
print(f"Requirements.txt loading time: {elapsed_time} seconds")

# No UV: 182.17838215827942 seconds or 3 minutes
# UV: 26.280544996261597 seconds or 0.4 minutes
# Optimized in 86,67%