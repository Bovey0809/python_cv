from PIL import Image
from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

def normolize(points):
    '''在齐次坐标下, 对点集进行归一化, 使最后一行为1'''
    for row in points:
        row /= points[-1]
    return points

def make_homog(points):
    '''将点集(dimxn的数组)转换为齐次坐标表示'''
    return np.vstack((points, ones((1, points.shape[1]))))


im = np.array(Image.open('homography.png').convert('L'))

print(Image.open('homography.png').convert('L'))

H = np.array([[1.4, 0.05, -100],[0.05, 1.5, -100], [0, 0, 1]])
im2 = ndimage.affine_transform(im, H[:2, :2], (H[0, 2], H[1, 2]))

plt.imshow(plt.imread('homography.png'))
plt.show()
plt.imshow(im)
plt.figure()
plt.gray()
plt.imshow(im2)
plt.show()
plt.waitforbuttonpress()
plt.close()
