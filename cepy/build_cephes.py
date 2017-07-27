# build_cephes.py - python script to build included cephes with CFFI
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
import os

import cffi


ffibuilder = cffi.FFI()

dirname = os.path.dirname(os.path.abspath(__file__))
sourcefile = os.path.join(dirname, 'cephes.h')
SOURCE_FILENAMES = [
    'acosh.c',
    'airy.c',
    'arcdot.c',
    'asin.c',
    'asinh.c',
    'atan.c',
    'atanh.c',
    'bdtr.c',
    'bernum.c',
    'beta.c',
    'btdtr.c',
    'cbrt.c',
    'chbevl.c',
    'chdtr.c',
    'clog.c',
    'cmplx.c',
    'const.c',
    'cosh.c',
    'cpmul.c',
    'dawsn.c',
    'drand.c',
    'ei.c',
    'eigens.c',
    'ellie.c',
    'ellik.c',
    'ellpe.c',
    'ellpj.c',
    'ellpk.c',
    'euclid.c',
    'exp.c',
    'exp10.c',
    'exp2.c',
    'expn.c',
    'expx2.c',
    'fabs.c',
    'fac.c',
    'fdtr.c',
    'fftr.c',
    'floor.c',
    'fresnl.c',
    'gamma.c',
    'gdtr.c',
    'gels.c',
    'hyp2f1.c',
    'hyperg.c',
    'i0.c',
    'i1.c',
    'igam.c',
    'igami.c',
    'incbet.c',
    'incbi.c',
    'isnan.c',
    'iv.c',
    'j0.c',
    'j1.c',
    'jn.c',
    'jv.c',
    'k0.c',
    'k1.c',
    'kn.c',
    'kolmogorov.c',
    'levnsn.c',
    'log.c',
    'log10.c',
    'log2.c',
    'lrand.c',
    'lsqrt.c',
    'minv.c',
    'mtherr.c',
    'mtransp.c',
    'nbdtr.c',
    'ndtr.c',
    'ndtri.c',
    'pdtr.c',
    'planck.c',
    'polevl.c',
    'polmisc.c',
    'polrt.c',
    'polylog.c',
    'polyr.c',
    'pow.c',
    'powi.c',
    'psi.c',
    'revers.c',
    'rgamma.c',
    'round.c',
    'shichi.c',
    'sici.c',
    'simpsn.c',
    'simq.c',
    'sin.c',
    'sincos.c',
    'sindg.c',
    'sinh.c',
    'spence.c',
    'sqrt.c',
    'stdtr.c',
    'struve.c',
    'tan.c',
    'tandg.c',
    'tanh.c',
    'unity.c',
    'yn.c',
    'zeta.c',
    'zetac.c',
    ]

SOURCES = [os.path.join(dirname, filename) for filename in SOURCE_FILENAMES]

with open(sourcefile) as f:
    ffibuilder.cdef(f.read())

ffibuilder.set_source(
    'cepy._cephes',
    '#include "{0}"'.format(sourcefile),
    sources=SOURCES,
    library_dirs=['.'])

ffibuilder.compile(verbose=True)
