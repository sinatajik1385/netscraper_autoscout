
import threading
import subprocess
import time
def do_stuff () :
    def run_script(script_name):
        subprocess.run(["python", script_name])

    if __name__ == "__main__":
        script1_thread = threading.Thread(target=run_script, args=("net_scraper_bmw.py",))
        script2_thread = threading.Thread(target=run_script, args=("net_scraper_mercedes.py",))
        script3_thread = threading.Thread(target=run_script, args=("net_scraper_volkswagen.py",))
        



        script1_thread.start()
        script2_thread.start()
        script3_thread.start()


        script1_thread.join()
        script2_thread.join()
        script3_thread.join()


        print("all scripts have finished executing.")
if __name__ == "__main__" :
    while True :
        do_stuff()
        time_wait = 30
        print (f'waiting {time_wait} minuts')
        time.sleep (time_wait *60)