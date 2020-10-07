import nmap3

def top_ports(mainip):
    nmap =nmap3.Nmap()
    results=nmap.scan_top_ports(mainip)
    print(results)

def os_identify(mainip):
    nmap=nmap3.Nmap()
    results=nmap.nmap_os_detection(mainip)
    print(results)

def DNS_Brute_force(mainip):
    nmap=nmap3.Nmap()
    results=nmap.nmap_dns_brute_script(mainip)
    print(results)

def fin_Scan(mainip):
    nmap=nmap3.NmapScanTechniques()
    results=nmap.nmap_fin_scan(mainip)
    print(results)

if __name__ == "__main__": 
    print("Enter the target IP for Nmap scan")
    main = input("IP Address:")
    print("Please select what do you want to perform :")
    print("1. Top Port scan \n 2. OS Identification \n 3. DNS_Brute_Force \n 4. fin Scan")
    option = int(input("Enter your choice here:"))
    if option == 1:
        top_ports(main)
    elif option == 2:
        os_identify(main)
    elif option == 3:
        DNS_Brute_force(main)
    elif option == 4:
        fin_Scan(main)
    else:
        print("Wrong option selected please re-run the program")
    

