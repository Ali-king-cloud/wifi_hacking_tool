"""
This script retrieves the SSID of the currently connected Wi-Fi network
on Windows and finds its saved password using the netsh utility.
It is designed to be simple, lean, and beginner-friendly.
"""

import subprocess

def get_current_wifi_ssid() -> str | None:
    """
    Retrieve the SSID (network name) of the currently connected Wi-Fi.
    
    Returns:
        The SSID as a string if connected, or None if not connected or on error.
    """
    try:
        # Run the Windows command to show current wireless interface status
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the command output line by line
        for line in result.stdout.splitlines():
            line = line.strip()
            # Look for the line containing "SSID" (but not "BSSID")
            if line.startswith("SSID") and ":" in line:
                # Split at the colon to get the SSID name
                parts = line.split(":", 1)
                ssid = parts[1].strip()
                return ssid
                
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Command failed to run or wasn't found (e.g., non-Windows system)
        pass
        
    return None

def get_wifi_password(ssid: str) -> str | None:
    """
    Retrieve the saved Wi-Fi password for a given SSID on Windows.
    
    Args:
        ssid: The SSID of the Wi-Fi network.
        
    Returns:
        The password string if found, or None if not found or on error.
    """
    try:
        # Run netsh to show profile details including the clear-text key.
        # We pass the argument 'name=SSID' directly without wrapping in double quotes,
        # as subprocess.run handles spaces in arguments automatically.
        result = subprocess.run(
            ["netsh", "wlan", "show", "profile", f"name={ssid}", "key=clear"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Parse the command output line by line
        for line in result.stdout.splitlines():
            line = line.strip()
            # Look for the line containing the key content (password)
            # In English Windows, this label is "Key Content"
            if "Key Content" in line and ":" in line:
                parts = line.split(":", 1)
                password = parts[1].strip()
                return password
                
    except subprocess.CalledProcessError:
        # Occurs if the profile doesn't exist or netsh command failed
        pass
        
    return None

def main() -> None:
    """Main execution function."""
    print("--- Wi-Fi Password Retriever ---")
    
    # Step 1: Find the SSID of the currently connected network
    ssid = get_current_wifi_ssid()
    
    if not ssid:
        print("Error: Could not retrieve the connected Wi-Fi SSID.")
        print("Please ensure your Wi-Fi is turned on and connected to a network.")
        return
        
    print(f"Connected SSID: {ssid}")
    
    # Step 2: Retrieve the password for the found SSID
    password = get_wifi_password(ssid)
    
    if password:
        print(f"Wi-Fi Password: {password}")
    else:
        print("Could not retrieve the password.")
        print("This network may not require a password, or the script lacks sufficient permissions.")

if __name__ == "__main__":
    main()
