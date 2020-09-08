import unittest
from Utils import softmax
from Utils import smoothLoss
from Utils import GradientDescentMomentum
from Utils import crossEntropy
from Utils import getMask
from Embedding_layer import Embedding_layer
import numpy as np 


# looks fine, stepped through tests w/ debugger 
class tests(unittest.TestCase):
    # def test1(self):
    #     yhat = np.array([[0.5,0.1,0.1,0.3], [0.8,0.1,0.05,0.05], [0.3,0.4,0.2,0.1]])
    #     y = np.array([1,2,3])
    #     mask = np.array([True, True, False])
    #     ce = crossEntropy(y, yhat, mask)


    # def test2(self):
    #     params = [np.random.randn(3,5) for i in range(2)]
    #     dparams = [np.random.randn(3,5) for i in range(2)]
    #     obj = GradientDescentMomentum()
    #     obj(0.7, params, dparams, True)

    # def test3(self):
    #     seq = np.array(([3,4,9,8,7,1,1,1,1],[4,5,6,7,8,9,1,1,1]))
    #     out = getMask(seq, 1)
    #     print(out)


    # def test4(self):
    #     obj1 = smoothLoss()
    #     self.assertEqual(obj1(5.32), 0.9*1 + 0.1*5.32)

    # def test5(self):
    #     logits_prac = np.array([[0.3, 0.2, 0.4, 0.1], [0.6,0.2,0.1,0.1], [0.5,0.3,0.1,0.1]])
    #     print(softmax(logits_prac))

    # def test6(self):
    #     logits_prac2 = np.array([[0.8,0.2], [0.9,0.1]])
    #     print(softmax(logits_prac2))


    def test_embed_forward(self):
        inp_seq = np.array([[3,2,1,4,0], [0,0,1,1,2]])
        obj = Embedding_layer(5, 3, GradientDescentMomentum)
        output = obj._forward(inp_seq)
        self.assertEqual(output.shape, (2,5,3))

    def test_embed_backward(self):
        inp_seq = np.array([[3,2,1,4]])
        obj = Embedding_layer(5, 3, GradientDescentMomentum)
        obj.x = inp_seq 
        dZ = np.array([[0.3, 0.2,0.1], [-0.1, 0.2, 0.3], [0.3, 0.2, 0.7], [0.1,0.5,0.6]])
        obj._backward(dZ, 0.2)
        







if __name__ == "__main__":
    unittest.main() 
