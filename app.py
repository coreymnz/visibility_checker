import streamlit as st

st.set_page_config(page_title="Visibility Checker", layout="centered")

st.title("Object Visibility Calculator")

# Dropdown for common object sizes
object_options = {
    "Ping-pong ball (40 mm)": 0.04,
    "Soccer ball (220 mm)": 0.22,
    "3 × 3 m building": 3.0,
    "Custom": None
}
selection = st.selectbox("Select object size", list(object_options.keys()))

# Determine object size
if selection != "Custom":
    size = object_options[selection]
    st.write(f"Object size: {size} m")
else:
    size = st.number_input(
        "Custom object size (m)", min_value=0.001, max_value=100.0, value=0.04, format="%.3f"
    )

# Distance input with 1 m step
distance = st.number_input(
    "Distance to observer (m)", min_value=1.0, max_value=10000.0, value=140.0, step=1.0, format="%.1f"
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
