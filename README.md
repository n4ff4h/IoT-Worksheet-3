# IoT Worksheet 3

The objective of this is to communicate a microbit with a server. I have chose FastAPI as the server. A middleware exists to read and write serial data to and from the server and the microbit. The microbit will send "Hello" as serial data using a print function when button 'A' is pressed. This data will be decoded into a string in the middleware and a get request to the root route of the server is sent which will return a response of "Hello, world!". This response is then forwarded to the microbit and displayed on the microbit screen.

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
