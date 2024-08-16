model_1_download:
	python src/model_1/download/download.py

model_1_transform:
	python src/model_1/transform/transform.py

model_1_train:
	python src/model_1/train/train.py

model_1_run_pipeline: model_1_download model_1_transform model_1_train

model_2_download:
	python src/model_2/download/download.py

model_2_transform:
	python src/model_2/transform/transform.py

model_2_train:
	python src/model_2/train/train.py

model_2_run_pipeline: model_2_download model_2_transform model_2_train