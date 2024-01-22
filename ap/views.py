from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_selection import mutual_info_regression
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.neighbors import KNeighborsRegressor
import os
import pandas as pd
import json
##name	sector	price	price_earnings	dividend_yield	earnings_share	52_week_low	52_week_high
	## market_cap	ebitda	price_sales	price_book	52_week_add	52_week_sub	52_week_div	52_week_mul
def predict(request):
    file_path = os.path.join(os.path.dirname(__file__), 'sp_companies_best_model.pkl')
    model = joblib.load(file_path)

    df = pd.DataFrame.from_dict([request.data])
    df.head()
    res = model.predict(df)
    return {"results" : res}
@api_view(['GET'])
def get_analysis(request):
    result = predict(request)
    return Response(result)