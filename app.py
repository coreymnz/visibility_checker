import streamlit as st

st.set_page_config(page_title="Visibility Checker", layout="centered")

st.title("Object Visibility Calculator")

# Input fields for object size and distance
size = st.number_input(
    "Object size (m)", min_value=0.001, max_value=10.0, value=0.04, format="%.3f"
)

distance = st.number_input(
    "Distance to observer (m)", min_value=1.0, max_value=10000.0, value=140.0, format="%.1f"
)

# Calculate angular size in arcminutes
angular_arcmin = (size / distance) * 3438

st.markdown(f"**Angular size:** {angular_arcmin:.2f} arcmin")

# Visibility result
if angular_arcmin >= 1:
    st.success("Visible to the naked eye (≥ 1 arcmin)")
else:
    st.error("Too small to see (< 1 arcmin)")

# Optional DSLR pixel estimate
if st.checkbox("Show DSLR pixel estimate (20MP, 50mm lens)"):
    # Approximate: full-frame sensor ~ 5472x3648 px over ~50° FOV
    fov_deg = 50
    pixels_vertical = 3648
    pix_per_deg = pixels_vertical / fov_deg
    pix_size = (angular_arcmin / 60) * pix_per_deg
    st.write(f"Estimated size on sensor: {pix_size:.1f} pixels")

st.markdown("---")
st.write("Feel free to adjust the inputs or expand this app to batch-process CSV files!")
