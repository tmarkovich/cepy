/* cephes.h - Cephes header for use with CFFI
 * Copyright 2017 Gamalon, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

typedef struct
    {
    double r;
    double i;
    } cmplx;

typedef struct{
    double n;
    double d;
    }fract;

// Method prototypes
double acosh(double x);
int airy(double x, double *ai, double *aip, double *bi, double *bip);
double asin(double x);
double acos(double x);
double asinh(double xx);
double atan(double x);
double atan2(double x, double y);
double atanh(double x);
double bdtrc(int k, int n, double p);
double bdtr(int k, int n, double p);
double bdtri(int k, int n, double p);
double beta(double a, double b);
double lbeta(double a, double b);
double btdtr(double a, double b, double x);
double cbrt(double x);
double chbevl(double x, double array[], int n);
double chdtrc(double df, double x);
double chdtr(double df, double x);
double chdtri(double df, double y);
void clog(cmplx *z, cmplx *w);
void cexp(cmplx *z, cmplx *w);
void csin(cmplx *z, cmplx *w);
void ccos(cmplx *z, cmplx *w);
void ctan(cmplx *z, cmplx *w);
void ccot(cmplx *z, cmplx *w);
void casin(cmplx *z, cmplx *w);
void cacos(cmplx *z, cmplx *w);
void catan(cmplx *z, cmplx *w);
void csinh(cmplx *z, cmplx *w);
void casinh(cmplx *z, cmplx *w);
void ccosh(cmplx *z, cmplx *w);
void cacosh(cmplx *z, cmplx *w);
void ctanh(cmplx *z, cmplx *w);
void catanh(cmplx *z, cmplx *w);
void cpow(cmplx *a, cmplx *z, cmplx *w);
double cosh(double x);
int cpmul(cmplx *a, int da, cmplx *b, int db, cmplx *c, int *dc);
double dawsn( double xx);
double ei(double x);
double ellie(double phi, double m);
double ellik(double phi, double m);
double ellpe(double x);
int ellpj(double u, double m, double *sn, double *cn, double *dn, double *ph);
double ellpk(double x);
double euclid( double *num, double *den);
void rdiv(fract *ff1, fract *ff2, fract *ff3);
void rmul(fract *ff1, fract *ff2, fract *ff3);
void rsub(fract *ff1, fract *ff2, fract *ff3);
void radd(fract *ff1, fract *ff2, fract *ff3);
double exp(double x);
double exp10(double x);
double exp2(double x);
double expn(int n, double x);
double expx2(double x, int sign);
double fabs(double x);
double fac(int i);
double fdtrc(int ia, int ib, double x);
double fdtr(int ia, int ib, double x);
double fdtri(int ia, int ib, double y);
double ceil(double x);
double floor(double x);
double frexp(double x, int *pw2);
double ldexp(double x, int pw2);
int fresnl(double xxa, double *ssa, double *cca);
double gam(double x);
double lgam(double x);
double gdtr(double a, double b, double x);
double gdtrc(double a, double b, double x);
int gels(double A[], double R[], int M, double EPS, double AUX[]);
double hyp2f1(double a, double b, double c, double x);
// double hyt2f1(double a, double b, double c, double x);
// double hys2f1(double a, double b, double c, double x);
double hyperg(double a, double b, double x);
double hyp2f0(double a, double b, double x, int type, double *err);
double i0(double x);
double i0e(double x);
double i1(double x);
double i1e(double x);
double igamc(double a, double x);
double igam(double a, double x);
double igami(double a, double y0);
double incbet(double aa, double bb, double xx);
double incbi(double aa, double bb, double yy0);
// int signbit(double x);
// int isnan(double x);
// int isfinite(double x);
double iv(double v, double x);
double j0(double x);
double y0(double x);
double y1(double x);
double j1(double x);
double jn(int n, double x);
double jv(double n, double x);
double k0(double x);
double k0e(double x);
double k1(double x);
double k1e(double x);
double kn(int nn, double x);
double smirnov(int n, double e);
double kolmogorov(double y);
double smirnovi(int n, double p);
double kolmogi(double p);
// void getnum(char *s, double *px);
int levnsn(int n, double r[], double a[], double e[], double refl[]);
double log(double x);
double log10(double x);
double log2(double x);
long lrand();
double lsqrt(double x);
int minv(double A[], double X[], int n, double B[], int IPS[]);
int mtherr(char *name, int code);
double nbdtrc(int k, int n, double p);
double nbdtr(int k, int n, double p);
double nbdtri(int k, int n, double p);
double ndtr(double a);
double erfc(double a);
double ndtri(double y0);
double pdtrc(int k, double m);
double pdtr(int k, double m);
double pdtri(int k, double y);
double plancki(double w, double T);
double planckc(double w, double T);
double planckd(double w, double T);
double planckw(double T);
double polevl(double x, double coef[], int N);
double p1evl(double x, double coef[], int N);
void polatn(double num[], double den[], double ans[], int nn);
void polsqt(double pol[], double ans[], int nn);
void polsin(double x[], double y[], int nn);
void polcos(double x[], double y[], int nn);
int polrt(double xcof[], double cof[], int m, cmplx root);
double polylog(int n, double x);
void polini(int maxdeg);
void polprt(fract a[], int na, int d);
void polclr(fract a[], int n);
void polmov(fract a[], int na, fract b[]);
void polmul(fract a[], int na, fract b[], int nb, fract c[]);
void poladd(fract a[], int na, fract b[], int nb, fract c[]);
void polsub(fract a[], int na, fract b[], int nb, fract c[]);
int poldiv(fract a[], int na, fract b[], int nb, fract c[]);
void polsbt(fract a[], int na, fract b[], int nb, fract c[]);
void poleva(fract a[], int na, fract *x, fract *s);
double pow(double x, double y);
double powi(double x, int nn);
double psi(double x);
double revers(double y[], double x[], int n);
double rgamma(double x);
double round(double x);
int shichi(double x, double *si, double *ci);
int sici(double x, double *si, double *ci);
double sin(double x);
double cos(double x);
double radian(double d, double m, double s);
// int sincos(double x, double *s, double *c, int flg);
double sindg(double x);
double cosdg(double x);
double sinh(double x);
double spence(double x);
double sqrt(double x);
double stdtr(int k, double t);
double stdtri(int k, double p);
double onef2(double a, double b, double c, double x, double *err);
double threef0(double a, double b, double c, double x, double *err);
double struve(double v, double x);
double yv(double v, double x);
double tan(double x);
double cot(double x);
// double tancot(double xx, int cotflag);
double tandg(double x);
double cotdg(double x);
double tanh(double x);
double log1p(double x);
double expm1(double x);
double cosm1(double x);
double yn(int n, double x);
double zeta(double x, double q);
double zetac(double x);
