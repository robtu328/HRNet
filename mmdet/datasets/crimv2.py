from .coco import CocoDataset


class Crimv2Dataset(CocoDataset):
    # 5 weapon classes from crimv2_coco_robo
    CLASSES = ('g', 'h', 'k', 'p', 'r')
