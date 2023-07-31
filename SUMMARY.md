**LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation** is a dataset for a semantic segmentation task. It is used in the geoinformational systems (GIS) domain. 



The dataset consists of 5987 images with 20658 labeled objects belonging to 7 different classes including *background*, *road*, *building*, and other: *forest*, *water*, *agriculture*, and *barren*.

Images in the LoveDA dataset have pixel-level semantic segmentation annotations. Due to the nature of the semantic segmentation task, it can be automatically transformed into an object detection (bounding boxes for every object) task. There are 1796 (30% of the total) unlabeled images (i.e. without annotations). There are 3 splits in the dataset: *Test* (1796 images), *Train* (2522 images), and *Val* (1669 images). The dataset was released in 2021 by the [Wuhan University, China](https://en.whu.edu.cn/).

Here is the visualized example grid with annotations:

<img src="https://github.com/dataset-ninja/remote-sensing-land-cover-dataset/raw/main/visualizations/side_annotations_grid.png">
