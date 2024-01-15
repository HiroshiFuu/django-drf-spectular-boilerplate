from drf_spectacular.openapi import AutoSchema, ComponentRegistry


class CustomAutoSchema(AutoSchema):
    def get_operation(self, path, path_regex, path_prefix, method, registry: ComponentRegistry):
        operation = super().get_operation(path, path_regex, path_prefix, method, registry)

        if operation and operation['tags'] == ['dj-rest-auth']:
            operation['tags'] = ['Account']

        return operation
