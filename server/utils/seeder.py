from ..models import Author
class SeederUtil:
    def seed(self):
        self.author()

    def author(self):
        obj, created = Author.objects.get_or_create(
            first_name='Default',
            middle_name='Default',
            last_name='Default',
            id=1,
            defaults={
                'first_name': 'Default',
                'middle_name': 'Default',
                'last_name': 'Default',
            }
        )
        if created:
            obj.save()
            print('New Author: ', obj.id)
        else:
            print('Exists Author: ', obj.id)
