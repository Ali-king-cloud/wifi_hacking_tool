import subprocess

commands = {
    "all_details": ["ipconfig", "all"],
    "only_mac": ["getmac", "/v"]
}
my_input = input("Enter your number \n 1 for the all details related to mac \n 2 for the only mac: ")
try:
    if my_input == "1":
        details = subprocess.run(commands["all_details"],
                                 capture_output=True,
                                 text=True,
                                 check=True)
        print(details.stdout)
    elif my_input == "2":
        details = subprocess.run(commands["only_mac"],
                                 capture_output=True,
                                 text=True,
                                 check=True)
        print(details.stdout)
    else:
        print("be resonable bro")
except Exception as e:
    print(f"bhai koi serious error agya hai : {e}")

