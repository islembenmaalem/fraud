import streamlit as st
from dotenv import load_dotenv
import requests

load_dotenv()

#mlflow_username = os.getenv('MLFLOW_TRACKING_USERNAME')
#mlflow_password = os.getenv('MLFLOW_TRACKING_PASSWORD')

#print(f'MLFLOW_TRACKING_USERNAME: {mlflow_username}')
#print(f'MLFLOW_TRACKING_PASSWORD: {mlflow_password}')
#os.environ['MLFLOW_TRACKING_USERNAME']= mlflow_username
#os.environ["MLFLOW_TRACKING_PASSWORD"] = "580d73690283aa12650dff07f3881600d00f83c3"
#mlflow.set_tracking_uri('https://dagshub.com/islembenmaalem/mlops_project.mlflow')
#mlflow.set_experiment("idsd-sd-experiment")


#df_mlflow = mlflow.search_runs(filter_string="metrics.F1_score_test<1")
#run_id = df_mlflow.loc[df_mlflow['metrics.F1_score_test'].idxmax()]['run_id']

#logged_model = f'runs:/{run_id}/ML_models'

#model = mlflow.pyfunc.load_model(logged_model)

st.title("Fraud Detector App")

st.write("## Enter Data for Prediction")

amt = st.number_input("Amount", min_value=0.0)
cc_num = st.number_input("Credit Card Number", min_value=0)
hour = st.number_input("Hour", min_value=0)
category = st.selectbox("Category", ["grocery_pos", 'shopping_net','misc_net','shopping_pos','gas_transport','misc_pos','kids_pets','entertainment','personal_care','home','food_dining','grocery_net','health_fitness','travel'])
month = st.number_input("Month", min_value=1, max_value=12)
city_pop = st.number_input("City Population", min_value=0)
age = st.number_input("Age", min_value=0)
gender = st.selectbox("Gender", ["M", "F"])  
zip_code = st.number_input("Zip Code", min_value=0)
state = st.selectbox("State", ['NC', 'WA', 'ID', 'MT', 'VA', 'PA', 'KS', 'TN', 'IA', 'WV', 'FL',
       'CA', 'NM', 'NJ', 'OK', 'IN', 'MA', 'TX', 'WI', 'MI', 'WY', 'HI',
       'NE', 'OR', 'LA', 'DC', 'KY', 'NY', 'MS', 'UT', 'AL', 'AR', 'MD',
       'GA', 'ME', 'AZ', 'MN', 'OH', 'CO', 'VT', 'MO', 'SC', 'NV', 'IL',
       'NH', 'SD', 'AK', 'ND', 'CT', 'RI', 'DE']) 
