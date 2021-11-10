from django.urls import path, include
from .views import (home,
                    todoList,
                    todoListCreate,
                    toDo_list,
                    todoListUpdate,
                    todoListDelete,
                    toDo_detail,
                    TodoList,
                    TodoDetail,
                    TodoListCreate,
                    TodoRetrieveUpdateDelete,
                    TodoConcListCreate,
                    TodoConcRetreiveUpdateDelete,
                    TodoVSListRetreive,
                    TodoMVS
                    )
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todovs-list', TodoVSListRetreive)
router.register('todomvs-list', TodoMVS)

urlpatterns = [
    path('', home),
    # path('todoList/', todoList),
    # path('todoListCreate/', todoListCreate),
    # path('toDo_list/', toDo_list),
    # path('todoListUpdate/<int:pk>/', todoListUpdate),
    # path('todoListDelete/<int:pk>/', todoListDelete),
    # path('toDo_detail/<int:pk>/', toDo_detail),
    # path('todo-list/', TodoList.as_view()),
    path('todo-list/', TodoListCreate.as_view()),
    # path('todo-list/', TodoConcListCreate.as_view()),
    # path('todo-detail/<int:pk>', TodoDetail.as_view()),
    # path('todo-detail/<int:pk>', TodoRetrieveUpdateDelete.as_view()),
    path('todo-detail/<int:pk>', TodoConcRetreiveUpdateDelete.as_view()),
    path('', include(router.urls))

]
