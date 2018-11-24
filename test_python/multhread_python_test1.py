from concurrent.futures import ThreadPoolExecutor
import time
 
def return_after_5_secs(message,x):
    time.sleep(x)
    return message
 
def return_sucess():
	print(x)

 
future= []
 
pool = ThreadPoolExecutor(3)
 
future.append(pool.submit(return_after_5_secs, ("ID 1"),8))
future.append(pool.submit(return_after_5_secs, ("ID 2"),2))
future.append(pool.submit(return_after_5_secs, ("ID 3"),6))
future.append(pool.submit(return_after_5_secs, ("ID 4"),3))
future.append(pool.submit(return_after_5_secs, ("ID 5"),4))
future.append(pool.submit(return_after_5_secs, ("ID 6"),1))
future.append(pool.submit(return_after_5_secs, ("ID 7"),2))
future.append(pool.submit(return_after_5_secs, ("ID 8"),1))


runing = len(future)
results_order = []
print(time.localtime())

while runing > 0:
	runing = len(future)
	#print(runing)
	for r in future:
		if(r.done() == True):
			runing = runing - 1
			if (r.result() not in results_order):
				results_order.append(r.result())
				print("Terminou: ",r.done(), r.result())
				print(time.localtime())
	if (runing == 0):
		break
