class Cricket2K:
    def __init__(self,name,role,rating,pid=0):
        self.pid=pid
        self.name=name
        self.role=role
        self.rating=rating

    def __str__(self):
        return 'Cricket2K: id:{} Name:{} Role:{} Rating:{}'.format(self.pid,self.name,self.role,self.rating)
