import cv2
import os
import glob
import argparse

# settings
parser = argparse.ArgumentParser()
parser.add_argument('--folder_in', type=str, default='./image', metavar='str',
                    help='folder_in: input image folder (default: ./image)')
parser.add_argument('--folder_out', type=str, default='./image_with_label', metavar='str',
                    help='folder_out: output image folder (default: ./image_with_label)')
parser.add_argument('--cam_loc', type=str, metavar='str',
                    help='cam_loc: camera location from [ne, nw, se, sw]')
parser.add_argument('--preview', action='store_true', default=False,
                    help='visualize when processing images')
parser.add_argument('--bgr2rgb', action='store_true', default=False,
                    help='images channels convert from bgr to rgb')
args = parser.parse_args()


# any vehicles within this circle should be labeled.
# Don't modify.
if args.cam_loc == 'nw':
    x0, y0, r = 646, 470, 465
elif args.cam_loc == 'ne':
    x0, y0, r = 630, 482, 465
elif args.cam_loc == 'sw':
    x0, y0, r = None, None, None # todo
elif args.cam_loc == 'se':
    x0, y0, r = None, None, None # todo
else:
    raise NotImplementedError('camera location [%s] not found, pls select one from [ne, nw, se, sw]' % args.cam_loc)


img_dirs = glob.glob(os.path.join(args.folder_in, '*.jpg')) + \
           glob.glob(os.path.join(args.folder_in, '*.png')) + \
           glob.glob(os.path.join(args.folder_in, '*.bmp')) + \
           glob.glob(os.path.join(args.folder_in, '*.tif'))
           
if os.path.exists(args.folder_out) is False:
    os.mkdir(args.folder_out)

for i in range(len(img_dirs)):

    # read an image
    img = cv2.imread(img_dirs[i], cv2.IMREAD_COLOR)
    if args.bgr2rgb:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # draw a circle and save image to disk
    cv2.circle(img, center=(x0, y0), radius=r, color=(0, 0, 255),
               thickness=1, lineType=cv2.LINE_AA)
    cv2.imwrite(img_dirs[i].replace(args.folder_in, args.folder_out), img)

    if args.preview:
        cv2.imshow('img', img)
        cv2.waitKey(1)

    print('%s, processing %d/%d images...' % (img_dirs[i], i+1, len(img_dirs)))

print('----')
print('Complete. You can find your processed images at %s' % (args.folder_out))



