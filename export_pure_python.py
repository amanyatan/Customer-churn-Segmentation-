import joblib
import m2cgen as m2c
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "models")

model = joblib.load(os.path.join(MODELS_DIR, "xgboost_model.pkl"))
if getattr(model, "base_score", None) is None:
    model.base_score = 0.5

preprocessor = joblib.load(os.path.join(MODELS_DIR, "preprocessor.pkl"))

# Generate XGBoost code
code = m2c.export_to_python(model)
with open(os.path.join(BASE_DIR, "api", "xgboost_pure.py"), "w") as f:
    f.write(code)

# Extract preprocessor logic
numeric_transformer = preprocessor.transformers_[0][1]
categorical_transformer = preprocessor.transformers_[1][1]

num_features = preprocessor.transformers_[0][2]
cat_features = preprocessor.transformers_[1][2]

means = numeric_transformer.mean_.tolist()
scales = numeric_transformer.scale_.tolist()

categories = [list(c) for c in categorical_transformer.categories_]

config = {
    "num_features": num_features,
    "cat_features": cat_features,
    "means": means,
    "scales": scales,
    "categories": categories
}

with open(os.path.join(BASE_DIR, "api", "preprocessor_config.json"), "w") as f:
    json.dump(config, f, indent=4)

print("Export successful!")
