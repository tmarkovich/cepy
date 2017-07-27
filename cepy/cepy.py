# cepy.py - Function indirection layer to link C to Python
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
from ._cephes.lib import airy
from ._cephes.lib import bdtrc
from ._cephes.lib import bdtr as _bdtr # redirected to allow argument handling
from ._cephes.lib import bdtri
from ._cephes.lib import beta
from ._cephes.lib import lbeta
from ._cephes.lib import btdtr
from ._cephes.lib import cbrt
from ._cephes.lib import chbevl
from ._cephes.lib import chdtrc
from ._cephes.lib import chdtr
from ._cephes.lib import chdtri
from ._cephes.lib import cpmul
from ._cephes.lib import dawsn
from ._cephes.lib import ei
from ._cephes.lib import ellie
from ._cephes.lib import ellik
from ._cephes.lib import ellpe
from ._cephes.lib import ellpj
from ._cephes.lib import ellpk
from ._cephes.lib import euclid
from ._cephes.lib import rdiv
from ._cephes.lib import rmul
from ._cephes.lib import rsub
from ._cephes.lib import radd
from ._cephes.lib import fdtrc
from ._cephes.lib import fdtr
from ._cephes.lib import fdtri
from ._cephes.lib import fresnl
from ._cephes.lib import gam
from ._cephes.lib import lgam
from ._cephes.lib import gdtr
from ._cephes.lib import gdtrc
from ._cephes.lib import gels
from ._cephes.lib import hyp2f1
from ._cephes.lib import hyperg
from ._cephes.lib import hyp2f0
from ._cephes.lib import i0
from ._cephes.lib import i0e
from ._cephes.lib import i1
from ._cephes.lib import i1e
from ._cephes.lib import igamc
from ._cephes.lib import igam
from ._cephes.lib import igami
from ._cephes.lib import incbet
from ._cephes.lib import incbi
from ._cephes.lib import iv
from ._cephes.lib import j0
from ._cephes.lib import y0
from ._cephes.lib import y1
from ._cephes.lib import j1
from ._cephes.lib import jn
from ._cephes.lib import jv
from ._cephes.lib import k0
from ._cephes.lib import k0e
from ._cephes.lib import k1
from ._cephes.lib import k1e
from ._cephes.lib import kn
from ._cephes.lib import smirnov
from ._cephes.lib import kolmogorov
from ._cephes.lib import smirnovi
from ._cephes.lib import kolmogi
from ._cephes.lib import levnsn
from ._cephes.lib import minv
from ._cephes.lib import nbdtrc
from ._cephes.lib import nbdtr
from ._cephes.lib import nbdtri
from ._cephes.lib import ndtr
from ._cephes.lib import erfc
from ._cephes.lib import ndtri as _ndtri # redirected to allow argument handling
from ._cephes.lib import pdtrc
from ._cephes.lib import pdtr
from ._cephes.lib import pdtri
from ._cephes.lib import plancki
from ._cephes.lib import planckc
from ._cephes.lib import planckd
from ._cephes.lib import planckw
from ._cephes.lib import p1evl
from ._cephes.lib import polatn
from ._cephes.lib import polsqt
from ._cephes.lib import polsin
from ._cephes.lib import polcos
from ._cephes.lib import polrt
from ._cephes.lib import polylog
from ._cephes.lib import polini
from ._cephes.lib import polprt
from ._cephes.lib import polclr
from ._cephes.lib import polmov
from ._cephes.lib import polmul
from ._cephes.lib import poladd
from ._cephes.lib import polsub
from ._cephes.lib import poldiv
from ._cephes.lib import polsbt
from ._cephes.lib import poleva
from ._cephes.lib import psi
from ._cephes.lib import revers
from ._cephes.lib import rgamma
from ._cephes.lib import shichi
from ._cephes.lib import sici
from ._cephes.lib import spence
from ._cephes.lib import stdtr
from ._cephes.lib import stdtri
from ._cephes.lib import onef2
from ._cephes.lib import threef0
from ._cephes.lib import struve
from ._cephes.lib import yv
from ._cephes.lib import yn
from ._cephes.lib import zeta
from ._cephes.lib import zetac

def betaln(a, b):
    """Returns log(Beta(a, b))

    This redirects the cephes lbeta to betaln to agree with the scipy naming
    convention.
    """
    return lbeta(a, b)


def bdtr(a, b, x):
    """Returns the binomial probability density

    This wraps the cephes function to enforce integer casting on the ``a`` and
    ``b`` arguments.
    """
    return _bdtr(int(a), int(b), x)


def gammainc(a, x):
    """Returns the incomplete gamma function

    This redirects the cephes provided igam to gammainc to agree with the scipy
    naming convention.
    """
    return igam(a, x)


def ndtri(x):
    """Returns the inverse of the Normal distribution function

    This wraps the cephes provided ndtri function to correctly catch the
    special cases for arguments.
    """
    if x <= 0.0:
        return -float('inf')
    elif x >= 1.0:
        return float('inf')
    else:
        return _ndtri(x)


def gamln(x):
    """Returns the log of the gamma function

    This redirects the cephes provided lgam function to gamln to agree with the
    scipy naming convention.
    """
    return lgam(x)
