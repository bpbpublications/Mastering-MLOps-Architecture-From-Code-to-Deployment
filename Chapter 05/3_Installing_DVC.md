## Installing DVC with pip
```bash
pip install dvc

```

### Setting up DVC
Assuming DVC is already installed in the system, it can be added to the cookie cutter project template by running the following command inside the cookiecutter Git project:
```bash
dvc init

```

### Add file to DVC
Once the data is stored under the data folder, we can start tracking the file using dvc add command. Assuming the filename is data.xml, we can use the following command:
```bash
dvc add data/data.xml

```

### Push file to DVC
Remote storage can be added, data can be pushed and pulled from remote storage using the following commands:
```bash
dvc remote add -d storage s3://mybucket/dvcstore
dvc push
dvc pull

```