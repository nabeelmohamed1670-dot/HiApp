[app]

title = Calculator
package.name = calculator
package.domain = org.nabeel

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy==2.3.0

orientation = portrait

fullscreen = 0

icon.filename = icon.png

android.api = 34
android.minapi = 21

android.permissions = INTERNET

[buildozer]

log_level = 2
warn_on_root = 1
