The **LoveDA: Land-cOVEr Domain Adaptive Semantic Segmentation** dataset was introduced to advance the fields of semantic learning and transferable learning. The LoveDA dataset comprises 5987 HSR images with 166768 annotated objects collected from three different cities, spanning both ***urban*** and ***rural*** domains. This diversity brings significant challenges, including multi-scale objects, complex background samples, and inconsistent class distributions. The LoveDA dataset is well-suited for tasks related to land-cover semantic segmentation and unsupervised domain adaptation (UDA).

Deep learning approaches have demonstrated substantial potential in the realm of high spatial resolution (HSR) land-cover mapping in remote sensing. Nevertheless, urban and rural environments often present significantly distinct geographical landscapes, posing challenges to the generalizability of such algorithms, especially in city-level or national-level mapping scenarios. Many existing HSR land-cover datasets primarily promote research into learning semantic representation, often neglecting the issue of model transferability.

<img src="https://github.com/supervisely/dataset-tools/assets/78355358/07aac5a6-9e98-40fd-83db-ba822a3e4128" alt="image" width="800">

<span style="font-size: smaller; font-style: italic;">Overview of the dataset distribution. The images were collected from Nanjing, Changzhou, and Wuhan cities, covering 18 different administrative districts.</span>

The LoveDA dataset is a valuable resource for promoting large-scale land-cover mapping. Its key characteristics include multi-scale objects, complex background samples, and inconsistent class distributions, providing real-world complexity for researchers working on semantic segmentation and UDA tasks. By focusing on the style differences between geographical environments, LoveDA presents a distinct challenge in UDA compared to general computer vision datasets.

## Image Distribution and Division

The LoveDA dataset was assembled from 0.3 m RGB images collected in Nanjing, Changzhou, and Wuhan, covering a total area of 536.15 km². This dataset consists of both urban and rural scenes, promoting diversity. Nine urban areas were carefully selected from economically developed districts characterized by high population density (>1000 people/km²). Concurrently, nine rural areas were chosen from less developed districts. After undergoing geometric registration and pre-processing, each area was represented by non-overlapping 1024 × 1024 images.

The LoveDA dataset is suitable for evaluating two primary tasks: **Semantic Segmentation** and **UDA**. For the first, eight areas are allocated for training, while the remainder are designated for validation and testing. These sets encompass both urban and rural regions. For the second, the UDA process addresses two cross-domain adaptation sub-tasks: 

   a) **Urban to Rural**: The source training set includes images from the Qinhuai, Qixia, Jianghan, and Gulou areas, while the validation set incorporates images from Liuhe and Huangpi. The test set contains images from Jiangning, Xinbei, and Liyang. The Oracle setting serves to test the upper limit of accuracy within a single domain, hence the training images originate from the Pukou, Lishui, Gaochun, and Jiangxia areas.

   b) **Rural to Urban**: In this case, the source training set comprises images from the Pukou, Lishui, Gaochun, and Jiangxia areas. The validation set uses images from Yuhuatai and Jintan, with the test set utilizing images from Jiangye, Wuchang, and Wujin. These settings explore model adaptability between rural and urban environments, posing unique challenges for the UDA task.

It can be evaluated for two tasks: semantic segmentation and unsupervised domain adaptation (UDA). The data division ensures spatial independence among training, validation, and test sets for these tasks.

| Domain | City          | Region   | #Images | Train | Val  | Test  |
| ------ | -------------  | -------  | ------- | ----- | ---- | ----- |
| Urban  | Nanjing       | Qixia    | 320     | X     |     |       |
| Urban  | Nanjing       | Gulou    | 320     | X     |     |       |
| Urban  | Nanjing       | Qinhuai  | 336     | X     |     |       |
| Urban  | Nanjing       | Yuhuatai | 357     |       |  X  |       |
| Urban  | Nanjing       | Jianye  | 357     |       |     |  X    |
| Urban  | Changzhou     | Jintan  | 320     |      |  X   |       |
| Urban  | Changzhou     | Wujin   | 320     |      |     |   X    |
| Urban  | Wuhan         | Jianghan | 180     | X     |     |       |
| Urban  | Wuhan         | Wuchang  | 143     |      |     |    X   |
| Rural  | Nanjing       | Pukou   | 320     | X     |     |       |
| Rural  | Nanjing       | Gaochun | 336     | X     |     |       |
| Rural  | Nanjing       | Lishui  | 336     | X     |     |       |
| Rural  | Nanjing       | Liuhe   | 320     |      |  X   |       |
| Rural  | Nanjing       | Jiangning | 336   |      |     |    X   |
| Rural  | Changzhou     | Liyang  | 320     |      |     |   X    |
| Rural  | Changzhou     | Xinbei  | 320     |      |     |   X    |
| Rural  | Wuhan         | Jiangxia | 374     | X     |     |       |
| Rural  | Wuhan         | Huangpi | 672     |      |   X  |       |
|        |               | Total   | 5987    | 2522  | 1669 | 1796  |


<img src="https://github.com/supervisely/dataset-tools/assets/78355358/41c1e786-4226-4c4e-891a-84e69fc5251f" alt="image" width="600">

## Statistics for LoveDA

The dataset exhibits the largest number of labeled pixels and land-cover objects compared to other HSR land-cover datasets. The urban scenes in LoveDA contain diverse man-made objects, whereas rural areas are dominated by agricultural land. Spectral statistics show consistency in mean values and lower standard deviations for rural images, indicating more homogeneous areas. The presence of multi-scale objects necessitates models with multi-scale capture capabilities, particularly for large-scale land cover mapping tasks, thus increasing the challenge of model transferability in the face of varying urban and rural scenes.

<img src="https://github.com/supervisely/dataset-tools/assets/78355358/aa2aa42a-c309-41e7-b1ba-d734085f90a3" alt="image" width="800">

