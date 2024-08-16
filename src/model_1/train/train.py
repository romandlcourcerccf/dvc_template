import papermill as pm

def train():
    pm.execute_notebook(
    input_path='src/model_1/train/train.ipynb',
    output_path='src/model_1/train/train_out.ipynb',
    kernel_name='dvc-proto'
)

if __name__ == '__main__':
    train()