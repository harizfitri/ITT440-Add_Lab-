from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.63.3',
    'username': 'harizfitri', 
    'password': 'harizfitri99', 
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
