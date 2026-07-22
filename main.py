import subprocess as sp

dictionary = {
    "SSID": ["netsh","wlan","show","interfaces"]}
result =  sp.run(
    [SSID for SSID in dictionary["SSID"]],
    capture_output=True,
    text=True,
    check=True
    )
print(result.stdout)
