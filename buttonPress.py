'''
Author & Contributer: Carlos Lopez Jr

'''

import subprocess
import time

python_file = ['python3', '/home/acm/Door.Ai/Face-Recognition-with-OpenCV/Recognize.py'] # change to correct location
def execute_bluetoothctl():
    try:
        while True:
            
            # Start bluetoothctl command with sudo
            bluetoothctl_process = subprocess.Popen(['sudo', 'bluetoothctl'], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            
            # Send the command to connect to the Bluetooth device
            bluetoothctl_process.stdin.write("connect 80:E4:DA:7C:B3:E4\n")
            bluetoothctl_process.stdin.flush()
            
            # Read the output until the desired string is found
            while True:
                output = bluetoothctl_process.stdout.readline().strip()
                # print(output)  # Print all output for debugging

                # if already connected -> disconnect the button 
                if "Connected: yes" in output:
                    print("-----------------------------\n\n\n")

                    print("Running Webcam Code")
                    subprocess.run(python_file)

                    print("-----------------------------")

                    
                    # disconnect the device
                    bluetoothctl_process.stdin.write("disconnect\n")
                    bluetoothctl_process.stdin.flush()


                    # send the exit command
                    bluetoothctl_process.stdin.write("exit\n")
                    bluetoothctl_process.stdin.flush()

                    break  # Exit the loop once the desired string is found
            # Sleep for a while before starting the loop again
            time.sleep(5)  # Adjust the sleep duration as needed
    except Exception as e:
        print("An error occurred:", e)

# Example usage
execute_bluetoothctl()
