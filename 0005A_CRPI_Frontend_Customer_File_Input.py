## Program Goals:
## a) To predict the Crime rates for the given customer data in "CPRI-customer.csv" file


## I) Importing the Python Libraries and other packages
import pandas as pd
import streamlit as st
from PIL import Image
import pickle
import time
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

## II) Loading the Pickke File and opening in "rb (read and binary)" mode
model = pickle.load(open('../Pickle-File/0003B_ML_Model_CRPI_DTC.pkl', 'rb'))

## III) Dispalying of "StopCrime" Image on the Frontend Screen
img1 = Image.open('StopCrime.jpg')
img1 = img1.resize((156,145))
st.image(img1,use_column_width=False)    

## IV) Displaying of Title in the Fronend screen"
st.title("CRPI Prediction using ML Regression Model")


## V)  Customer Data File browsing and reading from Frontend

#<---------------Customer Data file reading Starts------------------------>
st.text('Customer Data file reading starts...')
uploaded_file = st.file_uploader("Choose a file")
time.sleep(10)
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  #df["Year"]=df["Year"].astype('int')
  st.text('Input Customer file Data')
  st.text('Customer Data file reading ends...')
  st.write(df.shape)
  st.text('Displaying the first 5 records of Customer Data file')
  st.write(df.head(5))
time.sleep(5)
df1=df.copy()
#<---------------Customer Data file reading Ends-------------------------->

time.sleep(10)

# VI) Customer Data File preprocessing

#<-------Customer Data Preprocessing Starts------------------------------->
st.text('Customer Data Preprocessing starts...')

# VII) Converting "City" column based data from "Object" to "Integer"
le = preprocessing.LabelEncoder()
df1['City'] = le.fit_transform(df1.City.values)
df1['Type'] = le.fit_transform(df1.Type.values)

time.sleep(10)
st.text('Customer Data Preprocessing ends...')
time.sleep(5)
#<-------Customer Data Preprocessing Ends------------------------------->

## VIII) Prediction CRPI values for the given Customer Data and its display
#<-------Customer Data Prediction Starts-------------------------------->
st.text('Customer Data based CPRI Prediction process starts...')
time.sleep(5)
df2=df.copy()
prediction = model.predict(df1)
df2["Pred_CRPI"]=prediction

st.text('Customer Data with Predicted Values')

st.write(df2.head(5))
time.sleep(5)
st.text('Customer Data based CPRI Prediction process ends...')
time.sleep(5)
#<-------Customer Data Prediction Ends-------------------------------->

## IX) Downloading and writing out of Customer Data with Predicted values file to a Local Folder

#<-------Customer Data with Prediction Values file Downloading Start------>
st.text('Customer Data file with Predicted values downloading Process starts...')
time.sleep(5)

def convert_df(df2):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df2.to_csv().encode('utf-8')

csv1 = convert_df(df2)

df2.to_csv("D:/CRPI-Latest1/Frontend-Output-Files/0005A_Cust_Data_with_pred_values.csv", index = False)
#---------------------------------------------------------------------------
progress_text = "Downloading of CSV file is in progress. Please wait. ⏳"
my_progress_bar = st.progress(0)
status_text = st.empty()

for percent_complete in range(0, 101):
    time.sleep(0.02)
    my_progress_bar.progress(percent_complete)
    status_text.text(f"{progress_text} {percent_complete}%")

status_text.text("File has been downloaded! ⌛")
my_progress_bar.empty()
#---------------------------------------------------------------------------
## X) Display the Output .csv File writing out and Project completion info on to the Frotnend screen
time.sleep(5)

st.text('Downloaded file into your "Frontend-Output-Files" folder')
st.title('Execution of "CRPI Prediction Solution" is completed...Thanks...')
