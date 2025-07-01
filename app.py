import streamlit as st

st.set_page_config(page_title="Visibility Checker", layout="centered")
st.title("Object Visibility Calculator")

# Preset object sizes
options = [
    "Ping-pong ball (40 mm)",
    "Soccer ball (220 mm)",
    "3 × 3 m building",
    "Custom"
]

# Show all presets as radio buttons for visibility
selection = st.radio("Select object size:", options)

# Determine object size
if selection == "Ping-pong ball (40 mm)":
    size = 0.04
    st.write("Object size: 0.04 m (Ping-pong ball)")
elif selection == "Soccer ball (220 mm)":
    size = 0.22
    st.write("Object size: 0.22 m (Soccer ball)")
elif selection == "3 × 3 m building":
    size = 3.0
    st.write("Object size: 3.0 m (3 × 3 m building)")
else:
    size = st.number_input(
        "Custom object size (m)",
        min_value=0.001,
        max_value=100.0,
        value=0.04,
        step=0.001,
        format="%.3f"
    )

# Distance input with 1 m step and updated max range
distance = st.number_input(
    "Distance to observer (m)",
    min_value=1.0,
    max_value=20000.0,
    value=140.0,
    step=1.0,
    format="%.1f"
)

# Calculate angular size (arcminutes)
angular_arcmin = (size / distance) * 3438
st.markdown(f"**Angular size:** {angular_arcmin:.2f} arcmin")

# Visibility result
if angular_arcmin >= 1:
    st.success("Visible to the naked eye (≥ 1 arcmin)")
else:
    st.error("Too small to see (< 1 arcmin)")

# Optional DSLR pixel estimate
if st.checkbox("Show DSLR pixel estimate (20MP, 50mm lens)"):
    fov_deg = 50  # Approximate field of view of 50mm lens
    pixels_vertical = 3648  # Full-frame sensor vertical resolution
    pix_per_deg = pixels_vertical / fov_deg
    pix_size = (angular_arcmin / 60) * pix_per_deg
    st.write(f"Estimated size on sensor: {pix_size:.1f} pixels")

st.markdown("---")
st.write("Feel free to adjust the inputs or expand this app to batch-process CSV files!")
