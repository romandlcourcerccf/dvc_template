import papermill as pm

def download():
    pm.execute_notebook(
    input_path='src/model_1/transform/transform.ipynb',
    output_path='src/model_1/transform/transform_out.ipynb',
    kernel_name='dvc-proto'
)

if __name__ == '__main__':
    download()