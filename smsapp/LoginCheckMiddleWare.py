from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_fun,view_args,view_kwargs):
        modulename=view_fun.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "smsapp.HodViews":
                    pass
                elif modulename == "smsapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("admin_home"))
            elif user.user_type == "2":
                if modulename == "smsapp.StaffViews" or modulename == "smsapp.EditResultViewClass":
                    pass
                elif modulename == "smsapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("staff_home"))
            elif user.user_type == "3":
                if modulename == "smsapp.StudentViews":
                    pass
                elif modulename == "smsapp.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("student_home"))
            else:
                return HttpResponseRedirect(reverse("show_login"))
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename == "django.contrib.auth.views" or modulename == "django.contrib.admin.sites" or modulename == "smsapp.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))