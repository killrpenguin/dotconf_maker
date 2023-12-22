from os import system
import re

# grep -e 'CONFIG_*=y' /usr/src/linux/.config | grep -v "not set" /usr/src/linux/.config > ~/Documents/config_file
class My_Dot_Conf:
    def __init__(self):
        self.user_settings_hmap = {} #hash map key: {config name: mode or setting}

    def user_settings(self):
        with open("user_settings") as dot_config:
            dot_config = dot_config.read().strip().split()
            # regex searches for strings starting with "CON"
            dot_config = [re.search("^[C].[N].*", txt) for txt in dot_config]
            for val in dot_config:
                if val is not None:
                    txt = val.group().split("=", 1)
                    self.user_settings_hmap.update({txt[0]:txt[1]})

            for tst in self.user_settings_hmap.items():
                print(f"{tst}")

    def get_config(self):
        pass

if __name__ == '__main__':
    testing = My_Dot_Conf()
    testing.user_settings()
