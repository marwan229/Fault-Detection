import streamlit as st
import pickle  # For compatibility with older scikit-learn versions

# Load the model
model = pickle.load(open('DecisionTree_detection.sav', 'rb'))

# Function to predict fault
def predict_fault(Ia, Ib,Ic):
  # Prepare the input data (reshape if necessary)
  # Assuming your model expects a 2D array with each row being a sample (3 features)
  data = [[Ia, Ib,Ic]]
  prediction = model.predict(data)[0]
  return prediction

# Streamlit app layout
st.title("Fault Detection App")
st.subheader("Enter three-phase current values:")

current_a = st.number_input("Phase A Current (A)", min_value=0.0)
current_b = st.number_input("Phase B Current (A)", min_value=0.0)
current_c = st.number_input("Phase C Current (A)", min_value=0.0)

if st.button("Predict Fault"):
  prediction = predict_fault(current_a, current_b, current_c)
  if prediction == 0:
    st.success("Healthy")
  else:
    st.error("Fault Detected!")


