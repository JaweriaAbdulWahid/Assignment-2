import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * conversion_dict[to_unit] / conversion_dict[from_unit]
    return None

# Define unit conversion factors
unit_conversions = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361, "Mile": 0.000621371},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {"Celsius": 1, "Fahrenheit": 33.8, "Kelvin": 274.15},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400},
    "Speed": {"Meter/Second": 1, "Kilometer/Hour": 3.6, "Miles/Hour": 2.23694, "Feet/Second": 3.28084},
    "Area": {"Square Meter": 1, "Square Kilometer": 0.000001, "Square Foot": 10.7639, "Acre": 0.000247105},
    "Volume": {"Liter": 1, "Milliliter": 1000, "Gallon": 0.264172, "Cubic Meter": 0.001},
    "Energy": {"Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilowatt-Hour": 2.77778e-7}
}

# Streamlit UI
st.title("🔢 Unit Converter 🌍")
st.write("Easily convert between different units! 🎯")

# Dropdowns for quantity type and units
quantity = st.selectbox("📏 Select a Quantity:", list(unit_conversions.keys()))
from_unit = st.selectbox("🔄 Convert From:", list(unit_conversions[quantity].keys()))
to_unit = st.selectbox("↔️ Convert To:", list(unit_conversions[quantity].keys()))

# User input for value
value = st.number_input("💡 Enter Value:", min_value=0.0, step=0.1, format="%.2f")

# Perform conversion
if st.button("🚀 Convert"):
    result = convert_units(value, from_unit, to_unit, unit_conversions[quantity])
    if result is not None:
        st.success(f"✅ {value} {from_unit} is equal to {result:.4f} {to_unit} 🎉")
        st.balloons()
    else:
        st.error("❌ Conversion not possible! Please check the units.")

st.write("✨ Made with ❤️ using Streamlit!")
