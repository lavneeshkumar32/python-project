import os
from pathlib import Path

package_name="DiamondPricePrediction"
list_of_files=[
	"github/workflows/.gitkeep",
	f"src/{package_name}/_init_.py",
	f"src/{package_name}/components/data_ingestion.py",
	f"src/{package_name}/components/data_transformation.py",
	f"src/{package_name}/components/model_trainer.py",
	f"src/{package_name}/pipelines/_init_.py",
	f"src/{package_name}/pipelines/training_pipeline.py",
	f"src/{package_name}/pipelines/prediction_pipeline.py",
	f"src/{package_name}/logger.py",
	f"src/{package_name}/exception.py",
	f"src/{package_name}/utils/_init_.py",
	"notebooks/research.ipynb",
	"notebook/data/.gitkeep",
	"requirements.txt",
	"setup.py",
	"init_setup.sh",
	]

# here will create a directory

for filepath in list_of_files:
	filepath=Path(filepath)
	filedir,filename=os.path.split(filepath)

""" how exists_ok works: if "directory" already exists,
os.makedirs() will not raise an error, and it will do nothing.
if "my_directory" doesn't exist , it will create the directory"""	

if filedir !="":
	os.makedirs(filedir,exist_ok=True)
if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
	with open (filepath,"w")as f:
		pass
else:
	print("file already exists")		