# Additional pip install needed:
# pip install streamlit matplotlib

import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="Interactive Time Series", layout="centered")
st.title("Interactive Time Series App")
st.write("Use the sliders below to adjust the trend, seasonality and noise level of the generated time series.")

# Create sliders using Streamlit
trend = st.slider("Trend", min_value=-2.0, max_value=2.0, value=0.5, step=0.1)
seasonality = st.slider("Seasonality", min_value=0.0, max_value=3.0, value=1.0, step=0.1)
noise_level = st.slider("Noise Level", min_value=0.0, max_value=2.0, value=0.5, step=0.1)

# Generate sample time series data
def generate_data(trend_param, seasonality_param, noise_param):
    t = np.linspace(0, 4 * np.pi, 100)
    signal = trend_param * t + seasonality_param * np.sin(t) + noise_param * np.random.randn(100)
    return t, signal

# Create the plot
t, signal = generate_data(trend, seasonality, noise_level)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, signal, 'b-', linewidth=2, label='Generated Signal')
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.set_title(f"Interactive Time Series (Trend: {trend}, Seasonality: {seasonality}, Noise: {noise_level})")
ax.grid(True, alpha=0.3)
ax.legend()
fig.tight_layout()

# Display the plot in the app
st.pyplot(fig)
