from django.urls import path
from . import views

""".. function:: path(route, view, kwargs=None, name=None)

   Defines a URL pattern to match the given route and view function.

   :param str route: The URL pattern to match. It may contain angle brackets to capture parameters.
   :param view: The view function to call when the URL pattern is matched.
   :type view: function or str
   :param dict kwargs: Optional keyword arguments to pass to the view function.
   :param str name: Optional name for the URL pattern.

   :returns: URL pattern for the specified route and view.
   :rtype: django.urls.path

.. function:: views.teacher_info(request, pk)

   View function to display information about a specific teacher.

   :param HttpRequest request: The HTTP request object.
   :param str pk: The primary key of the teacher to display information about.

   :returns: HTTP response displaying information about the teacher.
   :rtype: django.http.HttpResponse

.. function:: path('teacher_info/<str:pk>/', views.teacher_info, name="teacher_info")

   Defines a URL pattern for displaying information about a specific teacher.

   :param str pk: The primary key of the teacher to display information about.

   :returns: URL pattern for the teacher information view.
   :rtype: django.urls.path
"""


urlpatterns = [
   path('',views.common_page,name="common_page")


    
""".. function:: path(route, view, name=None)

        Defines a URL pattern to match the given route and view function.

        :param str route: The URL pattern to match.
        :param view: The view function to call when the URL pattern is matched.
        :type view: function or str
        :param str name: Optional name for the URL pattern.

        :returns: URL pattern for the specified route and view.
        :rtype: django.urls.path

        .. _create-teacher-url:

        URL Pattern for Creating a Teacher
        -----------------------------------

        The following URL pattern maps requests to create a new teacher to the view function
        ``views.create_teacher``:

        .. code-block:: python

            from django.urls import path
            from . import views

            urlpatterns = [
                path('create_teacher/', views.create_teacher, name="create_teacher"),
            ]

        This URL pattern is used to create a new teacher. When a user visits the URL
        ``/create_teacher/``, it triggers the ``create_teacher`` view function, which is
        responsible for rendering the form to create a new teacher and handling form submission.

        For more information on Django URL patterns, see:
        `Django URL dispatcher documentation <https://docs.djangoproject.com/en/stable/topics/http/urls/>`_

"""

urlpatterns = [



   path('home/',views.home,name="home"),


   path('',views.common_page,name="common_page"),


   path('login/',views.login_admin,name="login"),
   path('register/',views.register,name="register"),
   path('logout/',views.logout_user,name="logout"),
   
   
    path('create_teacher/',views.create_teacher,name="create_teacher"), 
    path('create_teacher/',views.create_teacher,name="create_teacher"),
    path('teacher_info/<str:pk>/',views.teacher_info,name="teacher_info"),
    
    
    
    path('create_department/',views.create_department,name="create_department"),
   
]