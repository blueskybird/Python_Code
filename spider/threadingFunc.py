import threading
from time import ctime, sleep

def loop(nloop, nsec):
	print "start loop", nloop, "at:", ctime()
	sleep(nsec)
	print "stop loop", nloop, "at:", ctime()

loops = [2, 4]

def main():
	print "star at:", ctime()
	threads = []
	nloops = xrange(len(loops))
	
	for i in nloops:
		t = threading.Thread(target = loop, args = (i, loops[i]))
		threads.append(t)

	for i in nloops:
		threads[i].start()

	for i in nloops:
		threads[i].join()

	print "all DONE at:", ctime()


if __name__ == '__main__':
	main()