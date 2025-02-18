import streamlit as st
import requests
import pandas as pd
import pickle
import xgboost as xgb


st.set_page_config("Machine Failure Detection Web App", page_icon="⚙️")
st.image("images/alpha-perspective-Pw5jK6yjJR4-unsplash.jpg")
st.caption("_Photo by Alpha Perspective on Unsplash_")


def main():

    model_path = 'machine-failures-detection-service/xgb_clf.bin'

    with open(model_path, 'rb') as f:
        model, dv = pickle.load(f)

    st.title("Machine Failures Detection")
    st.divider()
    st.markdown("### **Observation that will be predicted:**")
    try:
        with st.sidebar:
            st.markdown("## Variables:")
            input_vars = get_input_variables()
        
        df_input_vars = pd.DataFrame(
            data={
                'variable':input_vars.keys(),
                'value':input_vars.values()
            }
        )
        st.dataframe(df_input_vars)
        if st.button("Predict", type='primary'):
            st.markdown("### **Prediction:**")
            
            with st.spinner("Please wait, predicting..."):

                
                #response = requests.post(url=st.secrets['API_url'], json=input_vars).json()
                

                X = dv.transform([input_vars])
                dX = xgb.DMatrix(X, feature_names=dv.feature_names_)

                y_pred = model.predict(dX)
                failure = y_pred >= 0.5

                result = {
                    'failure': bool(failure),
                    'failure_probability': float(y_pred)
                }

            
            #with st.container():
            #    st.write(f'**Machine failure**: {response['failure']}')
            #    st.write(f'**Probability of failure**: {round(response['failure_probability'], 4)}')
            

            with st.container():
                st.write(f'**Machine failure**: {result['failure']}')
                st.write(f'**Probability of failure**: {round(result['failure_probability'], 4)}')

            st.write("")
            st.divider() 
            st.markdown('### Contact Information')
            st.markdown(
            """ 
            - **Email** : mohammad_agus@outlook.com
            - **LinkedIn** : [in/moh-agus](https://www.linkedin.com/in/moh-agus/)
            - **Github** : [mohammad-agus](https://github.com/mohammad-agus)

            Go to the [github repository]('https://github.com/mohammad-agus/machine-failures-detection') for project details!
            """
            )


    except:
        st.warning("Input all variables!")



def get_input_variables():

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
