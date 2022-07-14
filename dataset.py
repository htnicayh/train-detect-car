import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset(
    'open-images-v6', split='train', classes=['car'], max_samples=20)
dataset = foz.load_zoo_dataset(
    'open-images-v6', split='validation', classes=['car'], max_samples=20)
