class DbRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'users':
            return 'users'
        elif model._meta.db_table == 'products':
            return 'products'
        elif model._meta.db_table == 'orders':
            return 'orders'
        return None

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'users' and model_name == 'user':
            return True
        if db == 'products' and model_name == 'product':
            return True
        if db == 'orders' and model_name == 'order':
            return True
        return False
