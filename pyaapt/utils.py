import subprocess, os, io

def popen3(cmd):
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE,
	                stderr=subprocess.PIPE, bufsize=-1)


	stdin = os._wrap_close(io.TextIOWrapper(proc.stdin), proc)
	stdout = os._wrap_close(io.TextIOWrapper(proc.stdout), proc)
	stderr = os._wrap_close(io.TextIOWrapper(proc.stderr), proc)

	return stdin, stdout, stderr, proc