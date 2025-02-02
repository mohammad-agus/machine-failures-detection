import streamlit as st
import requests
import pandas as pd

st.set_page_config("Machine Failure Detection Web App", page_icon="⚙️")
def main():
    st.title("Machine Failures Detection")
    st.image("images/8Rq0.gif")
    st.link_button("Go to the github repo for project details",
                   'https://github.com/mohammad-agus/machine-failures-detection')

    try:
        with st.sidebar:
            st.markdown("## Variables:")
            input_vars = get_response()
        
        df_input_vars = pd.DataFrame(
            data={
                'variable':input_vars.keys(),
                'value':input_vars.values()
            }
        )
        st.dataframe(df_input_vars)
        if st.button("Predict", type='primary'):
            with st.spinner("Please wait, predicting..."):
                response = requests.post(url=st.secrets['API_url'], json=input_vars).json()
            st.write(f'**Machine failure**: {response['failure']}')
            st.write(f'**Probability of failure**: {round(response['failure_probability'], 4)}')

    except:
        st.warning("Input all variables!")



def get_response():

    air_temperature_k = st.slider(
        label="Air temperature (K)",
        value=0.0,
        min_value=290.0,
        max_value=320.0,
        step=0.1
    )

    process_temperature_k = st.slider(
        label="Process temperature (K)",
        value=0.0,
        min_value=290.0,
        max_value=320.0,
        step=0.1
    )

    rotational_speed_rpm = st.slider(
        label="Rotational speed (RPM)",
        value=0,
        min_value=1150,
        max_value=2900,
        step=1
    )

    torque_nm = st.slider(
        label="Torque (Nm)",
        value=0.0,
        min_value=1.0,
        max_value=80.0,
        step=0.1
    )

    tool_wear_min = st.slider(
        label="Tool wear (minutes)",
        value=0.0,
        min_value=0.0,
        max_value=260.0,
        step=0.1
    )

    machine_types = ["L", "M", "H"]
    type = st.pills(
            label="Variants of the machine quality",
            options=machine_types,
            selection_mode='single'
    )

    try:
        input = {
        'type': type.lower(),
        'air_temperature_k': air_temperature_k,
        'process_temperature_k': process_temperature_k,
        'rotational_speed_rpm': rotational_speed_rpm,
        'torque_nm': torque_nm,
        'tool_wear_min': tool_wear_min
        }
    except:
        pass

    return input


 
if __name__ == "__main__":
    main()
