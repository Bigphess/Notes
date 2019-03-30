import numpy as np
from random import shuffle


def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops).

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape)  # initialize the gradient as zero

  # compute the loss and the gradient
  num_classes = W.shape[1]
  # 有多少需要训练的个数
  num_train = X.shape[0]
  loss = 0.0
  for i in range(num_train):
    scores = X[i].dot(W)
    correct_class_score = scores[y[i]]
    for j in range(num_classes):
      # 如果这个类型是正确的，那就不用管了
      if j == y[i]:
        continue
      margin = scores[j] - correct_class_score + 1  # note delta = 1
      if margin > 0:
        loss += margin
        dW[:, y[i]] += -X[i]
        dW[:, j] += X[i]

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train
  dW /= num_train

  # Add regularization to the loss.
  # reg是lanbda
  loss += reg * np.sum(W * W)
  dW += 2 * reg * W
  #############################################################################
  # TODO:                                                                     #
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################

  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  loss = 0.0
  dW = np.zeros(W.shape)  # initialize the gradient as zero

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_classes = W.shape[1]
  scores = X.dot(W)
  # 这里是取第N行（图片行）的第C个（class列），得到的是（500，）的正确类的score的矩阵
  correct_class_score = scores[np.arange(num_train), y]
  correct_class_score = np.repeat(correct_class_score, num_classes)
  correct_class_score = correct_class_score.reshape(num_train, num_classes)

  # NxC
  margin = scores - correct_class_score + 1.0
  margin[np.arange(num_train), y] = 0.0
  margin[margin <= 0] = 0.0

  loss += np.sum(np.sum(margin, axis=1)) / num_train

  # loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  margin[margin > 0] = 1.0
  calculate_times = np.sum(margin, axis=1)
  margin[np.arange(num_train), y] = - calculate_times

  dW = np.dot(X.T, margin) / num_train
  dW += 2 * reg * W

  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
