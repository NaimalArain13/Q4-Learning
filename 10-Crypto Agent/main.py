from runner import main
import streamlit as st
import asyncio

# Page configuration
st.set_page_config(page_title="Crypto Data Agent", page_icon="₿", layout="wide")

# Custom CSS for better styling
st.markdown(
    """
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #f7931a;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #333;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #f7931a;
    }
</style>
""",
    unsafe_allow_html=True,
)

st.markdown('<h1 class="main-header">₿ Crypto Data Agent</h1>', unsafe_allow_html=True)

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a section:", ["Quick Questions", "Custom Query","About"])

if page == "Quick Questions":
    st.markdown(
        '<h2 class="sub-header">Quick Crypto Questions</h2>', unsafe_allow_html=True
    )

    # Predefined questions
    question_type = st.selectbox(
        "What would you like to know about crypto?",
        [
            "Select a question type...",
            "Get information about a specific cryptocurrency",
            "Get first 10 cryptocurrencies",
            "Get global crypto market information",
            "Get market cap data for a cryptocurrency",
        ],
    )

    if question_type == "Get information about a specific cryptocurrency":
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.write(
            "**Popular cryptocurrencies:** BTC, ETH, ADA, DOT, LINK, LTC, BCH, XRP"
        )
        st.markdown("</div>", unsafe_allow_html=True)

        symbol = st.text_input(
            "Enter cryptocurrency symbol (e.g., BTC, ETH):", placeholder="BTC"
        )
        if st.button("Get Crypto Info", type="primary"):
            if symbol:
                with st.spinner("Fetching cryptocurrency information..."):
                    try:
                        response = asyncio.run(
                            main(f"Get information about {symbol} cryptocurrency")
                        )
                        print("RESPONSE", response)
                        st.success("Data retrieved successfully!")
                        st.write(response)
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please enter a cryptocurrency symbol.")

    elif question_type == "Get first 10 cryptocurrencies":
        if st.button("Get First 10 Cryptocurrencies", type="primary"):
            with st.spinner("Fetching first 10 cryptocurrencies..."):
                try:
                    response = asyncio.run(main("Get first 10 cryptocurrencies"))
                    st.success("Data retrieved successfully!")
                    print("RESPONSE", response)
                    st.write(response)

                except Exception as e:
                    st.error(f"Error: {str(e)}")

    elif question_type == "Get global crypto market information":
        if st.button("Get Global Market Info", type="primary"):
            with st.spinner("Fetching global market information..."):
                try:
                    response = asyncio.run(
                        main("Get global cryptocurrency market information")
                    )
                    st.success("Data retrieved successfully!")
                    print("RESPONSE", response)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    elif question_type == "Get market cap data for a cryptocurrency":
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        st.write("**Select a cryptocurrency to get its market cap data:**")
        st.markdown("</div>", unsafe_allow_html=True)

        # Popular cryptocurrencies with their symbols
        popular_cryptos = {
            "Bitcoin (BTC)": "BTC",
            "Ethereum (ETH)": "ETH",
            "Cardano (ADA)": "ADA",
            "Polkadot (DOT)": "DOT",
            "Chainlink (LINK)": "LINK",
            "Litecoin (LTC)": "LTC",
            "Bitcoin Cash (BCH)": "BCH",
            "Ripple (XRP)": "XRP",
            "Solana (SOL)": "SOL",
            "Polygon (MATIC)": "MATIC",
        }

        selected_crypto = st.selectbox(
            "Choose a cryptocurrency:",
            ["Select a cryptocurrency..."] + list(popular_cryptos.keys()),
        )

        if st.button("Get Market Cap Data", type="primary"):
            if selected_crypto != "Select a cryptocurrency...":
                with st.spinner(f"Getting market cap data for {selected_crypto}..."):
                    try:
                        # First get the ID for the selected cryptocurrency
                        symbol = popular_cryptos[selected_crypto]
                        print("SYMBOL",symbol)
                        id_response = asyncio.run(
                            main(f"Get the ID for {symbol} cryptocurrency")
                        )
                        print("ID RESPONSE:", id_response, type(id_response))

                        if isinstance(id_response, str):
                            crypto_id = id_response
                        elif isinstance(id_response, dict) and "id" in str(id_response):
                            import re

                            id_match = re.search(
                                r'id["\']?\s*:\s*["\']?(\d+)["\']?', str(id_response)
                            )
                            if id_match:
                                crypto_id = id_match.group(1)
                            
                      

                        # Now get the market cap data using the ID
                        print("CRYPTO ID",crypto_id)
                        market_cap_response = asyncio.run(
                            main(
                                f"Get market cap data for cryptocurrency ID {crypto_id}"
                            )
                        )
                        print("MARKET CAP RESPONSE:", market_cap_response)
                        st.success("Market cap data retrieved successfully!")
                        st.write(market_cap_response)

                    except Exception as e:
                        st.error(f"Error: {str(e)}")
            else:
                st.warning("Please select a cryptocurrency.")

elif page == "Custom Query":
    st.markdown('<h2 class="sub-header">Custom Query</h2>', unsafe_allow_html=True)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.write("**Available capabilities:**")
    st.write("• Get cryptocurrency information by symbol (BTC, ETH, etc.)")
    st.write("• Get all available cryptocurrencies")
    st.write("• Get global crypto market statistics")
    st.write("• Get market cap data by cryptocurrency ID")
    st.markdown("</div>", unsafe_allow_html=True)

    custom_input = st.text_area(
        "Enter your custom query:",
        placeholder="Example: What is the current price of Bitcoin?",
        height=100,
    )

    if st.button("Run Custom Query", type="primary"):
        if custom_input:
            with st.spinner("Processing your query..."):
                try:
                    response = asyncio.run(main(custom_input))
                    st.success("Query completed successfully!")
                    print("RESPONSE", response)
                    st.write(response)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a query.")

elif page == "About":
    st.markdown(
        '<h2 class="sub-header">About the Crypto Data Agent</h2>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <div class="info-box">
        <h3>What can this agent do?</h3>
        <p>This Crypto Data Agent provides real-time cryptocurrency information using the CoinLore API. It can:</p>
        <ul>
            <li>Fetch information about specific cryptocurrencies by symbol</li>
            <li>Get a list of all available cryptocurrencies</li>
            <li>Retrieve global cryptocurrency market statistics</li>
            <li>Access market cap data for specific cryptocurrencies</li>
        </ul>
    <h3>How to use:</h3>
    <ul>
        <li>Use <strong>Quick Questions</strong> for common queries with predefined options</li>
        <li>Use <strong>Custom Query</strong> to ask questions in natural language</li>
        <li>The agent will automatically choose the best tool to answer your question</li>
    </ul>
    <h3>Popular cryptocurrency symbols:</h3>
    <p>BTC, ETH, ADA, DOT, LINK, LTC, BCH, XRP, SOL, MATIC</p>
       <p>This agent is built using the CoinLore API and Streamlit. It is a simple agent that can be used to get information about cryptocurrencies.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666;'>Powered by CoinLore API | Built with Streamlit by Naimal❤️</p>",
    unsafe_allow_html=True,
)
