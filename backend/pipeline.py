import pandas as pd
import numpy as np
import os
import joblib
import json
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Paths
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'European_Bank.csv')
MODELS_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')
DATA_OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_and_preprocess_data(filepath):
    print("Loading dataset...")
    df = pd.read_csv(filepath)
    
    # 1. Clean data: Remove irrelevant columns
    cols_to_drop = ['Surname', 'CustomerId', 'Year', 'RowNumber']
    cols_to_drop = [c for c in cols_to_drop if c in df.columns]
    df.drop(columns=cols_to_drop, inplace=True)
    
    # Handle any obvious missing values if present (though this dataset is usually clean)
    df.dropna(inplace=True)
    
    # 2. Feature Engineering
    # - Balance-to-Salary ratio
    # Add a small epsilon to avoid division by zero
    df['BalanceSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1e-6)
    
    # - Age-Tenure interaction
    df['AgeTenureInteraction'] = df['Age'] * df['Tenure']
    
    # - Product usage density (Products per year of tenure)
    df['ProductUsageDensity'] = df['NumOfProducts'] / (df['Tenure'] + 1)
    
    return df

def generate_segmentation_analytics(df):
    print("Generating segmentation analytics...")
    
    # Geography Segment
    geo_segment = df.groupby('Geography')['Exited'].agg(['mean', 'count']).reset_index()
    geo_segment.columns = ['Geography', 'ChurnRate', 'TotalCustomers']
    
    # Age groups
    bins = [18, 30, 40, 50, 60, 100]
    labels = ['18-30', '31-40', '41-50', '51-60', '60+']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    age_segment = df.groupby('AgeGroup')['Exited'].agg(['mean', 'count']).reset_index()
    age_segment.columns = ['AgeGroup', 'ChurnRate', 'TotalCustomers']
    
    # Balance Segment
    balance_bins = [-1, 10000, 50000, 100000, 150000, 300000]
    balance_labels = ['0-10k', '10k-50k', '50k-100k', '100k-150k', '150k+']
    df['BalanceSegment'] = pd.cut(df['Balance'], bins=balance_bins, labels=balance_labels)
    balance_segment = df.groupby('BalanceSegment')['Exited'].agg(['mean', 'count']).reset_index()
    balance_segment.columns = ['BalanceSegment', 'ChurnRate', 'TotalCustomers']
    
    # Credit Score Bands
    credit_bins = [300, 580, 670, 740, 800, 900]
    credit_labels = ['Poor', 'Fair', 'Good', 'Very Good', 'Exceptional']
    df['CreditScoreBand'] = pd.cut(df['CreditScore'], bins=credit_bins, labels=credit_labels)
    credit_segment = df.groupby('CreditScoreBand')['Exited'].agg(['mean', 'count']).reset_index()
    credit_segment.columns = ['CreditScoreBand', 'ChurnRate', 'TotalCustomers']

    # Tenure Groups
    tenure_segment = df.groupby('Tenure')['Exited'].agg(['mean', 'count']).reset_index()
    tenure_segment.columns = ['Tenure', 'ChurnRate', 'TotalCustomers']

    segmentation_data = {
        'geography': geo_segment.to_dict(orient='records'),
        'age': age_segment.to_dict(orient='records'),
        'balance': balance_segment.to_dict(orient='records'),
        'credit_score': credit_segment.to_dict(orient='records'),
        'tenure': tenure_segment.to_dict(orient='records'),
        'total_customers': len(df),
        'overall_churn_rate': df['Exited'].mean(),
        'active_users': int(df['IsActiveMember'].sum())
    }
    
    # Save to JSON
    os.makedirs(DATA_OUT_DIR, exist_ok=True)
    with open(os.path.join(DATA_OUT_DIR, 'segmentation_insights.json'), 'w') as f:
        json.dump(segmentation_data, f, indent=4)
        
    # Drop created categorical columns for modeling
    df.drop(columns=['AgeGroup', 'BalanceSegment', 'CreditScoreBand'], inplace=True, errors='ignore')
    return df

def build_and_train_models(df):
    print("Building and training models...")
    X = df.drop(columns=['Exited'])
    y = df['Exited']
    
    # Define categorical and numerical features
    categorical_features = ['Geography', 'Gender']
    numerical_features = [col for col in X.columns if col not in categorical_features]
    
    # Preprocessing pipelines
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Transform data
    X_train_preprocessed = preprocessor.fit_transform(X_train)
    X_test_preprocessed = preprocessor.transform(X_test)
    
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'XGBoost': XGBClassifier(eval_metric='logloss', random_state=42)
    }
    
    results = {}
    
    print("\n--- Model Evaluation ---")
    for name, model in models.items():
        # Train model
        model.fit(X_train_preprocessed, y_train)
        
        # Predict
        y_pred = model.predict(X_test_preprocessed)
        y_prob = model.predict_proba(X_test_preprocessed)[:, 1]
        
        # Metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_prob)
        
        results[name] = {
            'Accuracy': acc,
            'Precision': prec,
            'Recall': rec,
            'F1-score': f1,
            'ROC-AUC': roc_auc
        }
        
        print(f"\n{name} Results:")
        for k, v in results[name].items():
            print(f"{k}: {v:.4f}")
            
    # As requested, XGBoost is the final model
    print("\nSaving final XGBoost model and preprocessor...")
    final_model = models['XGBoost']
    
    os.makedirs(MODELS_DIR, exist_ok=True)
    joblib.dump(final_model, os.path.join(MODELS_DIR, 'xgboost_model.pkl'))
    joblib.dump(preprocessor, os.path.join(MODELS_DIR, 'preprocessor.pkl'))
    
    print("Pipeline completed successfully!")

if __name__ == '__main__':
    df = load_and_preprocess_data(DATA_PATH)
    df = generate_segmentation_analytics(df)
    build_and_train_models(df)
