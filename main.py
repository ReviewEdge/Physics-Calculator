#inputs knowns
print("Enter knowns. Enter unknowns as .0")
v_i = float(input("Initial Velocity (m/s): "))
v_f = float(input("Final Velocity (m/s): "))
a = float(input("Acceleration (m/s^2): "))
t = float(input("Time (s): "))
d = float(input("Distance (d): "))



#finds final velocity
def find_v_f(v_i,a,t):
    return v_i + a * t

#finds initial velocity
def find_v_i(v_f,a,t):
    return v_f - (a * t)

#finds acceleration
def find_a(v_f,v_i,t):
    return (v_f - v_i) / t

#finds time
def find_t(v_f,v_i,a):
    return (v_f - v_i) / a

#finds v_i (with distance)
def find_v_i_with_d(a,t,d):
    return (-0.5*a*t*t+d) / t



#decides what function to run

#runs if doesn't have v_f, and fines v_i
if v_f == .0 and v_i != .0 and a != .0 and t != .0:
    print("Final Velocity: " + str(find_v_f(v_i, a, t)))
#runs if doensn't have v_i, and finds v_i
elif v_i == .0 and v_f != .0 and a != .0 and t != .0:
    print("Initial Velocity: " + str(find_v_i(v_f,a,t)))
#runs if doensn't have a, and finds a
elif a == .0 and v_f != .0 and v_i != .0 and t != .0:
    print("Acceleration: " + str(find_a(v_f,v_i,t)))
#runs if doensn't have t, and finds t
elif t == .0 and v_f != .0 and v_i != .0 and a != .0:
    t = find_t(v_f,v_i,a)
    if t >= 0:
        print("Time: " + str(t))
    else:
        print("Invalid Knowns (would result in negative time)")
        print("Time: " + str(t))
#runs if doesn't have v_i or v_f but has d, t, and a
elif v_f == .0 and v_i == .0 and t != .0 and a != .0 and d != .0:
    v_i = find_v_i_with_d(a,t,d)
    print("Initial Velocity: " + str(v_i))
    #now finds v_f
    v_f = find_v_f(v_i,a,t)
    print("Final Velocity: " + (str(v_f)))
else:
    print("invalid knowns")

#finds distance
if d == .0:
    d = (v_i * t) + 0.5*a*t*t
    print("Distance: " + str(d))
