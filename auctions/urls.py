from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register", views.register_player, name="register"),
    path("c_register", views.register_club, name="c_register"),
    path('player_home',views.player_home),
    path('club_home',views.club_home),
    path('participate/<int:id>/',views.participate),
    path('participatec/<int:id>/',views.participatec),
    path('my',views.my),
    path('myc',views.myc),
    path('registered/<int:auction>/',views.registred),
    path('addbid/<int:id>/<int:pid>/',views.add_bid),
    path('view',views.viewbid),
    path('accept/<int:cid>/',views.acceptoffer),
    path('myclub',views.myclub),
    path('edit-player',views.editplayer),
    path('edit-club',views.editculb),
    path('ourp',views.myplayers),
    path('changep',views.changepassword_player),
    path('changec',views.changepassword_club),
    path('cat', views.view_catagories),




    # path("create",views.create),
]

