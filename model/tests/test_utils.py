import unittest
import math
from model.utils import softmax
from model.utils import smoothLoss
from model.utils import GradientDescentMomentum
from model.utils import crossEntropy
from model.utils import getMask
from model.embedding_layer import EmbeddingLayer
import numpy as np


# looks fine, stepped through tests w/ debugger
class TestUtility(unittest.TestCase):

    def testCrossEntropy(self):
        yhat = np.array([[0.5, 0.1, 0.1, 0.3], [0.8, 0.1, 0.05, 0.05],
                         [0.3, 0.4, 0.2, 0.1]])
        y = np.array([1, 2, 3])
        mask = np.array([True, True, False])
        ce = math.floor(crossEntropy(y, yhat, mask))
        self.assertAlmostEqual(ce, 2)

    def testCrossEntropyBigger(self):
        yhat = np.array([[0.5, 0.1, 0.1, 0.3], [0.8, 0.1, 0.05, 0.05],
                         [0.3, 0.4, 0.2, 0.1], [0.5, 0.2, 0.1, 0.2],
                         [0.8, 0.05, 0.05, 0.1]])
        y = np.array([0, 1, 3, 2, 0])

        mask = np.array([False, True, True, False, False])
        ce = math.floor(crossEntropy(y, yhat, mask))
        self.assertAlmostEqual(ce, 2)

    def testGradientDescent(self):
        params = [np.random.randn(3, 5) for i in range(2)]
        dparams = [np.random.randn(3, 5) for i in range(2)]
        obj = GradientDescentMomentum()
        obj(0.7, params, dparams, True)

    def testMasks(self):
        seq = np.array(([3, 4, 9, 8, 7, 1, 1, 1,
                         1], [4, 5, 6, 7, 8, 9, 1, 1, 1]))
        out = getMask(seq, 1)

    def testSmoothLoss(self):
        obj1 = smoothLoss()
        self.assertEqual(obj1(5.32), 0.9 * 1 + 0.1 * 5.32)

    def testSoftmax1(self):
        logits_prac = np.array([[0.3, 0.2, 0.4, 0.1], [0.6, 0.2, 0.1, 0.1],
                                [0.5, 0.3, 0.1, 0.1]])
        print(softmax(logits_prac))

    def testSoftmax2(self):
        logits_prac2 = np.array([[0.8, 0.2], [0.9, 0.1]])
        print(softmax(logits_prac2))

    def test_embed_forward(self):
        inp_seq = np.array([[3, 2, 1, 4, 0], [0, 0, 1, 1, 2]])
        obj = EmbeddingLayer(5, 3, GradientDescentMomentum)
        output = obj.forward(inp_seq)
        self.assertEqual(output.shape, (2, 5, 3))


if __name__ == "__main__":
    unittest.main()
