'''
eand package (Easy Algebraic Numerical Differentiation)
Copyright (C) 2013 Tu-Hoa Pham

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import numpy as np
from math import tanh, exp, cos, sin, pi, cosh, sqrt
import matplotlib.pyplot as plt
from eand.kmand.monodiffrep import MonoDiffRep

'''
Demonstration for derivative estimation through repeated (kappa,mu)-algebraic numerical differentiation
See 'Numerical differentiation with annihilators in noisy environments' (Mboup et al., 2009)
'''

# Observation parameters
T0 = 0.;                        # initial observation time
T1 = 5.;                        # final observation time
Ts = 1./200.;                   # sampling period
SNR = 25.;                      # signal to noise ratio
t = np.arange(T0,T1+Ts,Ts);     # observation time
Ns = len(t);                    # total number of samples

# Noise-free signal
x = np.array([0.]*Ns)
xp = np.array([0.]*Ns)
xpp = np.array([0.]*Ns)
for i in range(Ns):
    x[i] = tanh(t[i]-1.) + exp(-t[i]/1.2)*sin(6.*t[i]+pi)
    xp[i] = -6.*exp(-5./6.*t[i])*cos(6.*t[i]) + 1./(cosh(1.-t[i])**2.) + 5./6.*exp(-5./6.*t[i])*sin(6.*t[i]);
    xpp[i] = 10.*exp(-5.*t[i]/6.)*cos(6.*t[i]) + 1271./36.*exp(-5.*t[i]/6.)*sin(6.*t[i]) + 2.*(1./cosh(1.-t[i])**2.)*tanh(1.-t[i]);
signalRefSeq = [x,xp,xpp]

# Noisy signal
noise_mean = 0;
noise_var = (1./(10.**(SNR/10.)-1.))*(1./Ns)*sum(x**2.);
noise_sd = sqrt(noise_var);
noise = np.random.normal(noise_mean,noise_sd,Ns)
signalNoisy = signalRefSeq[0] + noise

# Numerical differentiation parameters
monoDiffRepCfg = {'nTarget': 2,                   # derivative order to estimate
                  'qVec': [0,0,0],                # model complexity parameters
                  'kappaVec': [0,0,0],            # differentiator parameters
                  'muVec': [0,0,0],               # differentiator parameters
                  'MVec': [60,60,60],             # estimation samples
                  'Ts': Ts,
                  'xi': 0.5,                      # xi parameter for real lambda
                  'lambdaOptType': 'noisyenv',    # 'mismodel' or 'noisyenv'
                  'causality': 'causal',          # 'causal' or 'anticausal'
                  'flagCompleteTime': 'none',     # complete tPost into t: 'none', 'zero', 'findiff'
                  'rediffSeq': [-1,-1,1]}         # estimates order to use for redifferentiation

# Construction of the (kappa,mu)-algebraic numerical differentiator
monoDiffRep = MonoDiffRep(monoDiffRepCfg)

# Differentiation of the noisy signal
(tPostSeq,dPostSeq) = monoDiffRep.differentiate(t,signalNoisy)

# Plot initial noisy signal
plt.figure(-1)
plt.plot(t, signalRefSeq[0], 'b', label='reference')
plt.plot(t, signalNoisy, 'r', label='noisy signal')
plt.grid()
plt.axhline(color='k')
plt.axvline(color='k')
plt.legend()
plt.title('Initial noisy signal')

# Plot successive derivative estimates
for n in range(monoDiffRepCfg['nTarget']+1):
    plt.figure(n)
    plt.plot(t, signalRefSeq[n], 'b', label='reference')
    plt.plot(tPostSeq[n], dPostSeq[n], 'r', label='estimate')
    plt.grid()
    plt.axhline(color='k')
    plt.axvline(color='k')
    plt.legend()
    plt.title('Order %d derivative estimate' % (n))
plt.show()
