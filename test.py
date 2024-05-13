import importlib.metadata

lib = ['fastapi',
       'numpy',
       'pandas',
       'joblib',
       'scikit-learn',
       'scipy',
       'pytest',
       'setuptools',
       'wheel',
       'pydantic',
       'uvicorn',
       'gunicorn']

data_dict = {}

for i in lib:
    data_dict[i] = importlib.metadata.version(i)

print(data_dict)
# Change to test pipelines
