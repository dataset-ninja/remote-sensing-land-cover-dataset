Dataset **LoveDA - A Remote Sensing Land-Cover** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/x/9/Fl/9vEdc94lkHcdWll3t2EqyaydsVqWmd8AleS2MyawGwxZYp0tY1Ve1hNZqYb5zR9f2JHGk6TlOS9EM2weQ1aDOGd1u79WfpHxkkqJkimLKC0QBLYPzS2dlZAUiiHs.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='LoveDA - A Remote Sensing Land-Cover', dst_path='~/dtools/datasets/LoveDA - A Remote Sensing Land-Cover.tar')
```
The data in original format can be downloaded here:

- 🔗[Train.zip](https://zenodo.org/record/5706578/files/Train.zip?download=1)
- 🔗[Val.zip](https://zenodo.org/record/5706578/files/Val.zip?download=1)
- 🔗[Test.zip](https://zenodo.org/record/5706578/files/Test.zip?download=1)
