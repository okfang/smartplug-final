from myapp.admin import admin

@admin.route('/')
def admin():
    return "admin index"