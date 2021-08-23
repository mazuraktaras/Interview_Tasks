import copy


class Website:

    def __init__(self, name, domain, description, author, **kwargs):

        self.name = name
        self.domain = domain
        self.description = description
        self.author = author
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):

        summary = [f'Website "{self.name}"\n', ]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')
        return ''.join(summary)


class Prototype:
    def __init__(self):

        self.objects = dict()

    def register(self, identifier, obj):

        self.objects[identifier] = obj

    def unregister(self, identifier):

        del self.objects[identifier]

    def clone(self, identifier, **attrs):

        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect object identifier: {identifier}')
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])
        return obj


if __name__ == '__main__':
    keywords = ('python', 'data', 'apis', 'automation')

    website1 = Website(name='Site',
                       domain='www.my.com',
                       description='My site',
                       author='Taras')

    website2 = Website(name='Python Site',
                       domain='www.python.com',
                       description='Python main site',
                       author='People',
                       category='Learning',
                       keywords=keywords)

    prototype = Prototype()

    prototype.register('clone_website1', website1)
    website3 = prototype.clone('clone_website1', author='Taras Mazurak')

    prototype.register('clone_website3', website3)

    print(website1)
    print(website2)
    print(website3)
    print()
    print(prototype.objects)
