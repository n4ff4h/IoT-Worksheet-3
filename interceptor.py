import serial
import requests
import subprocess

def main(serial_port):
    try:
        with serial.Serial(serial_port, baudrate=115200, timeout=1, stopbits=1) as ser:
            print(f"Connected to micro:bit: {serial_port}")
            while True:
                data = ser.readline().decode().strip()
                if data:
                    print(data)
                    
                    # Make a get request to fast api server
                    r = requests.post('http://127.0.0.1:8000/', params={"password": data})
                    print(r.content.decode())
                    if r.status_code == 200:
                        ser.write(r.content)
                    else:
                        ser.write(r.status_code)

    except serial.SerialException:
        print(f"Failed to connect to {serial_port}. Make sure the micro:bit is connected.")
        return

if __name__ == "__main__":
    command = "ls /dev/tty.*"
    pattern = "/dev/tty.usbmodem"

    # Use subprocess to run the command and capture the output
    try:
        output_bytes = subprocess.check_output(command, shell=True)
        
        output_string = output_bytes.decode('utf-8') # This will output a string
        tty_devices = output_string.strip().split('\n') # Convert the string to a list of strings
        
        # Check and select if the list contains a matching element
        matching_devices = [device for device in tty_devices if pattern in device]

        # Print the matching devices
        if matching_devices:
            print("Matching devices found:")
            main(matching_devices[0])
        else:
            print("No matching devices found.")
            quit()
            
    except subprocess.CalledProcessError as e:
        print("Error executing the command:", e)






