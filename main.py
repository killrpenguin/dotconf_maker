from os import system
import re


# grep -e 'CONFIG_*=y' /usr/src/linux/.config | grep -v "not set" /usr/src/linux/.config > ~/Documents/config_file
class Dot_Conf:
    def __init__(self):
        pass

    @property  # {config name: mode or setting}
    def user_settings(self):
        user_settings_hmap = {}
        with open("user_settings") as dot_config:
            dot_config = dot_config.read().strip().split()
            # regex searches for strings starting with "CON"
            dot_config = [re.search("^[C].[N].*", txt) for txt in dot_config]
            for val in dot_config:
                if val is not None:
                    txt = val.group().split("=", 1)
                    user_settings_hmap.update({txt[0]: txt[1]})
                    # self.user_settings_user_settings_hmap.update({txt[0]:txt[1]})
        return user_settings_hmap

    def get_config(self):
        pass


if __name__ == '__main__':
    testing = Dot_Conf()
    print(testing.user_settings)
