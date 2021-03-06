from django.urls import path
from .views import (
    list_typedocs,
    create_typedocs,
    update_typedocs,
    delete_typedocs,
    list_docs,
    create_doc,
    update_doc,
    setdate_doc,
    delete_docs,
    typedoc_filter_con_respuesta,
    create_procedencia,
)

urlpatterns = [
    # TIPO DE DOCUMENTOS
    path('tipos/', list_typedocs, name='list_typedocs'),
    path('tipos/add/', create_typedocs, name='typedocs_add'),
    path('tipos/edit/<int:typedoc_id>/', update_typedocs, name='typedocs_edit'),
    path('tipos/remove/<int:typedoc_id>/', delete_typedocs, name='typedocs_delete'),
    path('tipos/filter/<int:typedoc_id>/', typedoc_filter_con_respuesta, name='typedoc_filter_con_respuesta'),
    # DOCUMENTOS
    path('', list_docs, name='list_docs'),
    path('add/', create_doc, name='docs_add'),
    path('edit/<int:doc_id>/', update_doc, name='docs_edit'),
    path('setdate/<int:doc_id>/', setdate_doc, name='docs_setdate'),
    path('remove/<int:doc_id>/', delete_docs, name='docs_delete'),
    # PROCEDENCIA
    path('procedencia/add/', create_procedencia, name='create_procedencia'),

]
