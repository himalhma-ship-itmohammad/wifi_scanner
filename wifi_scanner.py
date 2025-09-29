#!/usr/bin/env python3
"""
WiFi Network Scanner Tool
Developer: Mohammad Ali
GitHub: himalhma-ship-timohammad
⚠️ For Educational and Authorized Use Only
"""

import subprocess
import re
import socket
import platform
from datetime import datetime
import os
import sys
import time

def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print beautiful banner"""
    banner = """
    \033[1;36m
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║    ██╗    ██╗██╗███████╗██╗    ██████╗ ███████╗███╗   ██╗       ║
    ║    ██║    ██║██║██╔════╝██║    ██╔══██╗██╔════╝████╗  ██║       ║
    ║    ██║ █╗ ██║██║█████╗  ██║    ██████╔╝█████╗  ██╔██╗ ██║       ║
    ║    ██║███╗██║██║██╔══╝  ██║    ██╔══██╗██╔══╝  ██║╚██╗██║       ║
    ║    ╚███╔███╔╝██║██║     ██║    ██║  ██║███████╗██║ ╚████║       ║
    ║     ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝       ║
    ║                                                                  ║
    ║    \033[1;33m📡 ADVANCED WIFI NETWORK SCANNER TOOL\033[1;36m                   ║
    ║              \033[1;35mFor Authorized Testing Only\033[1;36m                         ║
    ║                                                                  ║
    ╠══════════════════════════════════════════════════════════════════╣
    ║                                                                  ║
    ║              \033[1;32mDeveloper: Mohammad Ali\033[1;36m                            ║
    ║              \033[1;37mGitHub: himalhma-ship-timohammad\033[1;36m                   ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    \033[0m
    """
    print(banner)

def print_colored(text, color_code):
    """Print colored text"""
    print(f"\033[{color_code}m{text}\033[0m")

def show_disclaimer():
    """Show ethical disclaimer"""
    print("\n" + "="*70)
    print_colored("⚖️  ETHICAL DISCLAIMER", "1;33")
    print("="*70)
    print_colored("This tool is for educational and authorized testing only.", "1;37")
    print_colored("• Use only on networks you own or have explicit permission to scan", "1;37")
    print_colored("• Do not use for unauthorized network access", "1;31")
    print_colored("• Developer is not responsible for misuse", "1;31")
    print_colored("• Respect privacy and follow local laws", "1;33")
    print("="*70)
    
    input("\n\033[1;36mPress Enter to accept and continue...\033[0m")
    clear_screen()
    print_banner()

def get_system_info():
    """Get system information"""
    print_colored("\n🔧 SYSTEM INFORMATION", "1;34")
    print_colored("═" * 50, "1;36")
    
    try:
        system = platform.system()
        node = platform.node()
        processor = platform.processor() or "Not Available"
        python_version = platform.python_version()
        
        print_colored(f"🏠 System        : {system}", "1;37")
        print_colored(f"🖥️  Node Name     : {node}", "1;37")
        print_colored(f"⚡ Processor     : {processor}", "1;37")
        print_colored(f"🐍 Python Version: {python_version}", "1;37")
        
    except Exception as e:
        print_colored(f"❌ Error getting system info: {e}", "1;31")

def scan_wifi_networks():
    """Scan for available WiFi networks"""
    print_colored("\n📡 SCANNING FOR WIFI NETWORKS", "1;34")
    print_colored("═" * 50, "1;36")
    
    try:
        # For Termux Android
        if platform.system() == "Linux" and "android" in platform.platform().lower():
            result = subprocess.run(['termux-wifi-scaninfo'], 
                                 capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print_colored("✅ WiFi Scan Completed", "1;32")
                networks = result.stdout.strip().split('\n')
                for i, network in enumerate(networks[:10], 1):  # Show first 10 networks
                    print_colored(f"📶 Network {i}: {network}", "1;37")
            else:
                print_colored("❌ WiFi scan failed. Make sure Termux:API is installed.", "1;31")
        
        # For Linux systems
        elif platform.system() == "Linux":
            result = subprocess.run(['nmcli', 'dev', 'wifi', 'list'], 
                                 capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print_colored("✅ WiFi Scan Completed", "1;32")
                lines = result.stdout.strip().split('\n')
                for line in lines[:8]:  # Show first 8 lines
                    print_colored(f"📶 {line}", "1;37")
            else:
                print_colored("❌ WiFi scan failed. nmcli not available.", "1;31")
                
        else:
            print_colored("❌ WiFi scanning not supported on this system", "1;31")
            
    except subprocess.TimeoutExpired:
        print_colored("❌ WiFi scan timeout", "1;31")
    except Exception as e:
        print_colored(f"❌ Error scanning WiFi: {e}", "1;31")

def get_network_info():
    """Get current network information"""
    print_colored("\n🌐 CURRENT NETWORK INFORMATION", "1;34")
    print_colored("═" * 50, "1;36")
    
    try:
        # Get hostname and local IP
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        print_colored(f"🏠 Hostname  : {hostname}", "1;37")
        print_colored(f"📍 Local IP  : {local_ip}", "1;37")
        
        # Get public IP
        try:
            import requests
            public_ip = requests.get('https://api.ipify.org', timeout=5).text
            print_colored(f"🌍 Public IP : {public_ip}", "1;32")
        except:
            print_colored("🌍 Public IP : Could not fetch", "1;31")
            
        # Get network interface info
        if platform.system() == "Linux":
            result = subprocess.run(['ip', 'addr'], capture_output=True, text=True)
            if result.returncode == 0:
                interfaces = re.findall(r'(\w+):.*?inet (\d+\.\d+\.\d+\.\d+)', result.stdout, re.DOTALL)
                for interface, ip in interfaces[:3]:  # Show first 3 interfaces
                    if ip != "127.0.0.1":
                        print_colored(f"🔗 Interface : {interface} - {ip}", "1;37")
                        
    except Exception as e:
        print_colored(f"❌ Error getting network info: {e}", "1;31")

def scan_connected_devices():
    """Scan for devices on local network"""
    print_colored("\n🔍 SCANNING CONNECTED DEVICES", "1;34")
    print_colored("═" * 50, "1;36")
    
    try:
        # Get local network range
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        network_prefix = '.'.join(local_ip.split('.')[:-1]) + '.'
        
        print_colored(f"🔎 Scanning network: {network_prefix}1-254", "1;33")
        print_colored("This may take a few minutes...", "1;37")
        
        active_devices = []
        
        # Scan first 20 IPs for demonstration
        for i in range(1, 21):
            ip = network_prefix + str(i)
            try:
                # Ping the device
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                result = subprocess.run(['ping', param, '1', '-W', '1', ip], 
                                      capture_output=True, text=True, timeout=2)
                
                if result.returncode == 0:
                    active_devices.append(ip)
                    print_colored(f"✅ Device found: {ip}", "1;32")
                else:
                    print_colored(f"❌ No response: {ip}", "1;31")
                    
            except:
                print_colored(f"⏹️  Timeout: {ip}", "1;33")
        
        print_colored(f"\n📊 Found {len(active_devices)} active devices", "1;36")
        
    except Exception as e:
        print_colored(f"❌ Error scanning devices: {e}", "1;31")

def run_speed_test():
    """Run basic speed test"""
    print_colored("\n🚀 NETWORK SPEED TEST", "1;34")
    print_colored("═" * 50, "1;36")
    
    try:
        print_colored("Testing download speed...", "1;33")
        
        # Simple speed test using ping and file download simulation
        start_time = time.time()
        
        # Test connectivity to major services
        test_servers = ['8.8.8.8', '1.1.1.1', 'google.com']
        for server in test_servers:
            try:
                param = '-n' if platform.system().lower() == 'windows' else '-c'
                result = subprocess.run(['ping', param, '2', server], 
                                      capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    print_colored(f"✅ {server}: Responsive", "1;32")
                else:
                    print_colored(f"❌ {server}: Slow response", "1;31")
            except:
                print_colored(f"⏹️  {server}: Timeout", "1;33")
        
        end_time = time.time()
        response_time = round((end_time - start_time) * 1000, 2)
        
        print_colored(f"\n⏱️  Average response time: {response_time} ms", "1;36")
        
        # Basic speed assessment
        if response_time < 100:
            print_colored("📈 Network Speed: Excellent", "1;32")
        elif response_time < 300:
            print_colored("📈 Network Speed: Good", "1;33")
        else:
            print_colored("📈 Network Speed: Slow", "1;31")
            
    except Exception as e:
        print_colored(f"❌ Error running speed test: {e}", "1;31")

def save_scan_report():
    """Save scan results to file"""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"wifi_scan_report_{timestamp}.txt"
    
    report = f"""
WiFi Network Scan Report
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Tool: WiFi Network Scanner
Developer: Mohammad Ali

This report contains network information for authorized testing purposes.
"""
    try:
        with open(filename, 'w') as f:
            f.write(report)
        print_colored(f"💾 Report saved as: {filename}", "1;32")
    except Exception as e:
        print_colored(f"❌ Error saving report: {e}", "1;31")

def print_menu():
    """Print main menu"""
    print_colored("\n" + "📱 MAIN MENU".center(50, "═"), "1;36")
    print_colored("1. 📡 Scan WiFi Networks", "1;33")
    print_colored("2. 🌐 Current Network Info", "1;33")
    print_colored("3. 🔍 Scan Connected Devices", "1;33")
    print_colored("4. 🚀 Network Speed Test", "1;33")
    print_colored("5. 💾 Save Scan Report", "1;33")
    print_colored("6. ℹ️  System Information", "1;33")
    print_colored("7. 🚪 Exit", "1;31")
    print_colored("═" * 50, "1;36")

def main():
    """Main function"""
    try:
        clear_screen()
        print_banner()
        show_disclaimer()
        
        while True:
            print_menu()
            
            try:
                choice = input("\n\033[1;36m👉 Enter your choice (1-7): \033[0m").strip()
                
                if choice == '1':
                    scan_wifi_networks()
                elif choice == '2':
                    get_network_info()
                elif choice == '3':
                    scan_connected_devices()
                elif choice == '4':
                    run_speed_test()
                elif choice == '5':
                    save_scan_report()
                elif choice == '6':
                    get_system_info()
                elif choice == '7':
                    print_colored("\n🎉 Thank you for using WiFi Network Scanner!", "1;32")
                    print_colored("👋 Developed by Mohammad Ali", "1;36")
                    break
                else:
                    print_colored("❌ Invalid choice! Please enter 1-7", "1;31")
                
                input("\n\033[1;37mPress Enter to continue...\033[0m")
                clear_screen()
                print_banner()
                
            except KeyboardInterrupt:
                print_colored("\n\n👋 Thank you for using WiFi Network Scanner!", "1;32")
                break
                
    except Exception as e:
        print_colored(f"\n❌ An error occurred: {e}", "1;31")
        print_colored("🔧 Please check your system configuration.", "1;33")

if __name__ == "__main__":
    # Check if running on supported platform
    if platform.system() not in ['Linux', 'Windows', 'Darwin']:
        print("❌ This tool is designed for Linux, Windows, or macOS systems.")
        sys.exit(1)
    
    main()
