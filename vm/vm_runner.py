import io
import dis
import sys
import types
import typing
import traceback

from contextlib import contextmanager


def compile_code(text_code: typing.Union[types.CodeType, str]) -> types.CodeType:
    """
    This is utility function with primary purpose to convert string code to code type.
    Secondary purpose - print byte code for text_code and all nested text_code
    :param text_code: text code for compiling
    :return: compiled code
    """
    if isinstance(text_code, str):
        # print("Text code:\n{}\n".format(text_code))
        code = compile(text_code, '<stdin>', 'exec')
    else:
        code = text_code

    for const in code.co_consts:
        if isinstance(const, types.CodeType):
            compile_code(const)

    # print("Disassembled code:\n")
    # dis.dis(code)

    return code


@contextmanager
def redirected(out: io._io._TextIOBase = sys.stdout, err: io._io._TextIOBase = sys.stderr) -> None:
    """
    Context manage for capturing standart outputs
    :param out: input text stream
    :param err: output text stream
    """
    saved_stdout = sys.stdout
    saved_stderr = sys.stderr
    try:
        sys.stdout = out
        sys.stderr = err
        yield
    finally:
        sys.stdout = saved_stdout
        sys.stderr = saved_stderr


def execute(code: types.CodeType, func: typing.Callable[..., None], *args: [...]) -> typing.Tuple[str, str, Exception]:
    """
    Capture all output from function execution
    :param code: code object to calculate
    :param func: functions which
    :param args: any number of arguments appropriate for function call
    :return: tuple of function execution output
    """
    stdout = io.StringIO()
    stderr = io.StringIO()

    exc = None
    with redirected(out=stdout, err=stderr):
        try:
            func(code, *args)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, file=sys.stderr)
            exc = e

    out = stdout.getvalue()
    err = stderr.getvalue()
    return out, err, exc
