# Fisheye Image Annotation Tutorial

[Michigan Traffic Lab, University of Michigan](https://traffic.engin.umich.edu/)

This repo provides a toolbox for image annotation. It also provides a brief tutorial on how to label fisheye traffic images for vehicle detection. This repo is based on [Labelme](https://github.com/wkentaro/labelme), an open source graphical image annotation toolbox.



## Installation

Install [Anaconda](https://www.continuum.io/downloads) first, then run below to install [Labelme](https://github.com/wkentaro/labelme) and [opencv-python](https://pypi.org/project/opencv-python/):

```shell
conda create --name=labelme python=3.6
conda activate labelme
pip install labelme
pip install opencv-python
```

Clone this repo:

```shell
git clone https://github.com/michigan-traffic-lab/fisheye-image-annotation.git 
cd ./fisheye-image-annotation
```

## Usage

### Pre-processing

Before annotating your images, copy your images to the `./image` folder and run the following script to mark a valid area on each of them. The boundary of the valid area is marked by a big red circle. **Any on-road vehicles within that circle should be annotated**. This can help you exclude those targets that are too far away and save annotation time. 

```shell
conda activate labelme
python preproc.py --folder_in ./image --folder_out ./image_with_label --preview
```

After the pre-processing, you can find your processed images in the folder `./image_with_label` .

### Annotation

Activate anaconda environment and open the Labelme software interface:

```shell
conda activate labelme
labelme --labels labels.txt --nodata --autosave
```

Please follow the steps below to annotate your images.

1. Select your image folder here. By default, the folder should be `./image_with_label` that you just have created, which contains those images after pre-processing.

   ![](./gallery/1.png)

2. Right-click and then select "Create LineStrip"

   ![](./gallery/2.png)

3. Consider each vehicle as a cuboid. Annotate the **bottom rectangle** of each of the vehicles with three vertices (Apparently, you only need three points instead of four to determine their bottom face). Choose a vehicle type from the drop-down menu ("car", "pickup", "van", "truck", "bus", "motorbike", and "others"). 

   ![](./gallery/3.png)

4. When you finish labeling all vehicles within the valid area, click "Next Image" to move on to the next one. Finally, all the annotations are saved as [JSON](http://www.json.org/) files in the same image directory. The following screenshot shows how your image folders will look like after annotating all images. You can reload them to check whether the annotation looks correct. 

   ![](./gallery/4.png)



## Things to know

1. Any on-road vehicles within the red circle should be annotated. The vehicles located in parking lots should be ignored, even within the circle. All the vehicles outside the circle should be ignored. 
2. When labeling the bottom rectangle of each vehicle, the order of the three vertices doesn't matter. You may either start from a vehicle's head then goes to its tail, or do it in the opposite way. 
3. If a vehicle is too small, you can use "Ctrl + scroll wheel" to zoom-in and zoom-out.
4. If you accidentally mislabeled any of the vehicles, try right-click --> "Edit Polygons" and "Edit Label" to correct them.
5. Sometimes it is hard to find the exact location of the vertices especially when the vehicles are too far away from the camera. Then, don't worry. If there are errors, just let them be.  Such errors are acceptable, and the deep neural network will learn to tolerate them during the training process.
6. Sometimes there could be bottom vertices that may have the same pixel location. If they do, you can either mark twice the same pixel location or makes a minor shift of your cursor on labeling them. 
7. The category label "others" refers to those special vehicles such as agricultural vehicles, bulldozers, cranes, etc.
8. If you have any further questions, please contact Dr. Zhengxia Zou (zzhengxi@umich.edu).
