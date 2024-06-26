from django.urls import include, path
from rest_framework.routers import SimpleRouter

from cats.views import CatViewSet

router = SimpleRouter()
router.register('cats', CatViewSet)
# Адреса будут соответственно cat-list и cat-detail
# Можно указать префикс иной:
# router.register('cats', CatViewSet, basename='tiger')
# Тогда будут tiger-list и tiger-detail

# DefaultRouter — это расширенная версия SimpleRouter: он умеет всё то же,
# что и SimpleRouter, а в дополнение ко всему генерирует корневой эндпоинт
# /, GET-запрос к которому вернёт список ссылок на все ресурсы,
# доcтупные в API.
# У этого эндпоинта тоже есть name: api-root.

urlpatterns = [
   path('', include(router.urls)),
]
