from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from agents.logistics import find_driver
from agents.communicator import generate_confirmation_message

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    
    print(f"Received: {incoming_msg}")
    
    if 'yes' in incoming_msg:
        # User confirmed! Let's book the driver.
        # In a real app, we would look up the specific proposal ID.
        # Here, we just find the best driver again.
        transport = find_driver("Village Center")
        
        # Generate the confirmation text
        response_text = generate_confirmation_message(transport)
        msg.body(response_text)
        
    else:
        msg.body("I received your message! Reply YES to book a driver.")
        
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
