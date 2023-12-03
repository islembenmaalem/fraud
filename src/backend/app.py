from fastapi import FastAPI, Request
from pydantic import BaseModel
import pandas as pd
import numpy as np
import mlflow
import mlflow.pyfunc
#setup mlflow
import os
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse
import mlflow.pyfunc
from typing import List, Dict
import uvicorn

load_dotenv()

mlflow_username = os.getenv('MLFLOW_TRACKING_USERNAME')
mlflow_password = os.getenv('MLFLOW_TRACKING_PASSWORD')

print(f'MLFLOW_TRACKING_USERNAME: {mlflow_username}')
print(f'MLFLOW_TRACKING_PASSWORD: {mlflow_password}')
os.environ['MLFLOW_TRACKING_USERNAME']= mlflow_username
os.environ["MLFLOW_TRACKING_PASSWORD"] = "580d73690283aa12650dff07f3881600d00f83c3"
mlflow.set_tracking_uri('https://dagshub.com/islembenmaalem/mlops_project.mlflow')
mlflow.set_experiment("idsd-sd-experiment")


df_mlflow = mlflow.search_runs(filter_string="metrics.F1_score_test<1")
run_id = df_mlflow.loc[df_mlflow['metrics.F1_score_test'].idxmax()]['run_id']

logged_model = f'runs:/{run_id}/ML_models'

model = mlflow.pyfunc.load_model(logged_model)


from pydantic import BaseModel
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse
import mlflow.pyfunc
from typing import List, Dict
import uvicorn


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "to fraud detector app"}


class InputData(BaseModel):
    features: List[dict]

@app.post("/predict_from_csv/")
async def predict_from_csv(file_path: str):
    # Read the CSV data
    input_df = pd.read_csv(file_path)

    results = []

    for _, row in input_df.iterrows():
        prediction = model.predict(pd.DataFrame([row]))
        prediction = int(np.round(prediction[0]))

        results.append({
            'prospectId': 1,
            'productId': 1,
            'fraud': prediction
        })

    return results

@app.post("/predict/")
async def predict(data: InputData):
    results = []
    auth_token = "predict json"
    print(auth_token)

    for features_dict in data.features:
        input_df = pd.DataFrame([features_dict])
        prediction = model.predict(input_df)
        prediction = int(np.round(prediction[0]))  

        results.append({
            'prospectId': 1,
            'productId': 1,
            'fraud': prediction
        })
    response_object = {
        'status': 'success',
        'results': results
    }
    return JSONResponse(content=response_object)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, log_level="debug")






