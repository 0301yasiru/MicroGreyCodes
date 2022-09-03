from subprocess import check_output, STDOUT
from re import findall, search

command = 'netsh wlan show profile'
output = check_output(command, shell=True, stderr=STDOUT, timeout=3, universal_newlines=True).decode('utf-8')

wlan_profiles = findall(r'Profile\s*:\s*(.*\b)', output)
max_p_l = max(map(lambda profile : len(profile), wlan_profiles))

passwords = []
for profile in wlan_profiles:
    try:
        command = "netsh wlan show profile \"{}\" key = clear".format(profile)
        output = check_output(command, shell=True, stderr=STDOUT, timeout=3, universal_newlines=True).decode('utf-8')
        password = search(r'Key\sContent\s+:\s+(.*)\b', output).group(1)
        passwords.append(password)
    except AttributeError:
        passwords.append('#OPEN??')

max_pw_l = max(map(lambda profile : len(profile), passwords))
wlan_profiles = list(zip(wlan_profiles, passwords))

with open('result.txt', 'w') as results:
    results.write('+' + '-'*(max_p_l+2) + '+' + '-'*(max_pw_l+2) + '+\n')
    results.write("| {0:^{2}} | {1:^{3}} |\n".format('PROFILE', 'PASSWORD', max_p_l, max_pw_l))
    results.write('+' + '-'*(max_p_l+2) + '+' + '-'*(max_pw_l+2) + '+\n')
    for couple in wlan_profiles:
        results.write("| {0:<{2}} | {1:<{3}} |\n".format(couple[0], couple[1], max_p_l, max_pw_l))
    results.write('+' + '-'*(max_p_l+2) + '+' + '-'*(max_pw_l+2) + '+\n')
