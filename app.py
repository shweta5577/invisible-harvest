"""
app.py
The Streamlit-based web interface for 'Invisible Harvest'.
"""
import streamlit as st
import time

# Import our existing agents
# Since we are running `streamlit run invisible_harvest/app.py`, 
# we need to make sure python can find the modules.
# We will use relative imports assuming the script is run as a module or fix path.

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from data.prices import get_crop_prices
from agents.analyst import calculate_profit
from agents.logistics import find_driver
from agents.communicator import generate_message, send_whatsapp_message

# PAGE CONFIG
st.set_page_config(page_title="Invisible Harvest", page_icon="🌾")

# HEADER
st.title("🌾 Invisible Harvest")
st.subheader("Agent-based Crop Logistics System")

# SIDEBAR STATUS
with st.sidebar:
    st.header("System Status")
    st.success("Agents Online")
    st.info("Market: OPEN")

# STEP 1: LOAD DATA
st.divider()
st.write("### 1. Market Data")

if st.button("Fetch Current Prices"):
    with st.spinner("Agents contacting markets..."):
        time.sleep(1) # Dramatic pause for effect
        prices = get_crop_prices()
        st.session_state['prices'] = prices
        st.json(prices)
        
        # Auto-run analysis if prices mock fetched
        st.session_state['analyzed'] = False

# STEP 2: ANALYSIS
if 'prices' in st.session_state:
    st.divider()
    st.write("### 2. Profit Analysis")
    
    prices = st.session_state['prices']
    analysis = calculate_profit(prices)
    
    col1, col2 = st.columns(2)
    col1.metric("Margin/kg", f"₹{analysis['margin_per_kg']}")
    col2.metric("Profitable?", "YES" if analysis['is_profitable'] else "NO")
    
    if analysis['is_profitable']:
        st.success("Analysis complete: Recommended to SELL.")
        st.session_state['analysis'] = analysis
    else:
        st.error("Analysis complete: NOT Recommended.")

# STEP 3: LOGISTICS & ACTION
if 'analysis' in st.session_state and st.session_state['analysis']['is_profitable']:
    st.divider()
    st.write("### 3. Logistics & Communication")
    
    # Run only if we haven't found a driver yet
    if 'logistics' not in st.session_state:
        with st.spinner("Finding nearest driver..."):
            time.sleep(0.5)
            logistics = find_driver("Village Center")
            st.session_state['logistics'] = logistics
    
    logistics = st.session_state['logistics']
    st.info(f"Driver Found: **{logistics['driver_name']}** (Cost: ₹{logistics['cost']})")
    
    # Show the message
    st.markdown("#### Preview Message")
    msg = generate_message(st.session_state['prices'], st.session_state['analysis'], logistics)
    st.code(msg, language="text")
    
    # Action Button
    if st.button("Reply 'YES' to Book"):
        st.balloons()
        st.success(f"CONFIRMED: Driver {logistics['driver_name']} is on the way!")
        
        with st.spinner("Sending WhatsApp Confirmation..."):
            status = send_whatsapp_message(msg)
            
        if "Error" in status:
            st.warning(f"Twilio Status: {status}")
        else:
            st.success(f"Twilio Status: {status}")
