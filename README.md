# IoT Worksheet 3 - Password unlocking system

So the aim of this project is to simulate the authorization of users when the correct button combination is pressed. This project involves three things, a microbit which sends the button combination, an interceptor program which listens on the microbits serial port for serial data transmission and a fastapi server connected to a database which validates users credentials.

## How it works

1. The microbit checks if a button combination is entered within a timeframe of 2 seconds right after the last button is pressed.
2. If there is a button combination, the microbit will send serial data to the computer using a print function.
3. The interceptor program which contantly listens on the microbits serial port will receive the data and a post request with that data is sent to the fastapi server.
4. When the server receives the request, it fetches all the passwords which matches the password from the request and responds with either Authorized or Unauthorized.
5. The interceptor program will then receive the response which will be sent back to the microbit using pyserial.
6. The microbit will be listening constantly for serial data from the computer using the uart library, and as soon as it receives the response data from the interceptor program, it then displays it on the microbit screen.

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
