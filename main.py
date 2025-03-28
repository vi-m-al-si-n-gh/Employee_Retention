from flask import Flask, request, render_template, send_file
from flask import Response
import pandas as pd
import os
from flask_cors import CORS, cross_origin
from apps.training.train_model import TrainModel
from apps.prediction.predict_model import PredictModel
from apps.core.config import Config

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST','GET'])
def index_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def predict_page():
    return render_template('predict.html')

@app.route('/batch-predict', methods=['POST','GET'])
def batch_predict_page():
    return render_template('batch_predict.html')

@app.route('/train', methods=['POST','GET'])
def train_page():
    return render_template('train.html')

@app.route('/about', methods=['POST','GET'])
def about_page():
    return render_template('about.html')

@app.route('/team')
def team_page():
    return render_template('team.html')

@app.route('/download', methods=['GET'])
def download_file():
    try:
        classpath = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(classpath,r"C:\Users\KIIT\Downloads\Employee_Retention_ML-main (2)\Employee_Retention_ML-main\data\prediction_data_results\Predictions.csv")
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return Response("File not found!", status=404)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.training_data_path
        #trainmodel object initialization
        trainModel=TrainModel(run_id,data_path)
        #training the model
        trainModel.training_model()
        return Response("Training successfull! and its RunID is : "+str(run_id))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
@app.route('/batchprediction', methods=['POST'])
@cross_origin()
def batch_prediction_route_client():
    try:
        config = Config()
        run_id = config.get_run_id()
        data_path = config.prediction_data_path

        if 'file' not in request.files:
            return Response("No file uploaded", status=400)

        file = request.files['file']
        if file.filename == '':
            return Response("No file selected", status=400)

        # Save uploaded file to the prediction data path
        file_path = os.path.join(data_path, file.filename)
        file.save(file_path)

        # Prediction object initialization
        predictModel = PredictModel(run_id, data_path)

        # Perform batch prediction
        predictions = predictModel.batch_predict_from_model()

        # Convert predictions to DataFrame and save as CSV
        predictions_df = pd.DataFrame(predictions, columns=['Predictions'])
        predictions_csv_path = os.path.join(data_path, f"batch_predictions_{run_id}.csv")
        predictions_df.to_csv(predictions_csv_path, index=False)

        return Response(f"Prediction successful! RunID: {run_id}. CSV stored at: {predictions_csv_path}")

    except (ValueError, KeyError) as e:
        return Response("Error Occurred! %s" % e)
    except Exception as e:
        return Response("Error Occurred! %s" % e)
@app.route('/prediction', methods=['POST'])
@cross_origin()
def single_prediction_route_client():
    try:
        config = Config()
        #get run id
        run_id = config.get_run_id()
        data_path = config.prediction_data_path
        print('Test')

        if request.method == 'POST':
            satisfaction_level = request.form['satisfaction_level']
            last_evaluation = request.form["last_evaluation"]
            number_project = request.form["number_project"]
            average_montly_hours = request.form["average_montly_hours"]
            time_spend_company = request.form["time_spend_company"]
            work_accident = request.form["work_accident"]
            promotion_last_5years = request.form["promotion_last_5years"]
            salary = request.form["salary"]

            data = pd.DataFrame(data=[[0 ,satisfaction_level, last_evaluation, number_project,average_montly_hours,time_spend_company,work_accident,promotion_last_5years,salary]],
                              columns=['empid','satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','salary'])
            # using dictionary to convert specific columns
            convert_dict = {'empid': int,
                            'satisfaction_level': float,
                            'last_evaluation': float,
                            'number_project': int,
                            'average_montly_hours': int,
                            'time_spend_company': int,
                            'Work_accident': int,
                            'promotion_last_5years': int,
                            'salary': object}

            data = data.astype(convert_dict)

            # object initialization
            predictModel = PredictModel(run_id, data_path)
            # prediction the model
            output = predictModel.single_predict_from_model(data)
            print('output : '+str(output))
            return Response("Predicted Output is : "+str(output))
    except ValueError:
        return Response("Error Occurred! %s" % ValueError)
    except KeyError:
        return Response("Error Occurred! %s" % KeyError)
    except Exception as e:
        return Response("Error Occurred! %s" % e)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)