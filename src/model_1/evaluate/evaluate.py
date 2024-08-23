import papermill as pm

def evaluate():
    pm.execute_notebook(
    input_path='src/model_1/evaluete/evaluate.ipynb',
    output_path='src/model_1/evaluete/evaluete_out.ipynb',
    kernel_name='dvc-template-7'
)

if __name__ == '__main__':
    evaluate()