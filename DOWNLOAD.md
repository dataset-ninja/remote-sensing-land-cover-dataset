Dataset **LoveDA** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://www.dropbox.com/scl/fi/8zj6978szhrd5y791imzc/loveda-DatasetNinja.tar?rlkey=fnrrxye1ltjnj9h1gfkv9f6uu&dl=1)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='LoveDA', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be downloaded here:

- [Datasheet.pdf](https://zenodo.org/record/5706578/files/Datasheet.pdf?download=1)
- [Train.zip](https://zenodo.org/record/5706578/files/Train.zip?download=1)
- [Val.zip](https://zenodo.org/record/5706578/files/Val.zip?download=1)
- [Test.zip](https://zenodo.org/record/5706578/files/Test.zip?download=1)
