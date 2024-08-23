cls_name = <YourClassName> 
cls_bases = (YourBaseClass_1, YourBaseClass_2, ....)
cls_dict = {} 
cls_body = """
YOUR CLASS BODY
"""
exec(cls_body, globals(), cls_dict)

YourClassName_As_VariableName = type(cls_name, cls_bases, cls_dict)
#----------------------------------------------------------------------------

