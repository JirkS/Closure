def append_jecna_postfix(uzivatelske_jmeno: str):
    return uzivatelske_jmeno + "@spsejecna.cz"


def append_seznam_postfix(uzivatelske_jmeno: str):
    return uzivatelske_jmeno + "@seznam.cz"


def create_email(appender_function, username: str):
    return appender_function(username)


try:
    appender_postfix = append_jecna_postfix
    print(appender_postfix("novak"))
    appender_postfix = append_seznam_postfix
    print(appender_postfix("syrovatko"))

    appender_postfix = append_jecna_postfix
    print(create_email(appender_postfix, "novak"))
    # ma vratit novak@spsejecna.cz
    appender_postfix = append_seznam_postfix
    print(create_email(appender_postfix, "syrovatko"))
    # ma vratit novak@seznam.cz
except Exception as e:
    print(e)
