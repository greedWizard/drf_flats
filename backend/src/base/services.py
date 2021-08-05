from typing import Any, Dict, List, Tuple, Type
from django.db.models import Model
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from rest_framework.exceptions import NotFound


class IServiceBase:
    model: Type[Model] = None
    basequeryset: Type[QuerySet] = None


class IServiceRead(IServiceBase):
    paginator_class: Type[Paginator] = Paginator
    page_size: Type[int] = 10
    NOT_FOUND_MESSAGE: Type[str] = 'Not Found'

    def fetch(self, page=None, **filters) -> QuerySet:
        ''' Returns queryset of filtered objects '''
        query = self.basequeryset.filter(**filters).all()

        if page:
            paginator = self.paginator_class(query, self.page_size)
            return paginator.get_page(page)
        return query
        
    def retrieve(self, pk: Any) -> Model:
        ''' Return specific objects by pk '''
        try:
            return self.basequeryset.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound(self.NOT_FOUND_MESSAGE)
    

class IServiceAction(IServiceBase):
    def create(self, **data) -> Model:
        ''' Create new object '''
        new_obj = self.model(**data)
        new_obj.save()
        
        return new_obj
    
    def update(self, update_data: Dict, **filters) -> QuerySet:
        ''' Update type of objects '''
        objects = self.basequeryset.filter(**filters).all()
        objects.update(**update_data)
        return objects
    
    def delete(self, **filters) -> Tuple[int, Dict[str, int]]:
        ''' Deletes type of objects '''
        return self.basequeryset.filter(**filters).delete()

    def bulk_delete(self, *pks) -> List[Any]:
        ''' Delete multiple objects '''
        deleted = []
        for pk in pks:
            try:
                deleted.append(
                    self.basequeryset.get(pk=pk).delete()
                )
            except self.model.DoesNotExist:
                continue
        return deleted


class IService(IServiceAction, IServiceRead):
    ''' 
        все действия с бд должны производиться только через наследников данного класса
        нельзя вызывать методы менеджера .delete, .create, .update и т.д. вне
        его наследников! 
    '''
    pass