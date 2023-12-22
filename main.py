import subprocess as sp
import re


# grep -e 'CONFIG_*=y' /usr/src/linux/.config | grep -v "not set" /usr/src/linux/.config > ~/Documents/config_file
class Dot_Conf:
    def __init__(self):
        pass

    @property  # {config name: mode or setting}
    def user_settings_from_file(self: dict) -> dict:
        user_settings_hmap = {}
        with open("user_settings") as dot_config:
            dot_config = dot_config.read().strip().split()
            # regex searches for strings starting with "CON"
            dot_config = [re.search("^[C].[N].*", txt) for txt in dot_config]
            for val in dot_config:
                if val is not None:
                    txt = val.group().split("=", 1)
                    user_settings_hmap.update({txt[0]: txt[1]})
        return user_settings_hmap

    @property
    def user_settings_from_system(self: dict) -> dict:
        user_settings_sys = {}
        lspci_drivers = sp.run(["lspci", "-nnk"], stdout=sp.PIPE)
        lspci_drivers = lspci_drivers.stdout.decode("utf-8").split("\n")
        lspci_drivers = [re.search("[es]:.*", txt) for txt in lspci_drivers]
        for driver in lspci_drivers:
            if driver is not None:
                print(f"{driver}")
                txt = driver.group().strip().split(" ")
                user_settings_sys.update({txt[1].upper(): "y"})
        return user_settings_sys

    def compare(self, *args, **kwargs) -> any:
        for itm in self.user_settings_from_system.items():
            print(itm[0])



if __name__ == "__main__":
    testing = Dot_Conf()
    testing.compare()
