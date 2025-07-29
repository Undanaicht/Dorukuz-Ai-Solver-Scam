# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: premium_ui_basic.py
# Bytecode version: 3.13.0rc3 (3571)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import os
import sys
import time
import random
import string
import base64
import hashlib
from datetime import datetime, timedelta
from colorama import init, Fore, Style
import cursor
init(autoreset=True)
VALID_LICENSE = 'KEYAUTH-axi-vEuDVy-5g1XTb-0dP'
VALID_PROXY = '0hheycfhhnkdi2i:e9di8x787fd5sxw@rp.scrapegw.com:6060'

class DiscordGeneratorPremium:
    def __init__(self):
        self.version = '2.1.1 PREMIUM'
        self.license_key = None
        self.proxy = None
        self.is_authenticated = False
        self.tokens_generated = 0
        self.emails_verified = 0
        self.captchas_solved = 0
        self.servers_joined = 0
        self.license_file = 'premium_license.dat'
        self.user_info = {'username': 'UNKOWN', 'expiry_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'), 'last_login': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'plan': 'PREMIUM'}

    def check_saved_license(self):
        """Check if license key is saved locally"""  # inserted
        try:
            if os.path.exists(self.license_file):
                with open(self.license_file, 'r') as f:
                    saved_license = f.read().strip()
                        if saved_license and self.validate_license(saved_license):
                            self.license_key = saved_license
                            self.is_authenticated = True
            return True
        except Exception as e:
            print(f'{Fore.RED}Error reading license file: {str(e)}')
            return False

    def validate_license(self, license_key):
        """Validate the entered license key"""  # inserted
        if license_key == VALID_LICENSE:
            try:
                with open(self.license_file, 'w') as f:
                    f.write(license_key)
        return True
            except Exception as e:
                print(f'{Fore.YELLOW}Warning: Could not save license key: {str(e)}')

    def validate_proxy(self, proxy):
        """Validate proxy format and connectivity"""  # inserted
        if proxy!= VALID_PROXY:
            pass  # postinserted
        return (False, 'Invalid proxy format or credentials. Please use a premium proxy.')

    def display_banner(self):
        """Display a simple banner"""  # inserted
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.CYAN}|           DISCORD TOKEN GENERATOR                   |')
        print(f'{Fore.CYAN}|                PREMIUM EDITION                      |')
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.WHITE}                Version: {self.version}')
        print('')
        if self.is_authenticated:
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f'{Fore.GREEN}|               LICENSE INFORMATION                   |')
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f"{Fore.WHITE}Licensed to: {Fore.CYAN}{self.user_info['username']}")
            print(f"{Fore.WHITE}License Key: {Fore.CYAN}{self.license_key[:8]}{'********'}{self.license_key[(-4):]}")
            print(f"{Fore.WHITE}Expiry: {Fore.CYAN}{self.user_info['expiry_date']}")
            print(f"{Fore.WHITE}Plan: {Fore.CYAN}{self.user_info['plan']}")
        return None

    def display_license_screen(self):
        """Display license activation screen"""  # inserted
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.CYAN}|            PREMIUM LICENSE ACTIVATION               |')
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.WHITE}The Premium License unlocks:')
        print(f'{Fore.GREEN}+ Unlimited token generation')
        print(f'{Fore.GREEN}+ Advanced captcha solver')
        print(f'{Fore.GREEN}+ Premium proxies')
        print(f'{Fore.GREEN}+ Phone & Email verification')
        print(f'{Fore.GREEN}+ Server joiner')
        print('')
        print(f'{Fore.CYAN}Don\'t have a license? Contact support from Telegram for purchase.')
        print('')
        license_key = input(f'{Fore.YELLOW}Enter License Key: {Fore.WHITE}')
        print(f'{Fore.CYAN}Validating license...')
        for _ in range(5):
            print('.', end='', flush=True)
            time.sleep(0.4)
        print('')
        if self.validate_license(license_key):
            self.license_key = license_key
            self.is_authenticated = True
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f'{Fore.GREEN}|                     SUCCESS                         |')
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f'{Fore.GREEN}License Successfully Activated!')
            print(f'{Fore.GREEN}Thank you for purchasing the Premium version.')
            print(f'{Fore.GREEN}All features are now unlocked.')
            time.sleep(2)
        return True

    def setup_proxy(self):
        """Configure proxy settings"""  # inserted
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.CYAN}|                   PROXY SETUP                       |')
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.YELLOW}Enter your premium proxy in the format:')
        print(f'{Fore.WHITE}username:password@host:port')
        print('')
        print(f'{Fore.CYAN}Premium proxies ensure high success rates and prevent bans.')
        print('')
        proxy = input(f'{Fore.YELLOW}Enter Proxy: {Fore.WHITE}')
        print(f'{Fore.CYAN}Testing proxy connection...')
        for _ in range(5):
            print('.', end='', flush=True)
            time.sleep(0.3)
        print('')
        is_valid, message = self.validate_proxy(proxy)
        if is_valid:
            self.proxy = proxy
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f'{Fore.GREEN}|                     SUCCESS                         |')
            print(f'{Fore.GREEN}+------------------------------------------------------+')
            print(f'{Fore.GREEN}{message}')
            print(f'{Fore.GREEN}Your premium proxy has been successfully configured.')
            time.sleep(1.5)
        return True

    def display_captcha_error(self):
        """Display captcha solver error"""  # inserted
        print(f'{Fore.RED}+------------------------------------------------------+')
        print(f'{Fore.RED}|          PRO AI SOLVER REQUIRED                     |')
        print(f'{Fore.RED}+------------------------------------------------------+')
        print(f'{Fore.RED}Advanced AI Captcha Solver Required')
        print('')
        print(f'{Fore.YELLOW}Your operation was blocked by Discord\'s captcha system.')
        print('')
        print(f'{Fore.WHITE}The Premium version includes basic captcha solving,')
        print(f'{Fore.WHITE}but the operation you\'re attempting requires the')
        print(f'{Fore.WHITE}Pro AI Solver add-on.')
        print('')
        print(f'{Fore.GREEN}Upgrade to Pro AI Solver for:')
        print(f'{Fore.CYAN}+ Advanced captcha recognition')
        print(f'{Fore.CYAN}+ Invisible solving mode')
        print(f'{Fore.CYAN}+ Unlimited solves per day')
        print(f'{Fore.CYAN}+ Higher success rates')
        print('')
        print(f'{Fore.YELLOW}Contact support from Telegram to upgrade your package.')
        input(f'\n{Fore.WHITE}Press Enter to continue...')

    def generate_tokens(self):
        """Generate Discord tokens"""  # inserted
        if not self.proxy:
            print(f'{Fore.RED}Error: Proxy not configured. Please set up your proxy first.')
            time.sleep(2)
        return None

    def verify_emails(self):
        """Verify emails for tokens"""  # inserted
        if not self.proxy:
            print(f'{Fore.RED}Error: Proxy not configured. Please set up your proxy first.')
            time.sleep(2)
        return None

    def verify_phones(self):
        """Verify phone numbers"""  # inserted
        if not self.proxy:
            print(f'{Fore.RED}Error: Proxy not configured. Please set up your proxy first.')
            time.sleep(2)
        return None

    def join_servers(self):
        """Join Discord servers"""  # inserted
        if not self.proxy:
            print(f'{Fore.RED}Error: Proxy not configured. Please set up your proxy first.')
            time.sleep(2)
        return None

    def display_stats(self):
        """Display generator statistics"""  # inserted
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.CYAN}|               GENERATOR STATISTICS                  |')
        print(f'{Fore.CYAN}+------------------------------------------------------+')
        print(f'{Fore.CYAN}Tokens Generated:  {Fore.GREEN}{self.tokens_generated}')
        print(f'{Fore.CYAN}Emails Verified:   {Fore.GREEN}{self.emails_verified}')
        print(f'{Fore.CYAN}Captchas Solved:   {Fore.GREEN}{self.captchas_solved}')
        print(f'{Fore.CYAN}Servers Joined:    {Fore.GREEN}{self.servers_joined}')
        print(f"{Fore.CYAN}License Status:    {(Fore.GREEN if self.is_authenticated else Fore.RED)}{('Active' if self.is_authenticated else 'Inactive')}")
        print(f"{Fore.CYAN}Proxy Status:      {(Fore.GREEN if self.proxy else Fore.RED)}{('Connected' if self.proxy else 'Not Configured')}")
        input(f'\n{Fore.WHITE}Press Enter to continue...')

    def run(self):
        """Run the main application"""  # inserted
        cursor.hide()
        try:
            if not self.check_saved_license():
                self.display_banner()
                if not self.display_license_screen():
                    print(f'{Fore.RED}License activation failed. Exiting...')
                    time.sleep(1)
                    sys.exit(1)
        pass
        self.display_banner()
        print(f'\n{Fore.CYAN}Main Menu:')
        print(f'{Fore.CYAN}1. Generate Tokens')
        print(f'{Fore.CYAN}2. Configure Proxy')
        print(f'{Fore.CYAN}3. View Statistics')
        print(f'{Fore.CYAN}0. Exit')
        choice = input(f'\n{Fore.WHITE}> ')
        if choice == '1':
            self.generate_tokens()
if __name__ == '__main__':
    try:
        generator = DiscordGeneratorPremium()
        generator.run()
        cursor.show()
    except KeyboardInterrupt:
        print(f'\n{Fore.YELLOW}Program terminated by user')