job = st.selectbox("Job", ['Psychologist, counselling', 'Special educational needs teacher',
       'Nature conservation officer', 'Patent attorney',
       'Dance movement psychotherapist', 'Transport planner',
       'Arboriculturist', 'Designer, multimedia',
       'Public affairs consultant', 'Pathologist', 'IT trainer',
       'Systems developer', 'Engineer, land', 'Systems analyst',
       'Naval architect', 'Radiographer, diagnostic',
       'Programme researcher, broadcasting/film/video', 'Energy engineer',
       'Event organiser', 'Operational researcher', 'Market researcher',
       'Probation officer', 'Leisure centre manager',
       'Corporate investment banker', 'Therapist, occupational',
       'Call centre manager', 'Police officer',
       'Education officer, museum', 'Physiotherapist', 'Network engineer',
       'Forensic psychologist', 'Geochemist',
       'Armed forces training and education officer',
       'Designer, furniture', 'Optician, dispensing',
       'Psychologist, forensic', 'Librarian, public', 'Fine artist',
       'Scientist, research (maths)', 'Research officer, trade union',
       'Tourism officer', 'Human resources officer', 'Surveyor, minerals',
       'Applications developer', 'Video editor', 'Curator',
       'Research officer, political party', 'Engineer, mining',
       'Education officer, community', 'Physicist, medical',
       'Amenity horticulturist', 'Electrical engineer',
       'Television camera operator', 'Higher education careers adviser',
       'Ambulance person', 'Dealer', 'Paediatric nurse',
       'Trading standards officer', 'Engineer, technical sales',
       'Designer, jewellery', 'Clinical biochemist',
       'Engineer, electronics', 'Water engineer', 'Science writer',
       'Film/video editor', 'Solicitor, Scotland',
       'Product/process development scientist', 'Tree surgeon',
       'Careers information officer', 'Geologist, engineering',
       'Counsellor', 'Freight forwarder',
       'Senior tax professional/tax inspector',
       'Engineer, broadcasting (operations)',
       'English as a second language teacher', 'Economist',
       'Child psychotherapist', 'Claims inspector/assessor',
       'Tourist information centre manager',
       'Exhibitions officer, museum/gallery', 'Location manager',
       'Engineer, biomedical', 'Research scientist (physical sciences)',
       'Purchasing manager', 'Editor, magazine features',
       'Operations geologist', 'Interpreter', 'Engineering geologist',
       'Agricultural consultant', 'Paramedic', 'Financial adviser',
       'Administrator, education', 'Educational psychologist',
       'Financial trader', 'Audiological scientist',
       'Scientist, audiological',
       'Administrator, charities/voluntary organisations',
       'Health service manager', 'Retail merchandiser',
       'Telecommunications researcher', 'Exercise physiologist',
       'Accounting technician', 'Product designer',
       'Waste management officer', 'Mining engineer', 'Surgeon',
       'Therapist, horticultural', 'Environmental consultant',
       'Broadcast presenter', 'Producer, radio',
       'Engineer, communications',
       'Historic buildings inspector/conservation officer',
       'Teacher, English as a foreign language', 'Materials engineer',
       'Health visitor', 'Medical secretary', 'Theatre director',
       'Technical brewer', 'Land/geomatics surveyor',
       'Engineer, structural', 'Diagnostic radiographer',
       'Television production assistant', 'Medical sales representative',
       'Building control surveyor', 'Therapist, sports',
       'Structural engineer', 'Commercial/residential surveyor',
       'Database administrator', 'Exhibition designer',
       'Training and development officer', 'Mechanical engineer',
       'Medical physicist', 'Administrator', 'Mudlogger',
       'Fisheries officer', 'Conservator, museum/gallery',
       'Programmer, multimedia', 'Cytogeneticist',
       'Multimedia programmer', 'Counselling psychologist', 'Chiropodist',
       'Teacher, early years/pre', 'Cartographer', 'Pensions consultant',
       'Primary school teacher', 'Electronics engineer',
       'Museum/gallery exhibitions officer', 'Air broker',
       'Chemical engineer', 'Advertising account executive',
       'Advertising account planner',
       'Chartered legal executive (England and Wales)',
       'Psychiatric nurse', 'Secondary school teacher',
       'Librarian, academic', 'Embryologist, clinical', 'Immunologist',
       'Television floor manager', 'Contractor', 'Health physicist',
       'Copy', 'Bookseller', 'Land', 'Chartered loss adjuster',
       'Occupational psychologist', 'Facilities manager',
       'Further education lecturer', 'Archivist', 'Investment analyst',
       'Engineer, building services', 'Psychologist, sport and exercise',
       'Journalist, newspaper', 'Doctor, hospital', 'Phytotherapist',
       'Pharmacologist', 'Horticultural therapist', 'Hydrologist',
       'Community arts worker', 'Public house manager', 'Architect',
       'Lexicographer', 'Psychotherapist, child',
       'Teacher, secondary school', 'Toxicologist',
       'Commercial horticulturist', 'Podiatrist', 'Building surveyor',
       'Architectural technologist', 'Editor, film/video',
       'Social researcher', 'Wellsite geologist', 'Minerals surveyor',
       'Designer, ceramics/pottery', 'Mental health nurse',
       'Volunteer coordinator', 'Chief Technology Officer',
       'Camera operator', 'Copywriter, advertising', 'Surveyor, mining',
       'Product manager', "Nurse, children's", 'Pension scheme manager',
       'Archaeologist', 'Sub', 'Designer, interior/spatial',
       'Futures trader', 'Chief Financial Officer',
       'Museum education officer', 'Quantity surveyor',
       'Physiological scientist', 'Loss adjuster, chartered',
       'Pilot, airline', 'Production assistant, radio',
       'Immigration officer', 'Retail banker',
       'Health and safety adviser', 'Teacher, special educational needs',
       'Jewellery designer', 'Community pharmacist',
       'Control and instrumentation engineer', 'Make',
       'Early years teacher', 'Sales professional, IT',
       'Scientist, marine', 'Intelligence analyst',
       'Clinical research associate', 'Administrator, local government',
       'Barrister', 'Engineer, control and instrumentation',
       'Clothing/textile technologist', 'Development worker, community',
       'Art therapist', 'Sales executive',
       'Armed forces logistics/support/administrative officer',
       'Optometrist', 'Insurance underwriter', 'Charity officer',
       'Civil Service fast streamer', 'Retail buyer',
       'Magazine features editor', 'Equities trader',
       'Trade mark attorney', 'Research scientist (life sciences)',
       'Psychotherapist', 'Pharmacist, community', 'Risk analyst',
       'Engineer, maintenance', 'Logistics and distribution manager',
       'Water quality scientist', 'Lecturer, further education',
       'Production assistant, television', 'Tour manager',
       'Music therapist', 'Surveyor, land/geomatics',
       'Engineer, production', 'Acupuncturist', 'Hospital doctor',
       'Teacher, primary school', 'Accountant, chartered public finance',
       'Illustrator', 'Scientist, physiological', 'Buyer, industrial',
       'Scientist, research (physical sciences)', 'Radio producer',
       'Manufacturing engineer', 'Animal technologist',
       'Production engineer', 'Biochemist, clinical',
       'Engineer, manufacturing', 'Comptroller',
       'General practice doctor', 'Designer, industrial/product',
       'Prison officer', 'Merchandiser, retail', 'Engineer, drilling',
       'Engineer, petroleum', 'Cabin crew', 'Commissioning editor',
       'Accountant, chartered certified', 'Local government officer',
       'Professor Emeritus', 'Press sub',
       'Chartered public finance accountant', 'Writer',
       'Chief Executive Officer', 'Occupational hygienist',
       'Doctor, general practice', 'Community education officer',
       'Landscape architect', 'Occupational therapist',
       'Special effects artist', 'Civil engineer, contracting',
       "Barrister's clerk", 'Travel agency manager',
       'Associate Professor', 'Neurosurgeon', 'Plant breeder/geneticist',
       'Radio broadcast assistant', 'Field seismologist',
       'Industrial/product designer', 'Metallurgist',
       "Politician's assistant", 'Insurance claims handler',
       'Theme park manager', 'Gaffer', 'Chief Strategy Officer',
       'Heritage manager', 'Ceramics designer', 'Animator',
       'Oceanographer', 'Colour technologist', 'Engineer, agricultural',
       'Therapist, drama', 'Orthoptist', 'Learning mentor',
       'Arts development officer', 'Biomedical engineer',
       'Race relations officer', 'Therapist, music', 'Retail manager',
       'Furniture designer', 'Building services engineer',
       'Maintenance engineer', 'Aid worker', 'Editor, commissioning',
       'Private music teacher', 'Scientist, biomedical',
       'Public relations account executive', 'Dispensing optician',
       'Advice worker', 'Hydrographic surveyor', 'Geoscientist',
       'Environmental health practitioner', 'Learning disability nurse',
       'Chief Operating Officer', 'Scientific laboratory technician',
       'Records manager', 'Barista', 'Marketing executive',
       'Tax inspector', 'Musician', 'Therapist, art',
       'Engineer, automotive', 'Clinical psychologist', 'Warden/ranger',
       'Surveyor, rural practice', 'Sport and exercise psychologist',
       'Education administrator', 'Chief of Staff',
       'Nurse, mental health', 'Music tutor',
       'Planning and development surveyor',
       'Teaching laboratory technician', 'Chief Marketing Officer',
       'Theatre manager', 'Quarry manager',
       'Interior and spatial designer', 'Lecturer, higher education',
       'Regulatory affairs officer', 'Secretary/administrator',
       'Chemist, analytical', 'Designer, exhibition/display',
       'Pharmacist, hospital', 'Site engineer',
       'Equality and diversity officer', 'Public librarian',
       'Town planner', 'Chartered accountant', 'Programmer, applications',
       'Manufacturing systems engineer', 'Web designer',
       'Community development worker', 'Animal nutritionist',
       'Petroleum engineer', 'Information systems manager',
       'Press photographer', 'Insurance risk surveyor', 'Soil scientist',
       'Buyer, retail', 'Public relations officer',
       'Health promotion specialist', 'Psychiatrist',
       'Visual merchandiser', 'Rural practice surveyor', 'Hotel manager',
       'Communications engineer', 'Insurance broker',
       'Radiographer, therapeutic', 'Set designer', 'Tax adviser',
       'Drilling engineer', 'Fitness centre manager', 'Farm manager',
       'Management consultant', 'Energy manager',
       'Museum/gallery conservator', 'Herbalist', 'Osteopath',
       'Statistician', 'Hospital pharmacist', 'Estate manager/land agent',
       'Sports development officer', 'Investment banker, corporate',
       'Biomedical scientist', 'Television/film/video producer',
       'Nutritional therapist', 'Company secretary', 'Production manager',
       'Magazine journalist', 'Media buyer', 'Data scientist',
       'Engineer, civil (contracting)', 'Herpetologist',
       'Garment/textile technologist', 'Scientist, research (medical)',
       'Civil Service administrator', 'Airline pilot', 'Textile designer',
       'Environmental manager', 'Furniture conservator/restorer',
       'Horticultural consultant', 'Firefighter',
       'Geophysicist/field seismologist', 'Psychologist, clinical',
       'Development worker, international aid', 'Sports administrator',
       'IT consultant', 'Presenter, broadcasting',
       'Outdoor activities/education manager', 'Field trials officer',
       'Social research officer, government',
       'English as a foreign language teacher',
       'Restaurant manager, fast food', 'Hydrogeologist',
       'Research scientist (medical)', 'Designer, television/film set',
       'Geneticist, molecular', 'Designer, textile',
       'Licensed conveyancer', 'Emergency planning/management officer',
       'Geologist, wellsite', 'Air cabin crew', 'Seismic interpreter',
       'Surveyor, hydrographic', 'Charity fundraiser', 'Stage manager',
       'Aeronautical engineer', 'Glass blower/designer', 'Ecologist',
       'Horticulturist, commercial', 'Research scientist (maths)',
       'Engineer, aeronautical',
       'Conservation officer, historic buildings', 'Art gallery manager',
       'Advertising copywriter', 'Engineer, civil (consulting)',
       'Oncologist', 'Engineer, materials',
       'Scientist, clinical (histocompatibility and immunogenetics)',
       'Investment banker, operational', 'Medical technical officer',
       'Academic librarian', 'Artist', 'Clinical cytogeneticist',
       'TEFL teacher', 'Administrator, arts', 'Teacher, adult education',
       'Catering manager', 'Environmental education officer',
       'Conservator, furniture', 'Analytical chemist',
       'Broadcast engineer', 'Media planner', 'Lawyer',
       'Producer, television/film/video',
       'Armed forces technical officer', 'Engineer, site',
       'Contracting civil engineer', 'Veterinary surgeon',
       'Sales promotion account executive', 'Broadcast journalist',
       'Dancer', 'Forest/woodland manager', 'Personnel officer',
       'Industrial buyer', 'Accountant, chartered',
       'Air traffic controller', 'Careers adviser', 'Information officer',
       'Ship broker', 'Legal secretary', 'Homeopath', 'Solicitor',
       'Warehouse manager'])  

