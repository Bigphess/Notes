import numpy as np

class KNearestNeighbor(object):
  """ a kNN classifier with L2 distance """

  def __init__(self):
    pass

  def train(self, X, y):
    """
    Train the classifier. For k-nearest neighbors this is just 
    memorizing the training data.

    Inputs:
    - X: A numpy array of shape (num_train, D) containing the training data
      consisting of num_train samples each of dimension D.
    - y: A numpy array of shape (N,) containing the training labels, where
         y[i] is the label for X[i].
    """
    self.X_train = X
    self.y_train = y
    
  def predict(self, X, k=1, num_loops=0):
    """
    Predict labels for test data using this classifier.

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data consisting
         of num_test samples each of dimension D.
    - k: The number of nearest neighbors that vote for the predicted labels.
    - num_loops: Determines which implementation to use to compute distances
      between training points and testing points.

    Returns:
    - y: A numpy array of shape (num_test,) containing predicted labels for the
      test data, where y[i] is the predicted label for the test point X[i].  
    """
    if num_loops == 0:
      dists = self.compute_distances_no_loops(X)
    elif num_loops == 1:
      dists = self.compute_distances_one_loop(X)
    elif num_loops == 2:
      dists = self.compute_distances_two_loops(X)
    else:
      raise ValueError('Invalid value %d for num_loops' % num_loops)

    return self.predict_labels(dists, k=k)

  def compute_distances_two_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a nested loop over both the training data and the 
    test data.

    Inputs:
    - X: A numpy array of shape (num_test, D) containing test data.

    Returns:返回的也是一个多维数组
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      is the Euclidean distance between the ith test point and the jth training
      point.
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    # print(X[1])
    for i in range(num_test):
      # print(i)
      for j in range(num_train):
        #####################################################################
        # TODO:                                                             #
        # Compute the l2 distance between the ith test point and the jth    #
        # training point, and store the result in dists[i, j]. You should   #
        # not use a loop over dimension.                                    #
        #####################################################################
        # L2dist = 0
        # # 在这张图里操作每个像素，这也太慢了！！！
        # for k in range(X.shape[1]):
        #   # 求两个像素之间的距离的平方,这里的train要加self
        #   L2dist = L2dist + np.square(X[i,k] - self.X_train[j,k])
        # dists[i,j] = np.sqrt(L2dist)
        
        #这里改成了用X[i]直接表示i对应的那行的像素值的和，直接做差（每一项之间），
        # 平方（每一个，求和（所有项），开方。会快很多！！！！

        dists[i,j] = np.sqrt(np.sum(np.square(X[i] - self.X_train[j])))

        # pass
        #####################################################################
        #                       END OF YOUR CODE                            #
        #####################################################################
    return dists

  def compute_distances_one_loop(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using a single loop over the test data.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))
    # print(self.X_train.shape)
    for i in range(num_test):
      #######################################################################
      # TODO:                                                               #
      # Compute the l2 distance between the ith test point and all training #
      # points, and store the result in dists[i, :].                        #
      #######################################################################
      # axis的位置会决定sum的时候加哪个括号，括号从外往里从0增加
      # print(self.X_train - X[i,:])
      dists[i,:] = np.sqrt(np.sum(np.square(self.X_train - X[i,:]),axis = 1))
      
      #######################################################################
      #                         END OF YOUR CODE                            #
      #######################################################################
    return dists

  def compute_distances_no_loops(self, X):
    """
    Compute the distance between each test point in X and each training point
    in self.X_train using no explicit loops.

    Input / Output: Same as compute_distances_two_loops
    """
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train)) 
    #########################################################################
    # TODO:                                                                 #
    # Compute the l2 distance between all test points and all training      #
    # points without using any explicit loops, and store the result in      #
    # dists.                                                                #
    #                                                                       #
    # You should implement this function using only basic array operations; #
    # in particular you should not use functions from scipy.                #
    #                                                                       #
    # HINT: Try to formulate the l2 distance using matrix multiplication    #
    #       and two broadcast sums.                                         #
    #########################################################################
    # square会把每一项都平方
    # 这里求出来的矩阵的大小是500x1，因为是axis = 1，相当于把每行的所有元素求和，然后保存了
    # dims，所以求出来实际是个列向量
    d1 = np.sum(np.square(X),axis = 1,keepdims = True)
    # 大小是1x5000，因为dims默认是false，没有保留括号，拉成了一个行向量
    d2 = np.sum(np.square(self.X_train),axis = 1)
    # 把每个点要求的像素值展开，发现就是train上这个行的平方，求和 + test上这个行的平方，求和
    # 再需要剪去的就是两个矩阵的点乘
    d3 = -2 * np.dot(X, self.X_train.T)
    # d1，d2可以广播，因为他们两个的维数可以对上，最后的大小是500x5000
    dists = np.sqrt(d1 + d2 + d3)
    #########################################################################
    #                         END OF YOUR CODE                              #
    #########################################################################
    return dists

  def predict_labels(self, dists, k=1):
    """
    Given a matrix of distances between test points and training points,
    predict a label for each test point.

    Inputs:
    - dists: A numpy array of shape (num_test, num_train) where dists[i, j]
      gives the distance betwen the ith test point and the jth training point.

    Returns:
    - y: A numpy array of shape (num_test,) containing predicted labels for the
      test data, where y[i] is the predicted label for the test point X[i].  
    """
    # print(dists.min())

    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in range(num_test):

      # A list of length k storing the labels of the k nearest neighbors to
      # the ith test point.
      closest_y = []
      #########################################################################
      # TODO:                                                                 #
      # Use the distance matrix to find the k nearest neighbors of the ith    #
      # testing point, and use self.y_train to find the labels of these       #
      # neighbors. Store these labels in closest_y.                           #
      # Hint: Look up the function numpy.argsort.                             #
      #########################################################################
      # print(np.argsort(dists[i]))
        # 这里输出的就是分类的结果了，所以范围就是0-9
        # print(self.y_train[np.argsort(dists[i])[j]])
      closest_y = self.y_train[np.argsort(dists[i])[:k]]
      # print(closest_y)
      #########################################################################
      # TODO:                                                                 #
      # Now that you have found the labels of the k nearest neighbors, you    #
      # need to find the most common label in the list closest_y of labels.   #
      # Store this label in y_pred[i]. Break ties by choosing the smaller     #
      # label.                                                                #
      #########################################################################
      # 这里得到的是预测结束之后的结果(对每一个测试的图片)
      # 把数组的中数字出现次数变成value，然后把这个值变成index
      fleuArr = np.bincount(closest_y)
      # 返回数组中最大值的index
      # print(np.argmax(fleuArr))
      y_pred[i] = np.argmax(fleuArr)
      #########################################################################
      #                           END OF YOUR CODE                            # 
      #########################################################################

    return y_pred

