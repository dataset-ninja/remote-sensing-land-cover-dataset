from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "LoveDA"
PROJECT_NAME_FULL: str = (
    "LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation"
)

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.BY_NC_SA_4_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Domain.GIS()]
CATEGORY: Category = Category.Aerial(extra=Category.Satellite())

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_DATE: Optional[str] = "2021-10-15"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = "https://zenodo.org/record/5706578#.YZvN7SYRXdF"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 886655
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/remote-sensing-land-cover-dataset"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Datasheet.pdf": "https://zenodo.org/record/5706578/files/Datasheet.pdf?download=1",
    "Train.zip": "https://zenodo.org/record/5706578/files/Train.zip?download=1",
    "Val.zip": "https://zenodo.org/record/5706578/files/Val.zip?download=1",
    "Test.zip": "https://zenodo.org/record/5706578/files/Test.zip?download=1",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = {
    "background": [87, 4, 79],
    "building": [152, 95, 173],
    "road": [17, 24, 149],
    "water": [180, 207, 210],
    "barren": [180, 162, 54],
    "forest": [134, 203, 67],
    "agriculture": [135, 102, 1],
}
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[
    str
] = "https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/file/4e732ced3463d06de0ca9a15b6153677-Paper-round2.pdf"
CITATION_URL: Optional[str] = "https://github.com/Junjue-Wang/LoveDA#citation"
AUTHORS: Optional[List[str]] = [
    "Junjue Wang",
    "Zhuo Zheng",
    "Ailong Ma",
    "Xiaoyan Lu",
    "Yanfei Zhong",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = "Wuhan University, China"
ORGANIZATION_URL: Optional[Union[str, List[str]]] = "https://en.whu.edu.cn/"

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {"area": ["rural", "urban"]}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