# Create a dictionary with the input data
input_data = {
    "amt": amt,
    "cc_num": cc_num,
    "hour": hour,
    "category": category,
    "month": month,
    "city_pop": city_pop,
    "age": age,
    "gender": gender,
    "zip": zip_code,
    "state": state,
    "job": job
}
input_data_json={
  "features": [
  input_data
    ]
}
#API_URL = "http://localhost:8000"
#API_URL = "http://backend:8000"
API_URL = "https://backendfrauddetection.onrender.com"
API_URL = "https://bb-96pa.onrender.com"
# Define a function to make predictions
def predict_fraud(data):
    #input_df = pd.DataFrame([data])
  #  prediction = int(np.round(model.predict(input_df)[0]))  # Adjust if needed
    response_json1 = requests.post(f"https://backendfrauddetection.onrender.com/predict/", json=input_data_json)
    response_json = requests.post(f"https://bb-96pa.onrender.com/predict/", json=input_data_json)
    return response_json1.json(),response_json.json()

if st.button("Predict"):
    response_json1,response_json = predict_fraud(input_data)
    st.write("## Prediction")
    st.write("Fraud: {}".format(response_json1["results"][0]["fraud"]))
    st.write("## Prediction")
    st.write("Fraud: {}".format(response_json["results"][0]["fraud"]))
