import datetime
import time
from playsound import playsound

def get_alarm_time():
    while True:
        alarm_time = input("Enter alarm time in HH:MM:SS (24-hour format): ")
        try:
            # Validate format
            alarm_time_obj = datetime.datetime.strptime(alarm_time, "%H:%M:%S").time()
            return alarm_time_obj
        except ValueError:
            print("Invalid format. Please try again.")

def main():
    print("=== Simple Alarm Clock ===")
    alarm_time = get_alarm_time()
    print(f"Alarm set for {alarm_time}")

    while True:
        now = datetime.datetime.now().time()
        if now >= alarm_time:
            print("Wake up! Alarm ringing!")
            try:
                # Play sound if available
                playsound('alarm.mp3')
            except:
                print("Unable to play sound. Make sure 'alarm.mp3' is in the same directory.")
            break
        time.sleep(1)  # Wait for 1 second before checking again

if __name__ == "__main__":
    main()
