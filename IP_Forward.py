#current IP forward status
sysctl net.ipv4.ip_forward


#disable IP forwarding
sysctl -w net.ipv4.ip_forward=0


#enable IP forwarding
sysctl -w ney.ipv4.forward=1
