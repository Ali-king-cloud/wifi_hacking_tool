from __future__ import annotations
import importlib.util
from pathlib import Path

PACKAGE_DIR = Path(__file__).resolve().parent


def _load_local_module(module_name: str, file_name: str):
    module_path = PACKAGE_DIR / file_name
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module {module_name} from {module_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


find_windows_wireless_interface = _load_local_module(
    "find_windows_wireless_interface", "find_wireless_interface.py"
).find_windows_wireless_interface


def wifi_storage(result) -> dict:
    """Parse `netsh wlan show interfaces` output into a dictionary."""
    wifi_details: dict[str, str] = {}

    if result is None:
        return wifi_details

    stdout = getattr(result, "stdout", "")
    for line in stdout.splitlines():
        line = line.strip()
        if not line or line.startswith("There is") or line.startswith("---"):
            continue
#ab yaha aik dictionary ki trick use krte hai :
# wo ye kai loop to chal rhi a hia data ko store krne kai liye aur agar line mai ":" h to
# wo key aur value ko split krke dictionary mai store kr dega or jo hum ne 1 likha hai wo ye ensure krta hai kai agar line mai multiple ":" h to wo sirf pehli ":" ko split krke key aur value mai divide kare ga
        if ":" in line:
            key, value = line.split(":", 1)
            wifi_details[key.strip()] = value.strip()


    return wifi_details


def main() -> None:
    result = find_windows_wireless_interface()
    clean_results = wifi_storage(result)

    print("--- TARGETED DICTIONARY ACCESS ---")
    if clean_results:
        print(f"Signal Quality : {clean_results.get('Signal')}")
        print(f"Interface Name : {clean_results.get('Name')}")
        print(f"Connected SSID : {clean_results.get('SSID')}")
        print(f"description    : {clean_results.get('Description')}")
        print(f"Physical Addr  : {clean_results.get('Physical address')}")
        print(f"Interface Type : {clean_results.get('Interface type')}")
        print(f"State          : {clean_results.get('State')}")
        print(f"GUID           : {clean_results.get('GUID')}")
        print(f"BSSID          : {clean_results.get('BSSID')}")
        print(f"SSID           : {clean_results.get('SSID')}")
        print(f"Network State  : {clean_results.get('State')}")
        print(f"Radio Type     : {clean_results.get('Radio type')}")
        print(f"Authentication : {clean_results.get('Authentication')}")
        print(f"Cipher         : {clean_results.get('Cipher')}")
        print(f"Channel        : {clean_results.get('Channel')}")
        print(f"Receive Rate   : {clean_results.get('Receive rate (Mbps)')}")
        print(f"Transmit Rate  : {clean_results.get('Transmit rate (Mbps)')}")
        print(f"Profile        : {clean_results.get('Profile')}")


    else:
        print("No active Wi-Fi data to clean.")


if __name__ == "__main__":
    main()

