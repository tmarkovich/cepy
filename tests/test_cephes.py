from __future__ import division
import random
from unittest import TestCase

import numpy as np
import scipy.special as special

from cepy import bdtr
from cepy import betaln
from cepy import btdtr
from cepy import gamln
from cepy import gammainc
from cepy import ndtri
from cepy import pdtr


np.seterr(all="ignore")


def allClose(a, b):
    global_truth = True
    for i in range(len(a)):
        local_truth = True
        if round(a[i] - b[i], 5) != 0:
            local_truth = False
        if np.isnan(a[i]) and np.isnan(b[i]):
            local_truth = True
        if np.isinf(a[i]) and np.isinf(b[i]):
            local_truth = True
        global_truth = local_truth
    return global_truth


class _TestOneArgFn(object):

    def test_fn(self):
        values = [self.fn(x) for x in self.vals]
        exact_values = [self.refFn(x) for x in self.vals]
        np.testing.assert_almost_equal(values, exact_values)


class _TestTwoArgFn(object):

    def test_fn(self):
        values = []
        exact_values = []
        for x in self.vals:
            for y in self.vals:
                values.append(self.fn(x, y))
                exact_values.append(self.refFn(x, y))
        np.testing.assert_almost_equal(values, exact_values)


class _TestThreeArgFn(object):

    def test_fn(self):
        values = []
        exact_values = []
        for x in self.vals:
            for y in self.vals:
                for z in self.vals:
                    values.append(self.fn(x, y, z))
                    exact_values.append(self.refFn(x, y, z))
        np.testing.assert_almost_equal(values, exact_values)


class TestGamln(TestCase, _TestOneArgFn):

    def ref(self, x):
        return special.gammaln(x)

    def setUp(self):
        self.fn = gamln
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestNdtri(TestCase, _TestOneArgFn):

    def ref(self, x):
        return special.ndtri(x)

    def setUp(self):
        self.fn = ndtri
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestBetaln(TestCase, _TestTwoArgFn):

    def ref(self, x, y):
        return special.betaln(x, y)

    def setUp(self):
        self.fn = betaln
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestGammainc(TestCase, _TestTwoArgFn):

    def ref(self, x, y):
        return special.gammainc(x, y)

    def setUp(self):
        self.fn = gammainc
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestPdtr(TestCase, _TestTwoArgFn):

    def ref(self, x, y):
        return special.pdtr(x, y)

    def test_fn(self):
        values = []
        exact_values = []
        for x in self.vals1:
            for y in self.vals2:
                values.append(self.fn(x, y))
                exact_values.append(self.refFn(x, y))
        np.testing.assert_almost_equal(values, exact_values)

    def setUp(self):
        self.fn = pdtr
        self.refFn = self.ref
        self.vals1 = [x for x in range(10)]
        self.vals2 = [x + 1 for x in range(10)]


class TestBdtr(TestCase, _TestThreeArgFn):

    def ref(self, x, y, z):
        return special.bdtr(x, y, z)

    def setUp(self):
        self.fn = bdtr
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(50)]


class TestBtdtr(TestCase, _TestThreeArgFn):

    def ref(self, x, y, z):
        return special.btdtr(x, y, z)

    def setUp(self):
        self.fn = btdtr
        self.refFn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(50)]
        self.vals.append(1.)
