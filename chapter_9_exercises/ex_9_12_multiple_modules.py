import ex_9_12_2_privilege_admin_modules as pa_module

dan_admin = pa_module.Admin("Daniel", "Farias", 33, "Venezuela")

dan_admin.describe_user()

dan_admin.privileges.show_privileges()