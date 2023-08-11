# IoT Worksheet 3

The objective of this is to communicate a microbit with a server. I have chose FastAPI as the server. A middleware exists to read and write serial data to and from the server and the microbit. The microbit will send "Hello" as serial data using a print function when button 'A' is pressed. This data will be decoded into a string in the middleware and a get request to the root route of the server is sent which will return a response of "Hello, world!". This response is then forwarded to the microbit and displayed on the microbit screen.

## How it works

1. When the button is pressed, the microbit executes a print function which will be sent through the serial stream.
2. In the computer, the middleware program will be listening for any data using the pyserial library on the specific serial port with the specific baudrate, 115200.
3. When it receives the data from the microbit, using requests library, sends a get request to the running fast api server.
4. The fast api server receives the the request at the endpoint and sends a response back to the middleware where it will be sent back to through the serial port to the microbit.
5. Now, the microbit will be contantly listening for serial data and as soon as it receives, the data, using the uart library, The data will be decoded and displayed on the microbit screen.

## Libraries Used

- `pyserial`
- `requests`
- `uart`
- `fastapi`
- `uvicorn`

## How to Run

One way is to simply hit `ctrl` + `F5` in VSCode after selecting 'FastAPI/Middleware' configuration in the debug section

### Manually

```bash
python3 -m venv .venv
pip install -r requirements.txt
uvicorn server:app --reload
python middleware.py
```

### Flash to Microbit

- Either flash the code from [https://python.microbit.org/](https://python.microbit.org/)
- Or, simply copy the hex file to the Microbit storage
