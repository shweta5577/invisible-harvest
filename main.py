"""
main.py
This is the central controller for the 'Invisible Harvest' system.
It coordinates the data flow between the different agents.
"""


# Import our moduless (agents and data)
from data.prices import get_crop_prices
from agents.analyst import calculate_profit
from agents.logistics import find_driver
from agents.communicator import generate_proposal_message, send_whatsapp_message

def main():
    print("--- Invisible Harvest System Starting ---\n")

    # Step 1: Get Prices
    # The Controller asks the Data layer for current market rates.
    print("[System] Fetching prices...")
    current_prices = get_crop_prices()
    print(f"[Debug] Prices found: {current_prices}")

    # Step 2: Analyze Profit
    # The Controller passes price data to the Analyst agent.
    print("[System] Analyzing profit marging...")
    profit_analysis = calculate_profit(current_prices)
    print(f"[Debug] Analysis: {profit_analysis}")

    # Check if we should proceed based on the Analyst's recommendation
    if profit_analysis['is_profitable']:
        
        # PROPOSAL PHASE
        # We only notify the user about the opportunity.
        print("[System] Profit margin is good. Sending proposal...")
        print("\n------------------------------------------------")
        message_content = generate_proposal_message(current_prices, profit_analysis)
        print(message_content)
        print("------------------------------------------------\n")
        
        # SEND WHATSAPP PROPOSAL
        status = send_whatsapp_message(message_content)
        print(f"[Twilio] {status}")
        
    else: 
        print("Profit margin too low. No action taken.")

    print("--- System Finished ---")

if __name__ == "__main__":
    main()
