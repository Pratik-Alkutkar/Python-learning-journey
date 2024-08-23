def abstract(F):
    F.is_virtual = True
    return F

class interface(type):
    def __new__(cls, c_name, c_super, c_dict):
        abstract_method_names = []
        for attr in c_dict.values():
            if type(attr) == type(lambda : None) and 'is_virtual' in attr.__dict__:
                abstract_method_names.append(attr.__name__)
        c_dict['abstract_methods'] = abstract_method_names

        liability_list = []
        for (name, attr) in c_dict.items():
            if type(attr) == type(lambda : None) and 'is_virtual' in attr.__dict__ and not name in liability_list:
                liability_list.append(name)                
                
        for super_cls in c_super: 
            for c in super_cls.__mro__:
                if c != object:
                    for (name, attr) in c.__dict__.items():
                        if type(attr) == type(lambda : None) and 'is_virtual' in attr.__dict__ and not name in liability_list:
                            liability_list.append(name)
        c_dict['liabilities'] = liability_list

        liability_fulfilled = dict.fromkeys(liability_list, False)
        for method_name in liability_list:
            if method_name in c_dict.keys():
                attr = c_dict[method_name]
                if type(attr) == type(lambda : None) and not 'is_virtual' in attr.__dict__:
                    liability_fulfilled[method_name] = True

        liability_unfulfilled = []
        is_concrete = True
        for (name, flg) in liability_fulfilled.items():
            if flg != True:
                is_concrete = False
                liability_unfulfilled.append(name)

        c_dict['unfulfilled_liabilities'] = liability_unfulfilled 
        if is_concrete:
            c_dict['concrete'] = True
        else:
            c_dict['concrete'] = False
        
        return type.__new__(cls, c_name, c_super, c_dict) 

    
    def __call__(self, *args, **kwargs):
        if self.concrete == True:
            return type.__call__(self, *args, **kwargs)
        else:
            raise TypeError("Abstract methods:", self.unfulfilled_liabilities)
    
class B1(metaclass = interface): 
    @abstract
    def f1(self):
        pass

    @abstract
    def f2(self):
        pass

print(B1.abstract_methods, B1.liabilities, B1.unfulfilled_liabilities, B1.concrete)
try:
    b1 = B1()
except:
    import sys
    exc_name, exc_data, _ = sys.exc_info()
    print(exc_name, exc_data, sep=':')

class B2(metaclass = interface):
    @abstract
    def f3(self):
        pass

    @abstract
    def f4(self):
        pass

print(B2.abstract_methods, B2.liabilities, B2.unfulfilled_liabilities, B2.concrete)
try:
    b2 = B2()
except:
    import sys
    exc_name, exc_data, _ = sys.exc_info()
    print(exc_name, exc_data, sep=':')

class D(B1, B2):
    def f1(self):
        pass
    def f2(self):
        pass
    
print(D.abstract_methods, D.liabilities, D.unfulfilled_liabilities, D.concrete)
try:
    d = D()
except:
    import sys
    exc_name, exc_data, _ = sys.exc_info()
    print(exc_name, exc_data, sep=':')

class D1(B1, B2):
    def f1(self):
        pass
    def f2(self):
        pass
    def f3(self):
        pass
    def f4(self):
        pass

print(D1.abstract_methods, D1.liabilities, D1.unfulfilled_liabilities, D1.concrete)
try:
    d1 = D1()
except:
    import sys
    exc_name, exc_data, _ = sys.exc_info()
    print(exc_name, exc_data, sep=':')
print("type(d1):", type(d1))
