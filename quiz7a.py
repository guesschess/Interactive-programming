# quiz 7a

# question 7
vel = 0
accelerate = 10

i = 0
for i in range(0,100000):
    vel += accelerate
    vel *= (1 - 0.1)
    i += 1
    
print vel
