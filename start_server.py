import os
import sys
from pyngrok import ngrok
from server import app
import threading

def start_ngrok():
    # Open a HTTP tunnel on the default port 5000
    # <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:5000">
    public_url = ngrok.connect(5000).public_url
    print(f"\n * Ngrok Tunnel Started: {public_url}")
    print(f" * COPY THIS URL and paste it into Twilio Sandbox Configuration as: {public_url}/whatsapp\n")

if __name__ == "__main__":
    # Start ngrok in a separate thread to not block Flask
    # Actually, we can just start it before app.run
    try:
        start_ngrok()
        app.run(port=5000)
    except KeyboardInterrupt:
        print("Shutting down...")
