## inputs
##--------
h1 = 2.3*3.281 # ft (total padestal height)
h2 = 2.2*3.281 # ft (padestal height below FGL)
h3 = 12*3.281 # ft (height of light pole above NGL)
dia = 6.5 # inch (outer dia of pole)
c = 24 # inch (padestal width and depth, assumed square padestal)
P = 21.2 # psf (wind pressure)

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
dia /= 12

# surface area of pole for wind catchment
A = dia*h3 # sft

# overturning moment
otm1 = (P*A) * (h3/2 + h1) # lb-ft
otm2 = ((ka*gamma*(h2**2.0)*c)/2) * (h2/3) # lb-ft
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
