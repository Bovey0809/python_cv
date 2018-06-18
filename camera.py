
# coding: utf-8

# In[1]:


from scipy import linalg


# In[2]:


import numpy as np


# In[3]:


class Camera(object):
    """表示真空照相机的类"""
    def __init__(self, P):
        """初始化照相机模型"""
        self.P = P
        self.K = None
        self.R = None
        self.t = None
        self.c = None
        
    def project(self, X):
        """X的投射点, 并且进行坐标归一化"""
        x = np.dot(self.P, X)
        for i in range(3):
            x[i] /= x[2]
        return x


# In[5]:


points = np.loadtxt('house.p3d').T


# In[7]:


points.shape


# In[8]:


points = np.vstack((points, np.ones(points.shape[1])))


# In[10]:


points.shape


# In[11]:


P = np.hstack((np.eye(3), np.array([[0], [0], [-10]])))


# In[12]:


P


# In[13]:


cam = Camera(P)


# In[14]:


cam


# In[15]:


x = cam.project(points)


# In[16]:


x


# In[17]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[18]:


plt.figure()


# In[19]:


plt.plot(x[0], x[1], 'k.')


# In[20]:


r = 0.05*np.random.rand(3)


# In[23]:


def rotation_matrix(a):
    """Create rotation matrix with pivot a.
    a: a point"""
    R = np.eye(4)
    R[:3, :3] = linalg.expm([[0, -a[2], a[1]], [a[2], 0, -a[0]],[-a[1], a[0], 0]])
    return R


# In[24]:


rot = rotation_matrix(r)


# In[25]:


rot


# In[26]:


plt.figure()


# In[28]:


for t in range(20):
    cam.P = np.dot(cam.P, rot)
    x = cam.project(points)
    plt.plot(x[0], x[1], 'k.')
    plt.show()

