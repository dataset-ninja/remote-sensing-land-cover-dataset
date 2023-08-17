Dataset **LoveDA** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/S/X3/2Rvv7MiSJdV3IGjbAPEQzd5yZOZgK0YG4qho63pvGRBhHs8i7EE6lljJyA2ZSWBtY6jkfOa4N1oIW3yhLoKn8bF3cZ3igckiT06bdsSgZDJQSluVvSPPj8CmUEwQ.tar)

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
