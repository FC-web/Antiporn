import ctypes, sys ,os
wi_fi="WI-FI"
VPN_VPN_Client="VPN - VPN Client"
Ethernet="Ethernet"
Preferred_DNS="185.228.168.10"
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    try:
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {wi_fi} static {Preferred_DNS} primary" ')
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {VPN_VPN_Client} static {Preferred_DNS} primary" ')
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {Ethernet} static {Preferred_DNS} primary" ')

    except:
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {Ethernet} static {Preferred_DNS} primary" ')
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {wi_fi} static {Preferred_DNS} primary" ')
        os.system(f'cmd /k "Netsh interface ipv4 set dnsservers {VPN_VPN_Client} static {Preferred_DNS} primary" ')
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
