# Mistgpu-auto-check-machine-script

# DO NOT ABUSE IT TO BRING TROUBLES TO MISTGPU OWNER

## How to use it
1. modify run.sh with your setting
- username: your username of the site(eg: tfoel3)
- password: your password of the site(eg: abcde123)
- machine_id: the id of machine you want to check(eg. 000034)
2. type bash run.sh in your terminal
3. the script will check mistgpu for every 30 seconds
4. the script will send wechat message to your file helper of your wechat account when the machine is available

## requirement
- wxpy
- BeautifulSoup
- requests

