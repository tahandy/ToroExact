#!/usr/bin/env python3
import exactRP

gamma  = 1.4
xbnds  = [0.0, 1.0]
nZones = 100

cases = {
	1: {"left":[1.0,      0.75,       1.0],   "right":[0.125,     0.0,      0.1],    "time":0.2,   "x0":0.3},
	2: {"left":[1.0,     -2.0,        0.4],   "right":[1.0,       2.0,      0.4],    "time":0.15,  "x0":0.5},
	3: {"left":[1.0,      0.0,     1000.0],   "right":[1.0,       0.0,      0.01],   "time":0.012, "x0":0.5},
	4: {"left":[5.99924, 19.5975,   460.894], "right":[5.99242,  -6.19633, 46.0950], "time":0.035, "x0":0.4},
	5: {"left":[1.0,    -19.59745, 1000.0],   "right":[1.0,     -19.59745,  0.01],   "time":0.012, "x0":0.8},
	6: {"left":[1.4,      0.0,        1.0],   "right":[1.0,       0.0,      1.0],    "time":2.0,   "x0":0.5},
	7: {"left":[1.4,      0.1,        1.0],   "right":[1.0,       0.1,      1.0],    "time":2.0,   "x0":0.5},
}

for icase in cases.keys():
	stateL = cases[icase]["left"]
	stateR = cases[icase]["right"]
	t      = cases[icase]["time"]
	x0     = cases[icase]["x0"]

	rp = exactRP.exactRP(gamma, stateL, stateR)
	rp.solve()

	dx = (xbnds[1]-xbnds[0])/nZones
	x  = []
	s  = []
	for i in range(0,nZones):
		x.append(xbnds[0] + (float(i)+0.5e0)*dx)
		if(abs(t) <= max(1.0e-9 * abs(t), 0.e0)):
			s.append(x[i]-x0)
		else:
			s.append((x[i]-x0)/t)

	dens, pres, velx = rp.sample(s)
	eint = []
	for i in range(0,nZones):
		eint.append((pres[i]/dens[i])/(gamma-1.e0))

	filename = "output/toro_{:1d}_exact.dat".format(icase)
	print(filename)
	with open(filename,'w+') as file:
		file.write("{:>15s} {:>15s} {:>15s} {:>15s} {:>15s}\n".format('x','dens','pres','velx','eint'))

		for i in range(0,nZones):
			file.write("{:15.10f} {:15.10f} {:15.10f} {:15.10f} {:15.10f}\n".format(x[i],dens[i],pres[i],velx[i],eint[i]))







