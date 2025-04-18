from chainHAndler import UpperCaseTextHandler, ReplaceTextHandle


def test_upper_case_text_handler():
    text = 'hello'
    expected_result = "HELLO"
    handler = UpperCaseTextHandler()

    assert handler.handle(text) == expected_result

def test_replace_text_handler():
    text = 'ewqdsaffsfddf'
    expected_result = "ewqdsa  s dd "

    handler = ReplaceTextHandle()

    assert handler.handle(text) == expected_result



def test_handlers_chain():
    text = 'ewqdsaffsfddf'
    expected_result = "EWQDDSA  S DD "

    handler1 = ReplaceTextHandle()
    handler2 = UpperCaseTextHandler()

    handler1.set_next(handler2)
    assert handler1.handle(text) == expected_result