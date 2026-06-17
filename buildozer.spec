[app]

title = Calculator
package.name = calculator
package.domain = org.nabeel

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

icon.filename = logo.png

android.api = 33
android.minapi = 21
android.ndk = 25b

android.archs = arm64-v8a

presplash.color = #000000

[buildozer]

log_level = 2
warn_on_root = 1
