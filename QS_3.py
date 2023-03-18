r_p_adult=37550.0
r_p_children=r_p_adult/3
no_adult=int(input())
no_children=int(input())
no_passenger=no_adult+no_children
t_c_b_d=(no_adult*37550.0)+(r_p_children*no_children)
service_tax=((t_c_b_d*7)/100)
t_c_a_d=(t_c_b_d+service_tax)-((t_c_b_d+service_tax)/10)
print("Total Ticket Price:",t_c_a_d)
