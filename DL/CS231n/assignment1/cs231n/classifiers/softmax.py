import numpy as np
from random import shuffle


def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

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
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_class = W.shape[1]
  num_train = X.shape[0]

  for i in range(num_train):
    # size(1,C)
    scores = X[i].dot(W)
    scores = np.exp(scores)
    # 减去平均数，以0为中心分布
    scores_sum = np.sum(scores)
    correct_class_score = scores[y[i]]

    for j in range(num_class):
      percent = scores[j] / scores_sum
      # print(percent)
      if j == y[i]:
        margin = - np.log(percent)
        dW[:, j] += (-1 + percent) * X[i]
        # print(margin)
        if margin > 0:
          loss += margin
      else:
        dW[:, j] += percent * X[i]

  loss /= num_train
  loss += reg * np.sum(W * W)
  dW = dW / num_train
  dW += reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)
  num_class = W.shape[1]
  num_train = X.shape[0]

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  # size（N，C）
  scores = X.dot(W)
  scores = np.exp(scores)
  # 对每行求和
  scores_sum = np.sum(scores, axis=1)
  scores_sum = np.repeat(scores_sum, num_class)
  scores_sum = scores_sum.reshape(num_train, num_class)
  # true_divide返回浮点数，普通的返回正数，size（N，C）
  percent = np.true_divide(scores, scores_sum)

  # 只有正确种类需要求loss
  Li = -np.log(percent[np.arange(num_train), y])
  loss = np.sum(Li)

  # 注意这里不需要求log
  dS = percent.copy()
  dS[np.arange(num_train), y] += -1
  dW = (X.T).dot(dS)

  loss /= num_train
  loss += reg * np.sum(W * W)
  dW /= num_train
  dW += reg * W

  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
