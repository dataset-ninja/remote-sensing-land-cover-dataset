import os
import numpy as np
from urllib.parse import unquote, urlparse

import supervisely as sly
from cv2 import connectedComponents
from dataset_tools.convert import unpack_if_archive
from supervisely.io.fs import get_file_name, get_file_name_with_ext
from tqdm import tqdm

import src.settings as s


def download_dataset(teamfiles_dir: str) -> str:
    """Use it for large datasets to convert them on the instance"""
    api = sly.Api.from_env()
    team_id = sly.env.team_id()
    storage_dir = sly.app.get_data_dir()

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
        parsed_url = urlparse(s.DOWNLOAD_ORIGINAL_URL)
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name_with_ext = unquote(file_name_with_ext)

        sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
        local_path = os.path.join(storage_dir, file_name_with_ext)
        teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)
        api.file.download(team_id, teamfiles_path, local_path)

        dataset_path = unpack_if_archive(local_path)

    if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
        for file_name_with_ext, url in s.DOWNLOAD_ORIGINAL_URL.items():
            if file_name_with_ext == "Datasheet.pdf":
                continue
            local_path = os.path.join(storage_dir, file_name_with_ext)
            teamfiles_path = os.path.join(teamfiles_dir, file_name_with_ext)

            if not os.path.exists(get_file_name(local_path)):
                sly.logger.info(f"Downloading '{file_name_with_ext}'...")
                if not os.path.exists(local_path):
                    api.file.download(team_id, teamfiles_path, local_path)

                sly.logger.info(f"Start unpacking archive '{file_name_with_ext}'...")
                unpacked_path = unpack_if_archive(local_path)
                sly.logger.info(f"Archive '{file_name_with_ext}' was unpacked successfully to '{unpacked_path}'.")
                sly.fs.silent_remove(local_path)

            else:
                sly.logger.info(
                    f"Archive '{file_name_with_ext}' was already unpacked to '{os.path.join(storage_dir, get_file_name(file_name_with_ext))}'. Skipping..."
                )

        dataset_path = storage_dir
    return dataset_path


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    objclass_bg = sly.ObjClass("background", sly.Bitmap)
    objclass_building = sly.ObjClass("building", sly.Bitmap)
    objclass_road = sly.ObjClass("road", sly.Bitmap)
    objclass_water = sly.ObjClass("water", sly.Bitmap)
    objclass_barren = sly.ObjClass("barren", sly.Bitmap)
    objclass_forest = sly.ObjClass("forest", sly.Bitmap)
    objclass_agriculture = sly.ObjClass("agriculture", sly.Bitmap)

    idx_to_objclasses = {
        1: objclass_bg,
        2: objclass_building,
        3: objclass_road,
        4: objclass_water,
        5: objclass_barren,
        6: objclass_forest,
        7: objclass_agriculture,
    }

    tag_meta_ptg1 = sly.TagMeta("rural", sly.TagValueType.NONE)
    tag_meta_ptg2 = sly.TagMeta("urban", sly.TagValueType.NONE)

    folder_to_tag_meta = {
        "Rural": tag_meta_ptg1,
        "Urban": tag_meta_ptg2,
    }

    teamfiles_dir = "/4import/LoveDA/"
    rural_dirname = "Rural"
    urban_dirname = "Urban"
    images_dirname = "images_png"
    masks_dirname = "masks_png"
    dataset_path = download_dataset(teamfiles_dir)
    # dataset_path = "/Users/almaz/Downloads/LoveDA/LoveDA - A Remote Sensing Land-Cover"

    def _create_ann(image_path, ds_path, dirname):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]

        image_name = get_file_name_with_ext(image_path)

        masks_dir = os.path.join(ds_path, dirname, masks_dirname)
        mask_path = os.path.join(masks_dir, image_name)
        if not os.path.exists(mask_path):
            return sly.Annotation(img_size=(img_height, img_wight))
        ann_np = sly.imaging.image.read(mask_path)[:, :, 2]
        for i in np.unique(ann_np):
            if i == 0:
                continue
            obj_mask = ann_np == i
            curr_bitmap = sly.Bitmap(obj_mask)
            curr_obj_class = idx_to_objclasses[i]
            if curr_bitmap.area > 100:
                curr_label = sly.Label(curr_bitmap, curr_obj_class)
                labels.append(curr_label)

        tag = sly.Tag(meta=folder_to_tag_meta[dirname])
        return sly.Annotation(img_size=(img_height, img_wight), labels=labels, img_tags=[tag])

    def _process_images_and_annotations(ds, batch, ds_path, dirname, progress_cb):
        images_names = [os.path.basename(img_name) for img_name in batch]

        anns_batch = [_create_ann(image_path, ds_path, dirname) for image_path in batch]
        img_infos = api.image.upload_paths(ds.id, images_names, batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress_cb(len(batch))

    meta = sly.ProjectMeta(
        obj_classes=list(idx_to_objclasses.values()),
        tag_metas=list(folder_to_tag_meta.values()),
    )

    project = api.project.create(workspace_id, project_name)
    api.project.update_meta(project.id, meta.to_json())

    ds_names = os.listdir(dataset_path)
    for ds_name in ds_names:
        ds_path = os.path.join(dataset_path, ds_name, ds_name)
        if os.path.isdir(ds_path):
            dataset = api.dataset.create(project.id, ds_name)
            rural_img_dir = os.path.join(ds_path, rural_dirname, images_dirname)
            urban_img_dir = os.path.join(ds_path, urban_dirname, images_dirname)

            rural_img_names = os.listdir(rural_img_dir)
            urban_img_names = os.listdir(urban_img_dir)
            rural_images = [os.path.join(rural_img_dir, img_name) for img_name in rural_img_names]
            urban_images = [os.path.join(urban_img_dir, img_name) for img_name in urban_img_names]
            all_images = rural_images + urban_images

            pbar = tqdm(desc=f"Processing '{ds_name}' dataset", total=len(all_images))
            for batch in sly.batched(rural_images, batch_size=10):
                _process_images_and_annotations(dataset, batch, ds_path, rural_dirname, pbar.update)
            for batch in sly.batched(urban_images, batch_size=10):
                _process_images_and_annotations(dataset, batch, ds_path, urban_dirname, pbar.update)

    return project
