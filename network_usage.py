import psutil

def monitor_network_usage():
    net_io= psutil.net_io_counters()
    print(f"Bytes sent : {net_io.bytes_sent}")
    print(f"Byte received : {net_io.bytes_recv}")

monitor_network_usage()