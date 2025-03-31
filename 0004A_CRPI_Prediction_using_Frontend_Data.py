## Python program using Streamlit Library for Frontend display
## This program will Predict the CRPI for the data provided (Year, City, Type)
## through Frontnend. It will estimate the Population of the city for the given 
## year. It will categorise the Crime Level Area, It will also calculate the number of Cases as well
## This program will display the Crime Level Area, Predicted CRPI, 
## Estimated Population and Predicted Number of cases

## I) Importing the Python Libraries and other packages
import streamlit as st
from PIL import Image
import pickle
import numpy as np

## II) Loading the Pickke File and opening in "rb (read and binary)" mode
model = pickle.load(open('../Pickle-File/0003B_ML_Model_CRPI_DTC.pkl', 'rb'))

## III) "def" is defining of Python function "run()". ":" is start of the function
def run():
    
    ## 1) Dispalying of "StopCrime" Image on the Frontend Screen
    img1 = Image.open('StopCrime.jpg')
    img1 = img1.resize((156,145))
    st.image(img1,use_column_width=False)    
    
    ## 2) Displaying of Title in the Fronend screen"
    st.title("CRPI Prediction using ML Regression Model")
    
    ## 3) Getting 'year' info through Frontend Screen
    year = st.number_input("Year for which Crime Rate to be predicted",value=2022)  

    ## 4) Getting 'city' info through Frontend Screen
    city_display = ('Ahmedabad', 'Bengaluru', 'Chennai', 'Coimbatore', 'Delhi', 'Ghaziabad', 'Hyderabad', 'Indore', 'Jaipur', 'Kanpur' 'Kochi', 'Kolkata', 'Kozhikode', 'Lucknow', 'Mumbai', 'Nagpur', 'Patna', 'Pune', 'Surat')
    city_options = list(range(len(city_display)))
    city = st.selectbox("Select City:", city_options, format_func=lambda x: city_display[x])
    
    ## 5) Calculation of City Population based on the 'year' info provided
    # Caculating the City Population based on the 'year' provided through Ftondend
    # Here increasing / decreasing the population as per the year.
    # Assuming that the population growth rate is 1% per year.
    if city == 0:
        pop = 63.50 
    elif city == 1:
        pop = 85.0
    elif city == 2:
        pop = 87.0 
    elif city == 3:
        pop = 21.50
    elif city == 4:
        pop = 163.10
    elif city == 5:
        pop = 23.60 
    elif city == 6:
        pop = 77.50
    elif city == 7:
        pop = 21.70 
    elif city == 8:
        pop = 30.70        
    elif city == 9:
        pop = 29.20 
    elif city == 10:
        pop = 21.20
    elif city == 11:
        pop = 141.40 
    elif city == 12:
        pop = 20.30
    elif city == 13:
        pop = 29.0 
    elif city == 14:
        pop = 184.10
    elif city == 15:
        pop = 25.00 
    elif city == 16:
        pop = 25.50
    elif city == 17:
        pop = 50.50 
    else:
        pop = 45.80
         
    year_diff = int(year) - 2011
    year_diff1 = float(year_diff)
    pop1 = 0.01*year_diff1*pop
    pop2 = pop + pop1
    
    ## 6) Getting 'crime type' info through Frontend Screen
    crime_display = ('Crime Committed by Juveniles', 'Crime against SC', 'Crime against ST', 'Crime against Senior Citizen', 'Crime against children',
 'Crime against women', 'Cyber Crimes', 'Economic Offences', 'Kidnapping', 'Murder')
    crime_options = list(range(len(crime_display)))
    crime = st.selectbox("Select Crime Type:", crime_options, format_func=lambda x: crime_display[x])
    
    ## 7) Prediction of Crime Rate of the City using the Pickle file
    ## Predicting the Crime Rate info (cpri) based on the info collected from the 
    ## frontend(year, city, Crime_Type) and the latest Population value of the 
    ## city calculated based on the year provided from the frontend 
    ## using the Pickle file   
    features = [[year, city, pop2, crime]]
    print(features)    
    cpri = model.predict(features)

    ## 8) Calcualtion of Total number of Crime cases
    ## Calculating the Total Number Crime Cases by using the formula
    ## Total Number Crime Cases = cpri * Latest Population of the City
    cases = cpri*pop2
    cases1 = np.round(cases)
        
    ## 9) Categorization of Crime Area
    ## Categorizing the "Crime Area" based on the Crime Rate (CPRI) value    
    if cpri <= 1:
        crime_status = "Very Low Crime Area" 
    elif cpri <= 5:
        crime_status = "Low Crime Area"
    elif cpri <= 15:
        crime_status = "High Crime Area"
    else: 
        crime_status = "Very High Crime Area" 

    ## 10) Displaying of various data in the frontend screen
    ## Displaying of Crime Area, Predicted Crime Rate, Predicted Number of Cases,
    ## calculated Population of the City based 
    ## on the year collected through frontend
    if st.button("Predict_Crime_Rate"):
        st.subheader('Predicted Crime Status :'+'  '+ crime_status)
        cpri1=np.round_(cpri, decimals=4)
        st.subheader('Predicted Crime Rate :'+' '+str(float(cpri1)))
        st.subheader('Predicted Number of Cases :'+'  '+str(int(cases1)))
        st.subheader('Population (in Lakhs) in the year '+ str(year)+" :  "+str(np.round_(pop2, decimals=2)))

## IV) End of the funtion "run()"

## V) Execution of the function "run()"
run()