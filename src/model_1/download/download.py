import papermill as pm


def download():
    pm.execute_notebook(
    input_path='src/model_1/download/download.ipynb',
    output_path='src/model_1/download/download_out.ipynb',
    kernel_name='dvc-template-7'
)

if __name__ == '__main__':
    download()