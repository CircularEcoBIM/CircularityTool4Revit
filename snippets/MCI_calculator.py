# Copyright (c) 2022 CircularEcoBIM, authors: Artur Tomczak <artomczak@gmail.com>, Ana Mestre <amestre@3drivers.pt >, Joana Fernandes <joanabfernandes@tecnico.ulisboa.pt>
# This file is part of CircularEcoBIM.


"""INPUTS"""
from operator import iadd


C_C, E_R, HHV, M_B, B_C, E_F, E_C, F_S, F_R, F_U, C_R, C_U  = IN[0]
# C_C, E_R, HHV, M_B, B_C, E_F, E_C, F_S, F_R, F_U, C_R, C_U  = [
# 	[0, 0, 0],
# 	[0, 0, 0],
# 	[0.203, 0.203, 0.203],
# 	[0.9666, 0.9666, 0.9666],
# 	[0.45, 0.45, 0.45],
# 	[0, 0, 0],
# 	[1, 1, 1],
# 	[1, 0, 0.12],
# 	[0, 0, 0],
# 	[0, 1, 0.88],
# 	[0, 0, 0],
# 	[0, 0, 0]
# 	]

M = IN[1]
# M = [2627, 2627, 3987]

"""CALCULATIONS"""

count = len(F_S)

# E_E - efficiency of the energy recovery process
# E_E = E_R/(HHV*M_B)
E_E = []
for i in range(count):
	try:
		E_E.append(E_R[i]/(HHV[i]*M_B[i]))
	except ZeroDivisionError:
		E_E.append(0)

# C_E - Fraction of mass of a product being collected for energy recovery where the material satisfies the requirements for inclusion
# C_E = E_E*B_C
C_E = [E_E*B_C for E_E,B_C in zip(E_E,B_C)]

# W_0 Waste from the linear flow Wj
# W_0 = M*(1-C_R-C_U-C_C-C_E)
W_0 = [M*(1-C_R-C_U-C_C-C_E) for M,C_R,C_U,C_C,C_E in zip(M,C_R,C_U,C_C,C_E)]

# W_F - Waste to produce any recycled content used as feedstock in the recycling process
# W_F = M*F_R*(1-E_F)/E_F
W_F = []
for i in range(count):
	try:
		W_F.append(M[i]*F_R[i]*(1-E_F[i])/E_F[i])
	except TypeError:
		W_F.append(i)
	except ZeroDivisionError:
		W_F.append(0)

# W_C - Waste generated in the  recycling process Wj
# W_C = M*(1-E_C)*C_R
W_C = [M*(1-E_C)*C_R for M,E_C,C_R in zip(M,E_C,C_R)]

# V_F - Amount of virgin material
#V_F = M*(1-F_R-F_U-F_S)
V_F = [M*(1-F_R-F_U-F_S) for M,F_R,F_U,F_S in zip(M,F_R,F_U,F_S)]

# W - Amount of unrecoverable waste
# W = W_0+(W_F+W_C)/2
W = [W_0+(W_F+W_C)/2 for W_0,W_F,W_C in zip(W_0,W_F,W_C)]

# LFI = Linear Flow Index
# LFI = (V_F+W)/(2*M)
LFI = [(V_F+W)/(2*M) for V_F,W,M in zip(V_F,W,M)]

# X - Product Utility
# X = (L_j/L_av_j)*(U_j/U_av_j)
# Assumption that the lifetime and utilisation values are exactly as per market average, hence X=1
L, L_av = 50, 50
U, U_av = 100, 100
X = (L/L_av)*(U/U_av)

# MCI - Material Circularity Indicator
# MCI = 1-(0.9/X*LFI)  but 0 <= MCI <= 1.0
MCI = [1-(0.9/X*LFIj) if X>0.9*LFIj else 0.0 for LFIj in LFI]
MCI = [mci if mci<=1.0 else 1.0 for mci in MCI]

"""RESULTS"""
OUT = E_E, C_E, W_0, W_F, W_C, V_F, W, LFI, X, MCI