import os,sys
# print sys.argv

def check_tab(_tab):
	#print _tab
        if _tab == 't':
                flag = '\t'
        elif _tab == 's':
                flag = '\s'
        else:
                flag = _tab
	return flag 

def check_pars(_pars):
	'_pars is list now'
	len_argv = len(_pars)
	if len_argv > 3 or len_argv == 1:
		raise Exception('header filename tab !!')
	else:
		if sys.argv[1] == '-':
			header = sys.stdin.readline()
		else:
			header = open(sys.argv[1]).readline()
		if len_argv == 2:
			t = 't'
		else:
			t = sys.argv[2]
	tab_flag = check_tab(t)
	return header,tab_flag

def header_print(_str,tab):
	for line,i in enumerate(_str.strip('\n').split('%s'%tab)):
		print '%d  %s'%(line+1,i)

if __name__ == '__main__':
	header_str,tab_flag_str = check_pars(sys.argv)
	header_print(header_str,tab_flag_str)	
