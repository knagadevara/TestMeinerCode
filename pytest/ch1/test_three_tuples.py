from collections import namedtuple

Task = namedtuple( 'Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

def test_default_values():
    """To check if the Default values got assigned properly"""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2

def test_member_access():
    """ Checking if the field's can be set other than defaults"""
    t3 = Task( "Text God" , "Kumar" )
    assert t3.summary == "Text God"
    assert t3.owner == "Kumar"
    assert (t3.done , t3.id) == (False , None)

def test_asdict():
    '''Tests if returns dictionary'''
    t_task = Task("do something cool", 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary': 'do something cool',
 	                'owner': 'okken',
 	                'done': True,
 	                'id': 21}
    assert t_dict == expected

def test_replace():
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected