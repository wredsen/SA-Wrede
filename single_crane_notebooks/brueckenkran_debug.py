import sympy as sp
import pickle
import copyreg
from sympy import sin, cos, tan, pi, Matrix, Q
from sympy.interactive import printing
import scipy as sc
import scipy.optimize

import symbtools as st
import symbtools.modeltools as mt
from symbtools.modeltools import Rz
import symbtools.noncommutativetools as nct

import pycartan as pc

printing.init_printing(1)

data = st.pickle_full_load("brueckenkran.pcl")

vec_x = st.symb_vector('x1:7', commutative=False)
vec_xdot = st.time_deriv(vec_x, vec_x)
st.make_global(vec_x)
st.make_global(vec_xdot)

basis_vec = st.row_stack(vec_x[:3,:], vec_xdot[:3,:], st.time_deriv(vec_xdot[:3,:],vec_xdot[:3,:])) ##:

s = sp.Symbol('s', commutative=False)

M1 = sp.Matrix([[1, 0], [-s, 1]])

H = data.H ##:
H_ = st.col_stack(H, sp.zeros(2,3))
Hdx = pc.VectorDifferentialForm(1, basis_vec, coeff=H_)
Hdx.coeff

H1dx = Hdx.left_mul_by(M1,s=s)
H1dx.coeff