from typing import Dict, List, Optional, Union

from dataset_tools.templates import AnnotationType, CVTask, Industry, License

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "LoveDA - A Remote Sensing Land-Cover"
PROJECT_NAME_FULL: str = "LoveDA: A Remote Sensing Land-Cover Dataset for Domain Adaptive Semantic Segmentation"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.BY_NC_SA_4_0()
INDUSTRIES: List[Industry] = [Industry.Satellite()]
CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]

RELEASE_YEAR: int = 2021
HOMEPAGE_URL: str = "https://zenodo.org/record/5706578#.YZvN7SYRXdF"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 0
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/remote-sensing-land-cover-dataset"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
  "Train.zip": "https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/Y/a/xu/gicWjDi0o8XZuc2HSZ67qp9TaC4imnhAI2iTJd4bwvxczL3FWsv8M6dPyWYbVV3SdMbifL8veLJ6nBq5pCppaMJ4AVv7ODQub51FdwkciYpJ1VkbBXJ8jRZE2bkB.zip",
  "Val.zip": "https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/5/xe/h7pCO3wYFQ7z1fLqVzexwrZ5trEJkQ0EMNQjcZoBXkySK3OOwecPOe7DQUlIbJvyUi1V8jmsMARE3OcXlHx4WiNChhM4F786Vrky446W2U8vTaqekhrx6oMHaRSx.zip",
  "Test.zip": "https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/a/t/6x/5mJlxSTs2sPxM9aLeu8L6k74z9502n3cMBL20fIRWeZfK4Nb2KiMkk1FB9XOHSY4hHK17SQQgVtVnd1OdSMflFkg3BHOYO2SGZdxS37MBf482Nd4N1QinvwNLRyJ.zip"
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = None
CITATION_URL: Optional[str] = "https://zenodo.org/record/5706578/export/hx"
ORGANIZATION_NAME: Optional[Union[str, List[str]]] = None
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "industries": INDUSTRIES,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["tags"] = TAGS if TAGS is not None else []

    return settings
