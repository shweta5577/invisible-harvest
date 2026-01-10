"""
main.py
This is the central controller for the 'Invisible Harvest' system.
It coordinates the data flow between the different agents.
"""

# Import our moduless (agents and data)
from data.prices import get_crop_prices
from agents.analyst import calculate_profit
from agents.logistics import find_driver
from agents.communicator import generate_message

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
        
        # Step 3: Find Driver
        # If profitable, the Controller asks Logistics agent for a driver.
        print("[System] Profit margin is good. Finding transport...")
        transport_details = find_driver("Village Center")
        print(f"[Debug] Transport found: {transport_details}")

        # Step 4: Send Message
        # Finally, the Controller passes everything to the Communicator agent.
        print("[System] Sending notification...")
        print("\n------------------------------------------------")
        generate_message(current_prices, profit_analysis, transport_details)
        print("------------------------------------------------\n")
        
        # Simulate the user checking their phone and replying
        user_reply = input("Reply to message (Type YES to book): ").strip().upper()
        
        if user_reply == "YES":
            print(f"\n[System] Success! Driver {transport_details['driver_name']} has been confirmed.")
            print(f"[System] Estimated pickup cost: ₹{transport_details['cost']}")
        else:
            print("\n[System] No confirmation received. Booking cancelled.")
        
    else: 
        print("Profit margin too low. No action taken.")

    print("--- System Finished ---")

if __name__ == "__main__":
    main()
