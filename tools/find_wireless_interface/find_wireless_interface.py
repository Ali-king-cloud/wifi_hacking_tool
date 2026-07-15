from __future__ import annotations

import subprocess


def find_windows_wireless_interface():
    """Find wireless interface data on Windows.

    Uses `netsh wlan show interfaces` and returns the subprocess result object.

    Returns:
        subprocess.CompletedProcess | None
    """

    try:
        # Run the Windows native netsh command to list WLAN interfaces
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result

    except subprocess.CalledProcessError:
        # Common when run on non-Windows or Wi-Fi service is unavailable
        return None
    except Exception:
        return None


def main() -> None:
    wifi_card = find_windows_wireless_interface()
    if wifi_card is not None:
        print("Connected Windows Wireless Interface data found.")
    else:
        print("No wireless interface detected or Wi-Fi is turned off.")


if __name__ == "__main__":
    main()

