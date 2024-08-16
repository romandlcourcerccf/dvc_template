import papermill as pm

pm.execute_notebook(
    input_path='src/model_1/download/download.ipynb',
    output_path='src/model_1/download/download_out.ipynb'
)