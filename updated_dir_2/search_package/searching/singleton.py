def singleton(myclass):
    instance={}
    def getInstance(*args,**kwargs):

        if myclass not in instance:
            instance[myclass]=myclass(*args,**kwargs)

        return instance
    return getInstance
