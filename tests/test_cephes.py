# test_cephes.py - tests for special functions defined in CePy
# Copyright 2017 Gamalon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
        exact_values = [self.ref_fn(x) for x in self.vals]
        np.testing.assert_almost_equal(values, exact_values)


class _TestTwoArgFn(object):

    def test_fn(self):
        values = []
        exact_values = []
        for x in self.vals:
            for y in self.vals:
                values.append(self.fn(x, y))
                exact_values.append(self.ref_fn(x, y))
        np.testing.assert_almost_equal(values, exact_values)


class _TestThreeArgFn(object):

    def test_fn(self):
        values = []
        exact_values = []
        for x in self.vals:
            for y in self.vals:
                for z in self.vals:
                    values.append(self.fn(x, y, z))
                    exact_values.append(self.ref_fn(x, y, z))
        np.testing.assert_almost_equal(values, exact_values)


class TestGamln(TestCase, _TestOneArgFn):

    def ref(self, x):
        return special.gammaln(x)

    def setUp(self):
        self.fn = gamln
        self.ref_fn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestNdtri(TestCase, _TestOneArgFn):

    def ref(self, x):
        return special.ndtri(x)

    def setUp(self):
        self.fn = ndtri
        self.ref_fn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestBetaln(TestCase, _TestTwoArgFn):

    def ref(self, x, y):
        return special.betaln(x, y)

    def setUp(self):
        self.fn = betaln
        self.ref_fn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(100)]
        self.vals.append(1.)


class TestGammainc(TestCase, _TestTwoArgFn):

    def ref(self, x, y):
        return special.gammainc(x, y)

    def setUp(self):
        self.fn = gammainc
        self.ref_fn = self.ref
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
                exact_values.append(self.ref_fn(x, y))
        np.testing.assert_almost_equal(values, exact_values)

    def setUp(self):
        self.fn = pdtr
        self.ref_fn = self.ref
        self.vals1 = [x for x in range(10)]
        self.vals2 = [x + 1 for x in range(10)]


class TestBdtr(TestCase, _TestThreeArgFn):

    def ref(self, x, y, z):
        return special.bdtr(x, y, z)

    def setUp(self):
        self.fn = bdtr
        self.ref_fn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(50)]


class TestBtdtr(TestCase, _TestThreeArgFn):

    def ref(self, x, y, z):
        return special.btdtr(x, y, z)

    def setUp(self):
        self.fn = btdtr
        self.ref_fn = self.ref
        self.vals = [random.uniform(0., 1.0) for _ in range(50)]
        self.vals.append(1.)
