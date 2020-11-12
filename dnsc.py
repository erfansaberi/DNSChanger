import os, ctypes, sys

#This checks the administrator privilages
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

#You can change your network name here
network_name = 'Ethernet'

#And also you can change your providers here
providers_list = {'1': {'name':'Google','primary':'8.8.8.8','secondary':'8.8.4.4'},
                  '2': {'name':'Shecan','primary':'178.22.122.100','secondary':'185.51.200.2'},
                  '3': {'name':'Cloudflare','primary':'1.1.1.1','secondary':'1.0.0.1'},
                  '4': {'name':'OpenDNS','primary':'208.67.222.222','secondary':'208.67.220.220'}
                  }


print('DNS providers list\n')
for provider in providers_list:
    print('{}-{}'.format(provider, providers_list[provider]['name']))
print('\n')

provider_code = input('Insert provider code: ')

print('\n')
print('You selected {}'.format(providers_list[provider_code]['name']))
print('Primary: {}'.format(providers_list[provider_code]['primary']))
print('Secondary: {}'.format(providers_list[provider_code]['secondary']))
print('\n')

#And now magic happens...
os.system('netsh interface ip add dns name="{}" addr={} index=1'.format(network_name,providers_list[provider_code]['primary']))
os.system('netsh interface ip add dns name="{}" addr={} index=2'.format(network_name,providers_list[provider_code]['secondary']))

print('DNS changed! (press enter to exit)')
input()