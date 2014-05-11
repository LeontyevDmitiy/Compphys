import math
N=2      #NUMBER OF PLANETS
G=1.
M=1.
class Planet:
    def __init__(self,m,x,y,vx,vy):
        self.mass=m
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
    def __repr__(self):
        return "|_|   M=%s, R=(%s,%s), V=(%s,%s)" % (self.mass, self.x, self.y, self.vx, self.vy)         

class Spacetime:
    def __init__(self):
        self.Planets=[]
        
    def add(self,Pl):
        self.Planets.append(Pl)
        return self
    def __repr__(self):
        return "%s" % (self.Planets)
    def timestep(self,dt):
        for i in range(N):
            xi=self.Planets[i].x[-1]
            yi=self.Planets[i].y[-1]
            vxi=self.Planets[i].vx[-1]
            vyi=self.Planets[i].vy[-1]
            x1=xi+vxi*dt
            y1=yi+vyi*dt
            vx1=self.Planets[i].vx[-1]
            vy1=self.Planets[i].vy[-1]
            for j in range(N):
                xj=self.Planets[j].x[-1]
                yj=self.Planets[j].y[-1]
                Sx=0.
                Sy=0.
                Rij=math.sqrt((xj-xi)**2+(yj-yi)**2)
                Mj=self.Planets[j].mass
                if Rij!=0:
                    Sx=+G*Mj*(xj-xi)/Rij**3*dt
                    Sy=+G*Mj*(yj-yi)/Rij**3*dt
                vx1=vx1+Sx
                vy1=vy1+Sy
            self.Planets[i].x.append(x1)
            self.Planets[i].y.append(y1)
            self.Planets[i].vx.append(vx1)
            self.Planets[i].vy.append(vy1)
        return self


#________________________________________

Pl=[]
U=Spacetime()

            #mass,X,Y,Vx,Vy
U.add(Planet(1.,[-1.],[1.],[0.],[0.5]))
#U.add(Planet(1.,[0.],[0.85],[0.],[0.]))
U.add(Planet(1.,[+1.],[0.],[0.],[0.]))
#U.add(Planet(i*100+1.,[1.],[i+0.],[i+0.],[i+2.]))
#U.add(Planet(i*100+1.,[1.],[i+0.],[i+0.],[i+2.]))

print U
dt=0.1
Nt=50
X=[]
Y=[]
for i in range(N):
    X.append([])
    Y.append([])
    
for ti in range(Nt):
    U.timestep(dt)
    for i in range(N):
        X[i].append(U.Planets[i].x[-1])
        Y[i].append(U.Planets[i].y[-1])       
from matplotlib.pyplot import *
import numpy as np

s1 = X[0]
s2 = Y[0]

figure(1)
subplot(211)
plot(X[0],Y[0],'ro')
plot(X[1],Y[1], 'gs')
savefig('fig1')

show()
