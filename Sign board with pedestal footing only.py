## inputs
##--------
h1 = 4 # ft (total padestal height)
h2 = 3.5 # ft (padestal height below FGL)
h3 = 9 # ft (height of sign board above NGL upto center of wind load)
c = 18 # inch (padestal width and depth, assumed square padestal)
A = 4 # sft (wind catchment area of sign board)
P = 32 # psf (wind pressure)

## assumptions
##------------
gamma = 120 # pcf (unit wt of soil)
gamma_conc = 150 # pcf (unit wt of concrete)
ka = 0.34 # active lateral pressure coefficient
kp = 3.0 # passive lateral pressure coefficient


## processing
##-----------
# unit consistency
c /= 12 # convert to ft

# overturning moment
otm1 = (P*A) * (h3 + h2)
otm2 = ((ka*gamma*(h2**2.0)*c)/2) * (h2/3)
otm = otm1 + otm2

# balancing moment
bm1 = (c*c*h1*gamma_conc) * (c/2)
bm2 = ((kp*gamma*(h2**2.0)*c)/2) * (h2/3)
bm = bm1 + bm2

fos = bm / otm # factor of safety

## output
##-------
print("Overturning moment due to wind force:", otm1,"kip-ft")
print("Overturning moment due to active soil pressure:", otm2, "kip-ft")
print("Total Overturning moment:", otm, "kip-ft")
print("\nBalancing moment due to weight of padestal:", bm1, "kip-ft")
print("Balancing moment due to passive pressure of soil:", bm2, "kip-ft")
print("Total Balancing moment:", bm, "kip-ft")
print("\nFactor of safety:", fos)