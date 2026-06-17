[app]

title = Calculator
package.name = calculator
package.domain = org.nabeel

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait

fullscreen = 0

icon.filename = logo.png

android.api = 34
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a, armeabi-v7a

presplash.color = #000000

[buildozer]

log_level = 2
warn_on_root = 1
