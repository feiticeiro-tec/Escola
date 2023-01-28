from functools import wraps

class GenericModel:
    def set_model_get(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.get_response, code=200)
            @namespace.expect(self.get)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_delete(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.doc({},code=204)
            @namespace.expect(self.delete)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_put(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.put_response, code=200)
            @namespace.expect(self.put)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func

    def set_model_post(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.post_response, code=201)
            @namespace.expect(self.post)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func
    
    def set_model_patch(self, namespace):
        def capture_func(f):
            @wraps(f)
            @namespace.marshal_with(self.patch_response, code=201)
            @namespace.expect(self.patch)
            def capture_args(*args, **kw):
                return f(*args, **kw)

            return capture_args
        return capture_func
