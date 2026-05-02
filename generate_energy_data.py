import random
from datetime import datetime, timedelta

def generate_energy_data(start_date_str="2026-01-01"):
    #แปลง string -> datetime
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.today()

    data = []
    current = start_date
    

    while current <= today:
        usage = random.randint(80, 220) #kWh ต่อวัน random data (simulate data)
        status = "high" if usage > 180 else "normal"

        data.append({ # datastructure
            "date": current.strftime("%Y-%m-%d"),
            "usage": usage,
            "status": status
        })

        current += timedelta(days=1) # loop เวลา เดินวันละ 1วัน

    return data
#ทดสอบ run
if __name__ == "__main__":
    energy_data = generate_energy_data()

    # แสดง 5 แถวแรก
    for item in energy_data[:5]:
        print(item)

    print("Total days: ", len(energy_data))