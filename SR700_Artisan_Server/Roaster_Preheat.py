#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SR700-Artisan-PDServer, released under GPLv3
# Roaster Run Recipe

import Pyro4

def main():
    roast_control = Pyro4.Proxy("PYRONAME:roaster.sr700")

    roast_control.set_time(1500)
    roast_control.set_temperature(120)
    roast_control.set_fan_speed(9)
    roast_control.run_roast()

if __name__ == '__main__':
    main()
