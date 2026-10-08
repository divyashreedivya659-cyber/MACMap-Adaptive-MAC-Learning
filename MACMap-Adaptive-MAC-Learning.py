from datetime import datetime

mac_table = {}
last_seen = {}

TIMEOUT = 5


def get_time():
    while True:
        time_input = input("Enter time (HH:MM): ")

        try:
            return datetime.strptime(time_input, "%H:%M")
        except ValueError:
            print("Invalid time. Enter time like 13:22")


def add_device():
    mac = input("Enter MAC address: ")
    port = input("Enter switch port: ")
    current_time = get_time()

    if mac in mac_table:

        if mac_table[mac] != port:
            print("\nMAC movement detected!")
            print("Previous port:", mac_table[mac])
            print("New port:", port)

            mac_table[mac] = port

        else:
            print("\nMAC address is already connected to this port.")

    else:
        mac_table[mac] = port
        print("\nMAC address learned successfully!")

    last_seen[mac] = current_time


def send_frame():
    source_mac = input("Enter source MAC address: ")
    destination_mac = input("Enter destination MAC address: ")
    source_port = input("Enter source device port: ")
    current_time = get_time()

    if source_mac in mac_table:

        if mac_table[source_mac] != source_port:
            print("\nMAC movement detected!")
            print("Previous port:", mac_table[source_mac])
            print("New port:", source_port)

        mac_table[source_mac] = source_port

    else:
        mac_table[source_mac] = source_port

    last_seen[source_mac] = current_time

    if destination_mac in mac_table:
        print("\nDestination MAC found!")
        print("Frame forwarded to:", mac_table[destination_mac])

    else:
        print("\nUnknown destination MAC!")
        print("Frame is flooded to other ports.")


def show_mac_table():
    print("\nMAC Address Table")

    if len(mac_table) == 0:
        print("MAC table is empty.")

    else:
        for mac in mac_table:
            time = last_seen[mac].strftime("%H:%M")
            print(mac, "->", mac_table[mac], "Last seen:", time)


def check_stale_entries():
    current_time = get_time()
    found = False

    print("\nStale Entries")

    for mac in last_seen:

        difference = current_time - last_seen[mac]
        minutes = difference.total_seconds() / 60

        if minutes >= TIMEOUT:
            print("Stale MAC entry:", mac)
            print("Port:", mac_table[mac])
            print("Last seen:", last_seen[mac].strftime("%H:%M"))
            found = True

    if not found:
        print("No stale MAC entries found.")


def show_events():
    print("\nNetwork Events")

    if len(mac_table) == 0:
        print("No network events available.")

    else:
        for mac in mac_table:
            print(mac, "->", mac_table[mac])


while True:

    print("\nMACMap")
    print("1. Add / Learn Device")
    print("2. Send Ethernet Frame")
    print("3. Show MAC Address Table")
    print("4. Check Stale Entries")
    print("5. Show Network Events")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_device()

    elif choice == "2":
        send_frame()

    elif choice == "3":
        show_mac_table()

    elif choice == "4":
        check_stale_entries()

    elif choice == "5":
        show_events()

    elif choice == "6":
        print("MACMap program ended.")
        break

    else:
        print("Invalid choice.")