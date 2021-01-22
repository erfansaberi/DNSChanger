def main():
    import os
    import ctypes
    import sys

    # This checks the administrator privilages
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print('dnsc command must be runned with administrator privilages')
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    # You can change your network name here
    network_name = 'Ethernet'

    # And also you can change your providers here
    providers_list = {'0': {'name': 'Auto Select', 'primary': 'DHCP', 'secondary': ''},
                    '1': {'name': 'Google', 'primary': '8.8.8.8', 'secondary': '8.8.4.4'},
                    '2': {'name': 'Shecan', 'primary': '178.22.122.100', 'secondary': '185.51.200.2'},
                    '3': {'name': 'Cloudflare', 'primary': '1.1.1.1', 'secondary': '1.0.0.1'},
                    '4': {'name': 'OpenDNS', 'primary': '208.67.222.222', 'secondary': '208.67.220.220'}
                    }

    print('*Your current DNS configurations:')
    current = os.popen('netsh interface ip show dns').read()
    print(current)

    print('*DNS providers list\n')
    for provider in providers_list:
        print(f'{provider}-{providers_list[provider]["name"]}\t{providers_list[provider]["primary"]}    {providers_list[provider]["secondary"]}')
    print('\n')

    provider_code = input('*Insert provider code (Network={}): '.format(network_name))

    if int(provider_code) > 0:
        print('\n')
        print(f'You selected {providers_list[provider_code]["name"]}')
        print(f'Primary: {providers_list[provider_code]["primary"]}')
        print(f'Secondary: {providers_list[provider_code]["secondary"]}')
        print('\n')

        # And now magic happens...
        os.system(f'netsh interface ip set dns name="{network_name}" static addr={providers_list[provider_code]["primary"]}')
        os.system(f'netsh interface ip add dns name="{network_name}" addr={providers_list[provider_code]["secondary"]} index=2')

    elif int(provider_code) == 0: #Set to auto select
        print('\nYou selected Auto select (get dns from dhcp)')
        os.system('netsh interface ipv4 set dnsservers name="{}" source=dhcp'.format(
            network_name))

    print('DNS changed')

main()